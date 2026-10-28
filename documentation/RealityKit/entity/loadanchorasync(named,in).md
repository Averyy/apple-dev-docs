# loadAnchorAsync(named:in:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Asynchronously loads an anchor entity from a bundle.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0 (renamed: AnchorEntity.init(named:in:))
- iPadOS 13.0+ - Deprecated in 18.0 (renamed: AnchorEntity.init(named:in:))
- Mac Catalyst 13.0+ - Deprecated in 18.0 (renamed: AnchorEntity.init(named:in:))
- macOS 10.15+ - Deprecated in 15.0 (renamed: AnchorEntity.init(named:in:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AnchorEntity.init(named:in:))

## Declaration

```swift
@MainActor
@preconcurrency static func loadAnchorAsync(named name: String, in bundle: Bundle? = nil) -> LoadRequest<AnchorEntity>
```

## Return Value

A resource loader that publishes the root entity in the loaded file as an [`AnchorEntity`](../anchorentity.md).

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use `nil` to search the app’s main bundle.

## See Also

### Loading an anchor entity
- [static func loadAnchor(named: String, in: Bundle?) throws -> AnchorEntity](./loadanchor%28named,in%29.md)
  Synchronously loads an anchor entity from a bundle.
- [static func loadAnchor(contentsOf: URL, withName: String?) throws -> AnchorEntity](./loadanchor%28contentsof,withname%29.md)
  Synchronously loads an anchor entity from a file URL.
- [static func loadAnchorAsync(contentsOf: URL, withName: String?) -> LoadRequest<AnchorEntity>](./loadanchorasync%28contentsof,withname%29.md)
  Asynchronously loads an anchor entity from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadanchorasync(named:in:))*