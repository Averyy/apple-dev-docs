# MLCTensorDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create a tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCTensorDescriptor
```

```objc
@interface MLCTensorDescriptor : NSObject
```

#### Overview

This class contains the mathematical properties of a tensor, such as data type and shape. It also includes initializers that help you create a tensor descriptor for common use cases, such as convolutional neural networks and recurrent neural networks.

## Topics

### Creating Tensor Descriptors
- [convenience init?(shape: [Int], dataType: MLCDataType)](./mlctensordescriptor/init%28shape,datatype%29.md)
  Creates a tensor descriptor with the shape and data type you specify.
- [convenience init?(shape: [Int], sequenceLengths: [Int], sortedSequences: Bool, dataType: MLCDataType)](./mlctensordescriptor/init%28shape,sequencelengths,sortedsequences,datatype%29.md)
  Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)](./mlctensordescriptor/init%28width,height,featurechannelcount,batchsize%29.md)
  Creates a tensor descriptor with the width and height, number of feature channels, and batch size you specify.
- [convenience init?(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, dataType: MLCDataType)](./mlctensordescriptor/init%28width,height,featurechannelcount,batchsize,datatype%29.md)
  Creates a tensor descriptor with the width and height, number of feature channels, batch size, and data type you specify.
- [convenience init?(convolutionWeightsWithInputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](./mlctensordescriptor/init%28convolutionweightswithinputfeaturechannelcount,outputfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [convenience init?(convolutionWeightsWithWidth: Int, height: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, dataType: MLCDataType)](./mlctensordescriptor/init%28convolutionweightswithwidth,height,inputfeaturechannelcount,outputfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the sizing, number of feature channels, and data type you specify.
- [convenience init?(convolutionBiasesWithFeatureChannelCount: Int, dataType: MLCDataType)](./mlctensordescriptor/init%28convolutionbiaseswithfeaturechannelcount,datatype%29.md)
  Creates a tensor descriptor with the number of feature channels and data type you specify.
- [class var maxTensorDimensions: Int](./mlctensordescriptor/maxtensordimensions.md)
  The maximum number of tensor dimensions.
- [+ descriptorWithShape:dataType:](./mlctensordescriptor/descriptorwithshape_datatype_.md)
  Creates a tensor descriptor with the shape and data type you specify.
- [+ descriptorWithShape:sequenceLengths:sortedSequences:dataType:](./mlctensordescriptor/descriptorwithshape_sequencelengths_sortedsequences_datatype_.md)
  Creates a tensor descriptor with the shape, variable sequence lengths, sorting indicator, and data type you specify.
### Inspecting Tensor Descriptors
- [var dataType: MLCDataType](./mlctensordescriptor/datatype.md)
  The tensor data type.
- [var dimensionCount: Int](./mlctensordescriptor/dimensioncount.md)
  The number of dimensions in the tensor.
- [var shape: [Int]](./mlctensordescriptor/shape-7i1rw.md)
  An array that contains the size in each dimension.
- [var stride: [Int]](./mlctensordescriptor/stride-5mzlt.md)
  An array that contains the stride, in bytes, in each dimension.
- [var tensorAllocationSizeInBytes: Int](./mlctensordescriptor/tensorallocationsizeinbytes.md)
  The allocation size, in bytes, for a tensor.
- [var sequenceLengths: [Int]?](./mlctensordescriptor/sequencelengths-3jdab.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [var sortedSequences: Bool](./mlctensordescriptor/sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.
- [var batchSizePerSequenceStep: [Int]?](./mlctensordescriptor/batchsizepersequencestep-6iz59.md)
  The batch size for each sequence.
- [shape](./mlctensordescriptor/shape-91vng.md)
  An array that contains the size in each dimension.
- [stride](./mlctensordescriptor/stride-3ydik.md)
  An array that contains the stride, in bytes, in each dimension.
- [sequenceLengths](./mlctensordescriptor/sequencelengths-3ntsa.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [batchSizePerSequenceStep](./mlctensordescriptor/batchsizepersequencestep-55mp8.md)
  The batch size for each sequence.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Tensors with Descriptors
- [convenience init(descriptor: MLCTensorDescriptor)](./mlctensor/init%28descriptor%29.md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](./mlctensor/init%28descriptor,data%29.md)
  Creates a tensor with the descriptor and data you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](./mlctensor/init%28descriptor,fillwithdata%29.md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](./mlctensor/init%28descriptor,randominitializertype%29.md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [enum MLCDataType](./mlcdatatype.md)
  A tensor data type.
- [class MLCTensorData](./mlctensordata.md)
  An encapsulation of the memory that tensor data uses.
- [enum MLCRandomInitializerType](./mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor)*