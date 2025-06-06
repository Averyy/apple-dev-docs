# Loading Reality Composer files manually without generated code

**Framework**: Realitykit

Load Reality Composer files that aren’t part of your Xcode project.

#### Overview

Although Xcode generates loading methods for all Reality Composer files in your Xcode project, there are times when you need to load them without the benefit of those generated loader methods. This scenario can happen, for example, when loading content downloaded as part of an in-app purchase bundle from the App Store.

You can manually load scenes synchronously or asynchronously. Unless your Reality Composer scene is very small, use the asynchronous method, which loads scenes in the background. Synchronous loading occurs on the main thread, so your app may become unresponsive if you use that method to load even moderately complex scenes.

##### Create a Scene Url

Regardless of whether you plan to load the scene synchronously or asynchronously, the first step is to create a URL that points to the Reality file that contains the scene you want to load. Then append the name of the scene to the URL.

Here’s an example of building a URL to load a scene from a Reality file inside your app’s bundle:

```swift
func createRealityURL(filename: String, 
                      fileExtension: String, 
                      sceneName:String) -> URL? {
    // Create a URL that points to the specified Reality file. 
    guard let realityFileURL = Bundle.main.url(forResource: filename, 
                                               withExtension: fileExtension) else {
        print("Error finding Reality file \(filename).\(fileExtension)")
        return nil
    }

    // Append the scene name to the URL to point to 
    // a single scene within the file.
    let realityFileSceneURL = realityFileURL.appendingPathComponent(sceneName, 
                                                                    isDirectory: false)
    return realityFileSceneURL
} 
```

##### Load the Scene Asynchronously From the Url

[`Entity`](entity.md) provides the [`loadAnchorAsync(contentsOf:withName:)`](entity/loadanchorasync(contentsof:withname:).md) method for loading scenes asynchronously from a URL. Loading in this manner uses the Combine framework and returns an [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable) object that you use to cancel scene loading.

You must maintain a strong reference to the returned [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable) object until loading has completed. Otherwise, the load process cancels as soon as the returned [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable) object is deallocated. To keep a strong reference to the returned [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable) object, store it in an array.

This example shows how to declare an array variable in your view controller or coordinator class to hold instances of [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable):

```swift
var streams = [Combine.AnyCancellable]()
```

