# MPSGraphDepthwiseConvolution3DOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The class that defines the parameters for a 3D-depthwise convolution operation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphDepthwiseConvolution3DOpDescriptor
```

#### Overview

A `MPSGraphDepthwiseConvolution3DOpDescriptor` defines constant parameters for 3D depthwise convolutions. Use this class with [`depthwiseConvolution3D(_:weights:descriptor:name:)`](mpsgraph/depthwiseconvolution3d(_:weights:descriptor:name:).md), [`depthwiseConvolution3DDataGradient(_:weights:outputShape:descriptor:name:)`](mpsgraph/depthwiseconvolution3ddatagradient(_:weights:outputshape:descriptor:name:).md) and [`depthwiseConvolution3DWeightsGradient(_:source:outputShape:descriptor:name:)`](mpsgraph/depthwiseconvolution3dweightsgradient(_:source:outputshape:descriptor:name:).md) methods.

## Topics

### Initializers
- [convenience init?(paddingStyle: MPSGraphPaddingStyle)](mpsgraphdepthwiseconvolution3dopdescriptor/init(paddingstyle:).md)
  Creates a 3D depthwise convolution descriptor with default values.
- [convenience init?(strides: [NSNumber], dilationRates: [NSNumber], paddingValues: [NSNumber], paddingStyle: MPSGraphPaddingStyle)](mpsgraphdepthwiseconvolution3dopdescriptor/init(strides:dilationrates:paddingvalues:paddingstyle:).md)
  Creates a 3D depthwise convolution descriptor with given values.
### Instance Properties
- [var channelDimensionIndex: Int](mpsgraphdepthwiseconvolution3dopdescriptor/channeldimensionindex.md)
  The axis that contains the channels in the input and the weights, within the 4D tile of the last dimensions.
- [var dilationRates: [NSNumber]](mpsgraphdepthwiseconvolution3dopdescriptor/dilationrates.md)
  The dilation rates for spatial dimensions.
- [var paddingStyle: MPSGraphPaddingStyle](mpsgraphdepthwiseconvolution3dopdescriptor/paddingstyle.md)
  The padding style for the operation.
- [var paddingValues: [NSNumber]](mpsgraphdepthwiseconvolution3dopdescriptor/paddingvalues.md)
  The padding values for spatial dimensions.
- [var strides: [NSNumber]](mpsgraphdepthwiseconvolution3dopdescriptor/strides.md)
  The strides for spatial dimensions.

## Relationships

### Inherits From
- [MPSGraphObject](mpsgraphobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSGraph](mpsgraph.md)
  The optimized representation of a compute graph of operations and tensors.
- [class MPSGraphCompilationDescriptor](mpsgraphcompilationdescriptor.md)
  A class that consists of all the levers for compiling graphs.
- [class MPSGraphConvolution2DOpDescriptor](mpsgraphconvolution2dopdescriptor.md)
  A class that describes the properties of a 2D-convolution operator.
- [class MPSGraphConvolution3DOpDescriptor](mpsgraphconvolution3dopdescriptor.md)
  A class that describes the properties of a 3D-convolution operator.
- [class MPSGraphCreateSparseOpDescriptor](mpsgraphcreatesparseopdescriptor.md)
  A class that describes the properties of a create sparse operation.
- [class MPSGraphDepthwiseConvolution2DOpDescriptor](mpsgraphdepthwiseconvolution2dopdescriptor.md)
  A class that defines the parameters for  a 2D-depthwise convolution operation.
- [class MPSGraphDevice](mpsgraphdevice.md)
  A class that describes the compute device.
- [class MPSGraphExecutable](mpsgraphexecutable.md)
  The compiled representation of a compute graph executable.
- [class MPSGraphExecutableExecutionDescriptor](mpsgraphexecutableexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule executable execution.
- [class MPSGraphExecutableSerializationDescriptor](mpsgraphexecutableserializationdescriptor.md)
  A class that consists of all the levers  to serialize an executable.
- [class MPSGraphExecutionDescriptor](mpsgraphexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule graph execution.
- [class MPSGraphFFTDescriptor](mpsgraphfftdescriptor.md)
  The class that defines the parameters for a fast Fourier transform (FFT) operation.
- [class MPSGraphGRUDescriptor](mpsgraphgrudescriptor.md)
  The class that defines the parameters for a gated recurrent unit (GRU) operation.
- [class MPSGraphImToColOpDescriptor](mpsgraphimtocolopdescriptor.md)
  The class that defines the parameters for an image to column or column to image operation.
- [class MPSGraphLSTMDescriptor](mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdepthwiseconvolution3dopdescriptor)*