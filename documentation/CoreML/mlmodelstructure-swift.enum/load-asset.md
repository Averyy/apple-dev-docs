# load(asset:)

**Framework**: Core ML  
**Kind**: method

Load the model structure asynchronously from the model asset.

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
static func load(asset: MLModelAsset) async throws -> MLModelStructure
```

## Parameters

- `asset`: The model asset.

## See Also

- [static func load(contentsOf: URL) async throws -> MLModelStructure](mlmodelstructure-swift.enum/load(contentsof:).md)
  Load the model structure asynchronously given the location of its on-disk representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum/load(asset:))*