# load(asset:configuration:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Type Method

Construct the compute plan of a model asynchronously given the model asset.

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
static func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLComputePlan
```

## Parameters

- `asset`: The model asset.
- `configuration`: The model configuration.

## See Also

### Loading a compute plan
- [static func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLComputePlan](./load%28contentsof,configuration%29.md)
  Construct the compute plan of a model asynchronously given the location of its on-disk representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n/load(asset:configuration:))*