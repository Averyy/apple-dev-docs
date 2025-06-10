# Loading Reality Composer files using generated code

**Framework**: RealityKit

Leverage automatically generated code to load scenes from Xcode.

#### Overview

When you add Reality Composer to your project, Xcode automatically generates code to handle many common tasks, such as loading scenes, retrieving objects, and triggering behaviors.

When you build in Xcode, it converts any Reality Composer file in the current target into a more compact, read-only format called a  , which has the extension `.reality`. You can also export Reality files directly from Reality Composer to use, for example, as downloadable content for your app. Although Xcode accepts both file types, you’ll typically use these editable Reality Composer project files during development.

Xcode generates both asynchronous and synchronous load methods. Unless your Reality Composer scene is very small, you should use the asynchronous method, which loads scenes in the background. Synchronous loading always occurs on the main thread, so your app may become unresponsive if you use that method to load even moderately complex scenes.

##### Load Reality Files Asynchronously Using Generated Code

For every scene in a Reality file, Xcode generates an asynchronous loading method. This method helps keep your app responsive when loading larger scenes. Xcode bases the name of each generated asynchronous loading method on the name of the scene it loads and the Reality file that contains it. Instead of returning the loaded object directly, these asynchronous loading methods return the loaded scene through a completion block.

The following example code loads a scene using the generated asynchronous load function:

```swift
Experience.loadBoxAsync(completion: { (result) in
    do {
        let boxScene = try result.get()
        // ...
    } catch {
        // handle error
    }
})
```

##### Load Reality Files Synchronously Using Generated Code

Xcode also creates a synchronous loading method for each scene in your Reality Composer projects. As with generated asynchronous methods, it bases the name of each generated method on the name of the scene it loads and the Reality Composer file that contains that scene.

The following example code synchronously loads a scene called Box from a Reality Composer project called Experience:

```swift
// Load the Box scene synchronously from the Experience Reality file
do {
    let boxAnchor = try Experience.loadBox()
    // ...
} catch {
    // handle error
}
```

> ❗ **Important**: Use RealityKit’s synchronous loading methods from the main thread only. RealityKit throws a runtime exception if you attempt to use it from any other thread. If you need to load a scene on a background thread, use asynchronous loading instead.

##### Show the Scene

After you load the Reality Composer scene, you display it to the user by adding it to the scene anchors of an [`ARView`](arview.md). Reality Composer scenes contain anchoring information, which allows RealityKit to automatically find an appropriate surface, object, or image, and anchor your scene to it. For example, RealityKit automatically places a horizontally anchored scene as soon as ARKit detects a flat horizontal surface. Similarly, it displays a scene with an image anchor when ARKit detects the specified image at the correct size.

To use automatic anchoring, add the loaded scene to the view’s anchors:

```swift
arView.scene.anchors.append(anchor)
```

For more control, you can also anchor your scene manually. See [`Taking Control of Scene Anchoring`](taking-control-of-scene-anchoring.md).

##### Remove the Scene

To remove the Reality Composer scene so the user can no longer see or interact with it, remove the object from the view’s anchors.

```swift
arView.scene.anchors.remove(anchor)
```

To remove all content from the view, use the [`removeAll()`](entity/componentset/removeall().md) method instead.

```swift
arView.scene.anchors.removeAll()
```

## See Also

- [Creating 3D Content with Reality Composer](creating-3d-content-with-reality-composer.md)
  Assemble assets into a dynamic 3D composition that you can add to a scene in your app, or share with AR Quick Look.
- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)
  Load Reality Composer files that aren’t part of your Xcode project.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loading-reality-composer-files-using-generated-code)*