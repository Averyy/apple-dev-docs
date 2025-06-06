# MPSGraphDepthwiseConvolution2DOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

A class that defines the parameters for  a 2D-depthwise convolution operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphDepthwiseConvolution2DOpDescriptor
```

#### Overview

An `MPSGraphDepthwiseConvolution2DOpDescriptor` defines constant parameters for 2D-depthwise convolutions. Use this class with [`depthwiseConvolution2D(_:weights:descriptor:name:)`](mpsgraph/depthwiseconvolution2d(_:weights:descriptor:name:).md), [`depthwiseConvolution2DDataGradient(_:weights:outputShape:descriptor:name:)`](mpsgraph/depthwiseconvolution2ddatagradient(_:weights:outputshape:descriptor:name:).md), and [`depthwiseConvolution2DWeightsGradient(_:source:outputShape:descriptor:name:)`](mpsgraph/depthwiseconvolution2dweightsgradient(_:source:outputshape:descriptor:name:).md) methods.

## Topics

### Initializers
- [convenience init?(dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)](mpsgraphdepthwiseconvolution2dopdescriptor/init(datalayout:weightslayout:).md)
  Creates a 2D-depthwise convolution descriptor with given properties and default values.
- [convenience init?(strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)](mpsgraphdepthwiseconvolution2dopdescriptor/init(strideinx:strideiny:dilationrateinx:dilationrateiny:paddingleft:paddingright:paddingtop:paddingbottom:paddingstyle:datalayout:weightslayout:).md)
  Creates a 2D-depthwise convolution descriptor with given values.
### Instance Properties
- [var dataLayout: MPSGraphTensorNamedDataLayout](mpsgraphdepthwiseconvolution2dopdescriptor/datalayout.md)
  The data layout of the input data in the forward pass.
- [var dilationRateInX: Int](mpsgraphdepthwiseconvolution2dopdescriptor/dilationrateinx.md)
  The dilation rate for the x dimension.
- [var dilationRateInY: Int](mpsgraphdepthwiseconvolution2dopdescriptor/dilationrateiny.md)
  The dilation rate for the y dimension.
- [var paddingBottom: Int](mpsgraphdepthwiseconvolution2dopdescriptor/paddingbottom.md)
  The explicit padding value for the y dimension operation adds after the data.
- [var paddingLeft: Int](mpsgraphdepthwiseconvolution2dopdescriptor/paddingleft.md)
  The explicit padding value for the x dimension the operation adds before the data.
- [var paddingRight: Int](mpsgraphdepthwiseconvolution2dopdescriptor/paddingright.md)
  The explicit padding value for the x dimension operation adds after the data.
- [var paddingStyle: MPSGraphPaddingStyle](mpsgraphdepthwiseconvolution2dopdescriptor/paddingstyle.md)
  The padding style for the operation.
- [var paddingTop: Int](mpsgraphdepthwiseconvolution2dopdescriptor/paddingtop.md)
  The explicit padding value for the y dimension operation adds before the data.
- [var strideInX: Int](mpsgraphdepthwiseconvolution2dopdescriptor/strideinx.md)
  The stride for the x dimension.
- [var strideInY: Int](mpsgraphdepthwiseconvolution2dopdescriptor/strideiny.md)
  The stride for the y dimension.
- [var weightsLayout: MPSGraphTensorNamedDataLayout](mpsgraphdepthwiseconvolution2dopdescriptor/weightslayout.md)
  The data layout of the weights.
### Instance Methods
- [func setExplicitPaddingWithPaddingLeft(Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int)](mpsgraphdepthwiseconvolution2dopdescriptor/setexplicitpaddingwithpaddingleft(_:paddingright:paddingtop:paddingbottom:).md)
  Sets the explicit padding values.

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
- [class MPSGraphDepthwiseConvolution3DOpDescriptor](mpsgraphdepthwiseconvolution3dopdescriptor.md)
  The class that defines the parameters for a 3D-depthwise convolution operation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdepthwiseconvolution2dopdescriptor)*