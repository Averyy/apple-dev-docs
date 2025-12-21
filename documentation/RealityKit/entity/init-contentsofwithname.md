# init(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: init

Creates an entity by asynchronously loading it from a file URL.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(contentsOf url: URL, withName resourceName: String? = nil) async throws
```

#### Return Value

The root entity of the loaded file.

#### Discussion

RealityKit supports loading entities from USD (`.usd`, `.usda`, `.usdc`, `.usdz`) and Reality (`.reality`) files.

For more information on loading entities, see [`Loading entities from a file`](loading-entities-from-a-file.md).

See [`init(named:in:)`](entity/init(named:in:).md) for an example of optimally loading content.

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.

## See Also

- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [Stored entities](stored-entities.md)
  Manage entities that you store as assets on disk.
- [Creating USD files for Apple devices](../USD/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [convenience init(named: String, in: Bundle?) async throws](entity/init(named:in:).md)
  Creates an entity by asynchronously loading it from a bundle.
- [struct ReferenceComponent](referencecomponent.md)
  A component that can load another entity from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/init(contentsof:withname:))*