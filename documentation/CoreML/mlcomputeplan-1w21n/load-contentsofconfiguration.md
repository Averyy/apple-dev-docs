# load(contentsOf:configuration:)

**Framework**: Core ML  
**Kind**: method

Construct the compute plan of a model asynchronously given the location of its on-disk representation.

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
static func load(contentsOf url: URL, configuration: MLModelConfiguration) async throws -> MLComputePlan
```

## Parameters

- `url`: The on-disk location of the compiled model (.mlmodelc directory).
- `configuration`: The model configuration.

## See Also

- [static func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLComputePlan](mlcomputeplan-1w21n/load(asset:configuration:).md)
  Construct the compute plan of a model asynchronously given the model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n/load(contentsof:configuration:))*