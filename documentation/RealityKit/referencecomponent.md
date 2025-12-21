# ReferenceComponent

**Framework**: RealityKit  
**Kind**: struct

A component that can load another entity from a file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ReferenceComponent
```

#### Overview

You can use a `ReferenceComponent` to load other entities from files in your app’s main bundle. This allows you to load complex scenes incrementally, resulting in more responsive apps. It also enables collaborative workflows so you can split a complex scene into separate pieces that different teams own.

Use a `ReferenceComponent` by adding it to an entity when building up a scene programmatically. Then call [`write(to:)`](entity/write(to:).md) to save the scene to a `.reality` file.

```swift
// Create the root entity.
let root = Entity()

// Create an entity that references another entity file.
let earth = Entity()
earth.setParent(root)

// Add a reference to another entity that loads immediately
// when the root entity loads.
earth.components.set(ReferenceComponent(
    named: "Earth",
    loadingPolicy: .immediate))

// Add a reference to another entity that loads on demand.
let mars = Entity()
mars.name = "mars"
mars.components.set(ReferenceComponent(
    named: "Mars",
    loadingPolicy: .onDemand))

// Write the root entity to a `.reality` file.
try await root.write(to: fileURL)
```

When your app loads the `.reality` file, it can dynamically load referenced entities from files. For references that have a [`ReferenceComponent.LoadingPolicy`](referencecomponent/loadingpolicy-swift.enum.md) of [`ReferenceComponent.LoadingPolicy.onDemand`](referencecomponent/loadingpolicy-swift.enum/ondemand.md), you can use [`loadReference(at:)`](referencecomponent/loadreference(at:)-1en8b.md) to load content on demand.

```swift
if let entity = root.findEntity(named: "mars") {
    try ReferenceComponent.loadReference(at: entity)
}
```

Conversely, use [`releaseReference(at:)`](referencecomponent/releasereference(at:).md) to unload content and free up memory.

## Topics

### Initializers
- [init(named: String, at: String, loadingPolicy: ReferenceComponent.LoadingPolicy)](referencecomponent/init(named:at:loadingpolicy:).md)
  Creates a reference component with a name, loading policy, and bundle path.
- [init(named: String, in: Bundle, loadingPolicy: ReferenceComponent.LoadingPolicy)](referencecomponent/init(named:in:loadingpolicy:).md)
  Creates a reference component with a name, loading policy, and bundle.
- [init(named: String, loadingPolicy: ReferenceComponent.LoadingPolicy)](referencecomponent/init(named:loadingpolicy:).md)
  Creates a reference component with a name and loading policy.
### Instance Properties
- [var loadingPolicy: ReferenceComponent.LoadingPolicy](referencecomponent/loadingpolicy-swift.property.md)
  A policy that defines when a referenced entity loads.
- [var reference: Entity?](referencecomponent/reference.md)
  The root entity of the referenced entity file.
- [var state: ReferenceComponent.ReferenceState](referencecomponent/state.md)
  A variable that indicates the loading state of the referenced entity.
### Type Methods
- [static loadReference(at:)](referencecomponent/loadreference(at:).md)
  Asynchronously loads another entity file that an entity depends on.
- [static func releaseReference(at: Entity) throws](referencecomponent/releasereference(at:).md)
  Releases the reference an entity holds.
### Enumerations
- [ReferenceComponent.LoadingPolicy](referencecomponent/loadingpolicy-swift.enum.md)
  Describes when a referenced entity loads.
- [ReferenceComponent.ReferenceState](referencecomponent/referencestate.md)
  Defines the current loading state of the referenced entity.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [Stored entities](stored-entities.md)
  Manage entities that you store as assets on disk.
- [Creating USD files for Apple devices](../USD/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [convenience init(contentsOf: URL, withName: String?) async throws](entity/init(contentsof:withname:).md)
  Creates an entity by asynchronously loading it from a file URL.
- [convenience init(named: String, in: Bundle?) async throws](entity/init(named:in:).md)
  Creates an entity by asynchronously loading it from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/referencecomponent)*