Load your scene asynchronously, storing the [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable) object in that array using the [`store(in:)`](https://developer.apple.com/documentation/Combine/AnyCancellable/store(in:)-6cr9i) method instead of the [`append(_:)`](https://developer.apple.com/documentation/Swift/Array/append(_:)) method. In this way, you ensure that the system won’t cancel your load operation.

This example shows how to asynchronously load a scene from a [`URL`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/LaunchServicesConcepts/LSCGlossary/LSCGlossary.html#//apple_ref/doc/uid/TP30000999-CH205-CBABFJEB):

```swift
func loadRealityComposerSceneAsync (filename: String,
                                    fileExtension: String,
                                    sceneName: String,
                                    completion: @escaping (Swift.Result<(Entity & HasAnchoring)?, Swift.Error>) -> Void) {

    guard let realityFileSceneURL = createRealityURL(filename: filename, fileExtension: fileExtension, sceneName: sceneName) else {
        print("Error: Unable to find specified file in application bundle")
        return
    }

    let loadRequest = Entity.loadAnchorAsync(contentsOf: realityFileSceneURL)
    let cancellable = loadRequest.sink(receiveCompletion: { (loadCompletion) in
        if case let .failure(error) = loadCompletion {
            completion(.failure(error))
        }
    }, receiveValue: { (entity) in
        completion(.success(entity))
    })
    cancellable.store(in: &streams)
}
```

> **Note**: If you use the [`store(in:)`](https://developer.apple.com/documentation/Combine/AnyCancellable/store(in:)-6cr9i) method instead of [`append(_:)`](https://developer.apple.com/documentation/Swift/Array/append(_:)), you don’t have to remove the [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable) object from the array after loading has finished. When using that method, the [`AnyCancellable`](https://developer.apple.com/documentation/Combine/AnyCancellable) object removes itself automatically from the array once it has finished loading.

##### Load the Scene Synchronously From the Url

Call the [`loadAnchor(contentsOf:withName:)`](entity/loadanchor(contentsof:withname:).md) method on [`Entity`](entity.md) and pass in a scene URL.

```swift
func loadRealityComposerScene (filename: String,
                                fileExtension: String,
                                sceneName: String) -> (Entity & HasAnchoring)? {
    guard let realitySceneURL = createRealityURL(filename: filename,
                                                 fileExtension: fileExtension,
                                                 sceneName: sceneName) else {
        return nil
    }
    let loadedAnchor = try? Entity.loadAnchor(contentsOf: realitySceneURL)

    return loadedAnchor
}

```

##### Load a Usdz File Asynchronously

You can load USDZ files asynchronously in the background using the [`loadModelAsync(contentsOf:withName:)`](entity/loadmodelasync(contentsof:withname:).md) method on [`Entity`](entity.md). Asynchronous loading of USDZ files also requires the [`Combine`](https://developer.apple.com/documentation/Combine) framework. To receive the scene once it’s loaded, the receiving class must conform to the [`Subscriber`](https://developer.apple.com/documentation/Combine/Subscriber) protocol.

This example shows you how to conform a view controller to the [`Subscriber`](https://developer.apple.com/documentation/Combine/Subscriber) protocol so it can receive the asynchronously loaded scene:

```swift
extension ViewController : Subscriber {

    // loadModelAsync loads a ModelEntity, so declare 
    // that as the Input type.
    typealias Input = ModelEntity

    // If loadModelAsync fails, it returns an Error instance, 
    // so declare Error as the Failure associated-object type.
    typealias Failure = Error

    // The publisher has finished, so ask it for the result 
    // as a single item.
    func receive(subscription: Subscription) {
        subscription.request(.max(1))
    }

    // You receive the model here and assign it to a property
    // so you can use it outside of this method. 
    func receive(_ input: ModelEntity) -> Subscribers.Demand {
        // Assign to robot, a property declared in your 
        // main view-controller class
        robot = input
        return .none
    }

    // When the publisher is done - either it has sent the 
    // model or it has errored - this method is called.
    func receive(completion: Subscribers.Completion<Error>) {
        switch (completion) {
            case .failure(let error):
                print("Error loading model: \(error)")
            case .finished:
                print("Model loaded successfully")
        }
    }
}
```

Once you set up your view controller as a [`Subscriber`](https://developer.apple.com/documentation/Combine/Subscriber), you can start loading a USDZ file as in this example:

```swift
let request = Entity.loadModelAsync(contentsOf: robotURL)
request.receive(subscriber: self)
```

For more information on using the [`Combine`](https://developer.apple.com/documentation/Combine) Framework, see [`Receiving and Handling Events with Combine`](https://developer.apple.com/documentation/Combine/receiving-and-handling-events-with-combine).

##### Load a Usdz File Synchronously

You can also load individual 3D models from USDZ files for use in your Reality Composer scenes. This is especially useful, for example, for loading objects that you might spawn multiple times in response to user input. In that case, you don’t want the asset loaded as part of your Reality Composer scene. Instead, you want to load it separately and add it to your scene when needed.

You can load a model synchronously using the [`loadModel(contentsOf:withName:)`](entity/loadmodel(contentsof:withname:).md) function on [`Entity`](entity.md), as in this example:

```swift
var loadedModel: Entity?
if let theURL = Bundle.main.url(forResource: "myModel", withExtension: "usdz") {
    let loadedModel = try? Entity.loadModel(contentsOf: theURL)
}
```

## See Also

- [Creating 3D Content with Reality Composer](creating-3d-content-with-reality-composer.md)
  Assemble assets into a dynamic 3D composition that you can add to a scene in your app, or share with AR Quick Look.
- [Loading Reality Composer files using generated code](loading-reality-composer-files-using-generated-code.md)
  Leverage automatically generated code to load scenes from Xcode.
- [Adding elements to a 3D scene](adding-elements-to-a-3d-scene.md)
  Add assets to your scene from Reality Composer’s library, or import custom assets.
- [Configuring elements in a scene](configuring-elements-in-a-scene.md)
  Define the appearance and behavior of objects in a scene.
- [Arranging elements in a scene](arranging-elements-in-a-scene.md)
  Manipulate objects to complete your Reality Composer scene.
- [Manipulating Reality Composer scenes from code](manipulating-reality-composer-scenes-from-code.md)
  Make programmatic changes to your scenes at runtime.
- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
  Create procedurally generated shape primitives to your Reality Composer scene.
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit/loading-reality-composer-files-manually-without-generated-code)*