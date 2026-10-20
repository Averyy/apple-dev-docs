# Loading entities from a file

**Framework**: RealityKit  
**Role**: Article

Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.

#### Overview

Use a load method to bring an entity stored in a file into your app. You can load USD files (.usd, .usda, .usdc, .usdz) and Reality files (.reality) this way.

##### Load an entity hierarchy synchronously

Use the `load(named:in:)` method to load an entity hierarchy from a USD or Reality file stored in a bundle. This method returns only after the operation completes. Omit the bundle parameter from the method call to load from the app’s main bundle:

```swift
let entity = try? Entity.load(named: "MyEntity") 
```

To load an entity stored at a specific location in the file system, create a file URL and use the [`load(contentsOf:withName:)`](./entity/load%28contentsof,withname%29.md) method instead:

```swift
let url = URL(fileURLWithPath: "path/to/MyEntity.usdz")
let entity = try? Entity.load(contentsOf: url)
```

The load methods preserve the entity hierarchy in the loaded file and return the root entity in the scene that the USD or Reality file contains. The entity can have any number of descendant entities that you access using the methods of the [`HasHierarchy`](./hashierarchy.md) protocol. Accessing entities this way enables you to store and import sophisticated compositions from a single asset.

##### Load an entity hierarchy asynchronously

Synchronous load operations block the thread on which you call them. To maintain a smooth user interface, use an asynchronous load instead. The entity initializer has an asynchronous overload. For example, load from a bundle asynchronously by calling the method:

```swift
_ = try! await Entity(named: "MyEntity")   // From the app's main bundle.
```

Call the asynchronous version of these initializers by prefacing the call with the await keyword from asynchronous methods or from inside of a [`Task`](../Swift/task.md) These overloads give you access to the full set of features [Concurrency](../Swift/concurrency.md) provides.

##### Load an anchor entity

When you want to load a composition rooted by an anchor entity, you can instead use the [`loadAnchor(named:in:)`](./entity/loadanchor%28named,in%29.md) method, or one of its siblings. These methods behave like the related load methods, except that they specifically return an [`AnchorEntity`](./anchorentity.md) instance that you can add to your scene:

```swift
if let anchor = try? Entity.loadAnchor(named: "MyEntity") {
    arView.scene.addAnchor(anchor)
}
```

As with the load methods, the load anchor methods preserve the entity hierarchy.

> **Note**: The load anchor methods work only for Reality files.

##### Load a flattened model or body-tracked entity

To load a model or body-tracked entity with internal structure that you don’t need to access, use the [`loadModel(named:in:)`](./entity/loadmodel%28named,in%29.md) or the [`loadBodyTracked(named:in:)`](./entity/loadbodytracked%28named,in%29.md) method, respectively. These methods and their siblings flatten the entity hierarchy into a single entity cast either as a [`ModelEntity`](./modelentity.md) or [`BodyTrackedEntity`](./bodytrackedentity.md). A flattened entity can be easier to work with when you don’t need access to the entity’s details.

> **Note**: The load model and body-tracked methods work only for USD files.

## See Also

### Loading an entity from a file
- [Generating procedural textures](../visionOS/generating-procedural-textures-in-visionos.md)
  Display a 3D model that generates procedural textures in a reality view.
- [protocol Resource](./resource.md)
  A shared resource you use to configure a component, like a material, mesh, or texture.
- [Stored entities](./stored-entities.md)
  Manage entities that you store as assets on disk.
- [Creating USD files for Apple devices](../USD/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [convenience init(contentsOf: URL, withName: String?) async throws](./entity/init%28contentsof,withname%29.md)
  Creates an entity by asynchronously loading it from a file URL.
- [convenience init(named: String, in: Bundle?) async throws](./entity/init%28named,in%29.md)
  Creates an entity by asynchronously loading it from a bundle.
- [struct ReferenceComponent](./referencecomponent.md)
  A component that can load another entity from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loading-entities-from-a-file)*