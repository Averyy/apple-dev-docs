# loadAnchorAsync(named:in:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads an anchor entity from a bundle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAnchorAsync(named name: String, in bundle: Bundle? = nil) -> LoadRequest<AnchorEntity>
```

#### Return Value

A resource loader that publishes the root entity in the loaded file as an [`AnchorEntity`](anchorentity.md).

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func loadAnchor(named: String, in: Bundle?) throws -> AnchorEntity](entity/loadanchor(named:in:).md)
  Synchronously loads an anchor entity from a bundle.
- [static func loadAnchor(contentsOf: URL, withName: String?) throws -> AnchorEntity](entity/loadanchor(contentsof:withname:).md)
  Synchronously loads an anchor entity from a file URL.
- [static func loadAnchorAsync(contentsOf: URL, withName: String?) -> LoadRequest<AnchorEntity>](entity/loadanchorasync(contentsof:withname:).md)
  Asynchronously loads an anchor entity from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadanchorasync(named:in:))*