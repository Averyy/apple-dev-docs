# init(from:named:contentType:)

**Framework**: RealityKit  
**Kind**: init

Creates an entity by asynchronously loading it from the in-memory contents of a file stored in a Data object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from data: Data, named name: String? = nil, contentType: UTType) async throws
```

#### Return Value

The root entity of the loaded file.

#### Discussion

RealityKit supports loading entities from USD (`.usd`, `.usda`, `.usdc`, `.usdz`) and Reality (`.reality`) files. This method attempts to load the data based on the content type specified instead of automatically determining it.

For more information on loading entities, see [`Loading entities from a file`](loading-entities-from-a-file.md).

See [`init(named:in:)`](entity/init(named:in:).md) for an example of optimally loading content.

## Parameters

- `data`: The Data object containing the in-memory contents of the file to load.
- `contentType`: The content type of the file to load. This can be any of the aforementioned file types, expressed as a UTType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/init(from:named:contenttype:))*