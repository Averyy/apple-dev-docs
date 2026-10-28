# loadAnchorAsync(contentsOf:withName:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Asynchronously loads an anchor entity from a file URL.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0 (renamed: AnchorEntity.init(contentsOf:withName:))
- iPadOS 13.0+ - Deprecated in 18.0 (renamed: AnchorEntity.init(contentsOf:withName:))
- Mac Catalyst 13.0+ - Deprecated in 18.0 (renamed: AnchorEntity.init(contentsOf:withName:))
- macOS 10.15+ - Deprecated in 15.0 (renamed: AnchorEntity.init(contentsOf:withName:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AnchorEntity.init(contentsOf:withName:))

## Declaration

```swift
@MainActor
@preconcurrency static func loadAnchorAsync(contentsOf url: URL, withName resourceName: String? = nil) -> LoadRequest<AnchorEntity>
```

## Return Value

A resource loader that publishes the root entity in the loaded file as an [`AnchorEntity`](../anchorentity.md).

## Parameters

- `url`: A file URL representing the file to load.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.

## See Also

### Loading an anchor entity
- [static func loadAnchor(named: String, in: Bundle?) throws -> AnchorEntity](./loadanchor%28named,in%29.md)
  Synchronously loads an anchor entity from a bundle.
- [static func loadAnchor(contentsOf: URL, withName: String?) throws -> AnchorEntity](./loadanchor%28contentsof,withname%29.md)
  Synchronously loads an anchor entity from a file URL.
- [static func loadAnchorAsync(named: String, in: Bundle?) -> LoadRequest<AnchorEntity>](./loadanchorasync%28named,in%29.md)
  Asynchronously loads an anchor entity from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadanchorasync(contentsof:withname:))*