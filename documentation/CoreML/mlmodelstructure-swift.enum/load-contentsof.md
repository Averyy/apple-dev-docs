# load(contentsOf:)

**Framework**: Core ML  
**Kind**: method

Load the model structure asynchronously given the location of its on-disk representation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
static func load(contentsOf url: URL) async throws -> MLModelStructure
```

## Parameters

- `url`: The location of its on-disk representation (.mlmodelc directory).

## See Also

- [static func load(asset: MLModelAsset) async throws -> MLModelStructure](mlmodelstructure-swift.enum/load(asset:).md)
  Load the model structure asynchronously from the model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/load(contentsof:))*