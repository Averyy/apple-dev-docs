# sparseDescriptor(descriptorWithStorageType:dataType:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a descriptor for a sparse tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func sparseDescriptor(descriptorWithStorageType sparseStorageType: MPSGraphSparseStorageType, dataType: MPSDataType) -> Self?
```

#### Return Value

The descriptor.

## Parameters

- `sparseStorageType`: A sparseStorageType.
- `dataType`: A dataType of the sparse tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcreatesparseopdescriptor/sparsedescriptor(descriptorwithstoragetype:datatype:))*