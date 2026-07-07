# AIModelAsset.Summary

**Framework**: Core AI  
**Kind**: struct

A summary of a model’s structure and statistics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Summary
```

#### Overview

Obtain a summary by calling [`summary(includingStatistics:)`](aimodelasset/summary(includingstatistics:).md). The summary describes the model’s functions, storage types, compute types, and operation distribution.

## Topics

### Inspecting precision information
- [var computeTypes: [String]](aimodelasset/summary/computetypes.md)
  The unique compute type names the model uses.
- [var storageTypes: [AIModelAsset.Summary.StorageType]](aimodelasset/summary/storagetypes.md)
  The unique scalar storage types and their element counts.
### Reviewing operation distribution
- [var operationDistribution: [AIModelAsset.Summary.OperationCount]](aimodelasset/summary/operationdistribution.md)
  The distribution of operations in the model, each with a count.
### Inspecting functions
- [var functions: [AIModelAsset.FunctionDescriptor]](aimodelasset/summary/functions.md)
  The functions in the model’s program.
### Supporting types
- [AIModelAsset.Summary.OperationCount](aimodelasset/summary/operationcount.md)
  A model operation and the number of times it occurs.
- [AIModelAsset.Summary.StorageType](aimodelasset/summary/storagetype.md)
  A scalar storage type and the number of elements that use it.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AIModelAsset.FunctionDescriptor](aimodelasset/functiondescriptor.md)
  A description of a function in the model’s program.
- [AIModelAsset.Metadata](aimodelasset/metadata-swift.struct.md)
  The metadata for a model asset, including author, license, and custom key-value pairs.
- [AIModelAsset.ValueDescriptor](aimodelasset/valuedescriptor.md)
  A description of a function’s input or output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/summary)*