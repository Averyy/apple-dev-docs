# init(from:named:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an entity by asynchronously loading it from the in-memory contents of a file stored in a Data object.

**Availability**:
- iOS 26.0+ - Deprecated in 27.2
- iPadOS 26.0+ - Deprecated in 27.2
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.2
- tvOS 26.0+ - Deprecated in 27.2
- visionOS 26.0+ - Deprecated in 27.2

> **Deprecated**: Use init(from:contentType:) instead. Specify the content type explicitly using a UTType for more reliable format handling.

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from data: Data, named name: String? = nil) async throws
```

## Return Value

The root entity of the loaded file.

## Discussion

RealityKit supports loading entities from USD (`.usd`, `.usda`, `.usdc`, `.usdz`) and Reality (`.reality`) files. This method automatically determines the file type using the first few bytes of the Data object.

For more information on loading entities, see [Loading entities from a file](../loading-entities-from-a-file.md).

See [`init(named:in:)`](./init%28named,in%29.md) for an example of optimally loading content.

## Parameters

- `data`: The Data object containing the in-memory contents of the file to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/init(from:named:))*