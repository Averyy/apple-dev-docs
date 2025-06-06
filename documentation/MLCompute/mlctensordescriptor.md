# MLCTensorDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create a tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCTensorDescriptor
```

#### Overview

This class contains the mathematical properties of a tensor, such as data type and shape. It also includes initializers that help you create a tensor descriptor for common use cases, such as convolutional neural networks and recurrent neural networks.

## Topics

### Creating Tensor Descriptors
- [convenience init?(shape: [Int], dataType: MLCDataType)](mlctensordescriptor/init(shape:datatype:).md)
  Creates a tensor descriptor with the shape and data type you specify.
- [convenience init?(shape: [Int], sequenceLengths: [Int], sortedSequences: Bool, dataType: MLCDataType)](mlctensordescriptor/init(shape:sequencelengths:sortedsequences:datatype:).md)
  Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)](mlctensordescriptor/init(width:height:featurechannelcount:batchsize:).md)
  Creates a tensor descriptor with the width and height, number of feature channels, and batch size you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, dataType: MLCDataType)](mlctensordescriptor/init(width:height:featurechannelcount:batchsize:datatype:).md)
  Creates a tensor descriptor with the width and height, number of feature channels, batch size, and data type you specify.
- [convenience init?(convolutionWeightsWithInputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](mlctensordescriptor/init(convolutionweightswithinputfeaturechannelcount:outputfeaturechannelcount:datatype:).md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [convenience init?(convolutionWeightsWithWidth: Int, height: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](mlctensordescriptor/init(convolutionweightswithwidth:height:inputfeaturechannelcount:outputfeaturechannelcount:datatype:).md)
  Creates a tensor descriptor with the sizing, number of feature channels, and data type you specify.
- [convenience init?(convolutionBiasesWithFeatureChannelCount: Int, dataType: MLCDataType)](mlctensordescriptor/init(convolutionbiaseswithfeaturechannelcount:datatype:).md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [class var maxTensorDimensions: Int](mlctensordescriptor/maxtensordimensions.md)
  The maximum number of tensor dimensions.
### Inspecting Tensor Descriptors
- [var dataType: MLCDataType](mlctensordescriptor/datatype.md)
  The tensor data type.
- [var dimensionCount: Int](mlctensordescriptor/dimensioncount.md)
  The number of dimensions in the tensor.
- [var shape: [Int]](mlctensordescriptor/shape-7i1rw.md)
  An array that contains the size in each dimension.
- [var stride: [Int]](mlctensordescriptor/stride-5mzlt.md)
  An array that contains the stride, in bytes, in each dimension.
- [var tensorAllocationSizeInBytes: Int](mlctensordescriptor/tensorallocationsizeinbytes.md)
  The allocation size, in bytes, for a tensor.
- [var sequenceLengths: [Int]?](mlctensordescriptor/sequencelengths-3jdab.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [var sortedSequences: Bool](mlctensordescriptor/sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.
- [var batchSizePerSequenceStep: [Int]?](mlctensordescriptor/batchsizepersequencestep-6iz59.md)
  The batch size for each sequence.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(descriptor: MLCTensorDescriptor)](mlctensor/init(descriptor:).md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](mlctensor/init(descriptor:data:).md)
  Creates a tensor with the descriptor and data you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](mlctensor/init(descriptor:fillwithdata:).md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(descriptor:randominitializertype:).md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [enum MLCDataType](mlcdatatype.md)
  A tensor data type.
- [class MLCTensorData](mlctensordata.md)
  An encapsulation of the memory that tensor data uses.
- [enum MLCRandomInitializerType](mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor)*