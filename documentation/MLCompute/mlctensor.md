# MLCTensor

**Framework**: ML Compute  
**Kind**: class

The data object you use throughout the framework.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCTensor
```

#### Overview

Create a tensor with or without data. For example, create a tensor with data for weights used by convolution or mean, variance, beta, and gamma parameters with batch normalization. Create a tensor without data to use as an input tensor when you build a graph.

## Topics

### Creating Tensors with Descriptors
- [convenience init(descriptor: MLCTensorDescriptor)](mlctensor/init(descriptor:).md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](mlctensor/init(descriptor:data:).md)
  Creates a tensor with the descriptor and data you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](mlctensor/init(descriptor:fillwithdata:).md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(descriptor:randominitializertype:).md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [class MLCTensorDescriptor](mlctensordescriptor.md)
  A configuration object you use to create a tensor.
- [enum MLCDataType](mlcdatatype.md)
  A tensor data type.
- [class MLCTensorData](mlctensordata.md)
  An encapsulation of the memory that tensor data uses.
- [enum MLCRandomInitializerType](mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.
### Creating Tensors by Specifying Shape
- [convenience init(shape: [Int])](mlctensor/init(shape:).md)
  Creates a tensor without data, with the shape you specify.
- [convenience init(shape: [Int], dataType: MLCDataType)](mlctensor/init(shape:datatype:).md)
  Creates a tensor without data, with the shape and data type you specify.
- [convenience init(shape: [Int], data: MLCTensorData, dataType: MLCDataType)](mlctensor/init(shape:data:datatype:).md)
  Creates a tensor with the shape, data, and data type you specify.
- [convenience init(shape: [Int], fillWithData: NSNumber, dataType: MLCDataType)](mlctensor/init(shape:fillwithdata:datatype:).md)
  Creates a tensor with the shape, scalar value, and data type you specify.
- [convenience init(shape: [Int], randomInitializerType: MLCRandomInitializerType)](mlctensor/init(shape:randominitializertype:).md)
  Creates a tensor with the shape and random initializer type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int)](mlctensor/init(width:height:featurechannelcount:batchsize:).md)
  Creates a tensor without data, with the sizes and number of feature channels you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData)](mlctensor/init(width:height:featurechannelcount:batchsize:data:).md)
  Creates a tensor with the sizes, number of feature channels, and data you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData, dataType: MLCDataType)](mlctensor/init(width:height:featurechannelcount:batchsize:data:datatype:).md)
  Creates a tensor with the sizes, number of feature channels, data, and data type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, fillWithData: Float, dataType: MLCDataType)](mlctensor/init(width:height:featurechannelcount:batchsize:fillwithdata:datatype:).md)
  Creates a tensor with the sizes and number of feature channels, and filled with the data and type you specify.
- [convenience init(width: Int, height: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(width:height:featurechannelcount:batchsize:randominitializertype:).md)
  Creates a tensor with the sizes, number of feature channels, and random data using the random initializer type you specify.
### Creating Tensors by Specifying Sequence Lengths
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int)](mlctensor/init(sequencelength:featurechannelcount:batchsize:).md)
  Creates a tensor without data, with the sequence length, number of feature channels, and batch size you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](mlctensor/init(sequencelength:featurechannelcount:batchsize:data:).md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and data you specify.
- [convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, data: MLCTensorData?)](mlctensor/init(sequencelengths:sortedsequences:featurechannelcount:batchsize:data:).md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and data you specify.
- [convenience init(sequenceLength: Int, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(sequencelength:featurechannelcount:batchsize:randominitializertype:).md)
  Creates a tensor with the sequence length, number of feature channels, batch size, and random initializer type you specify.
- [convenience init?(sequenceLengths: [Int], sortedSequences: Bool, featureChannelCount: Int, batchSize: Int, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(sequencelengths:sortedsequences:featurechannelcount:batchsize:randominitializertype:).md)
  Creates a tensor with the sequence lengths, sorting indicator, number of feature channels, batch size, and random initializer type you specify.
### Inspecting Tensors
- [var tensorID: Int](mlctensor/tensorid.md)
  A number that uniquely identifies the tensor, which the framework assigns when it creates a tensor.
- [var descriptor: MLCTensorDescriptor](mlctensor/descriptor.md)
  The configuration object you use to create a tensor.
- [var data: Data?](mlctensor/data.md)
  The tensor data.
- [var label: String](mlctensor/label.md)
  A string that identifes this tensor.
- [var device: MLCDevice?](mlctensor/device.md)
  The device associated with this tensor.
- [var optimizerData: [MLCTensorData]](mlctensor/optimizerdata.md)
  An array that contains optimizer buffers you specify when you create a tensor parameter.
- [var optimizerDeviceData: [MLCTensorOptimizerDeviceData]](mlctensor/optimizerdevicedata.md)
  An array that contains the device optimizer buffers you specify.
- [var hasValidNumerics: Bool](mlctensor/hasvalidnumerics.md)
  A Boolean that indicates whether a tensor contains NaN or INF values.
- [class MLCTensorOptimizerDeviceData](mlctensoroptimizerdevicedata.md)
  An encapsulation of the device memory associated with a tensor that an optimizer uses.
### Converting Tensors
- [func quantized(to: MLCDataType, scale: Float, bias: Int) -> MLCTensor?](mlctensor/quantized(to:scale:bias:).md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func quantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](mlctensor/quantized(to:scale:bias:axis:).md)
  Converts a 32-bit floating-point tensor with the scale and bias you specify.
- [func dequantized(to: MLCDataType, scale: MLCTensor, zeroPoint: MLCTensor) -> MLCTensor?](mlctensor/dequantized(to:scale:zeropoint:).md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.
- [func dequantized(to: MLCDataType, scale: MLCTensor, bias: MLCTensor, axis: Int) -> MLCTensor?](mlctensor/dequantized(to:scale:bias:axis:).md)
  Converts a tensor you quantize to a 32-bit floating-point tensor.
### Managing Tensor Data
- [func synchronizeData() -> Bool](mlctensor/synchronizedata.md)
  Synchronizes the data in host memory.
- [func synchronizeOptimizerData() -> Bool](mlctensor/synchronizeoptimizerdata.md)
  Synchronizes the optimizer data in host memory.
- [func copyDataFromDeviceMemory(toBytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool](mlctensor/copydatafromdevicememory(tobytes:length:synchronizewithdevice:).md)
  Copies tensor data from device memory to user-specified memory.
- [func bindAndWriteData(MLCTensorData, to: MLCDevice) -> Bool](mlctensor/bindandwritedata(_:to:).md)
  Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool](mlctensor/bindoptimizerdata(_:devicedata:).md)
  Associates the optimizer and device data buffers you specify to the tensor.

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

- [class MLCPlatform](mlcplatform.md)
  A utility class for setting global properties in the framework.
- [Layers](layers.md)
  Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.
- [Training and Validation](training-and-validation.md)
  Create, train, and validate a graph to produce acceptable prediction results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor)*