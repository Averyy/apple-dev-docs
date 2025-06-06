# MPSGraphConvolution2DOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

A class that describes the properties of a 2D-convolution operator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphConvolution2DOpDescriptor
```

#### Overview

Use an instance of this class is to add a 2D-convolution operator with the desired properties to the graph.

## Topics

### Initializers
- [convenience init?(strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, groups: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)](mpsgraphconvolution2dopdescriptor/init(strideinx:strideiny:dilationrateinx:dilationrateiny:groups:paddingleft:paddingright:paddingtop:paddingbottom:paddingstyle:datalayout:weightslayout:).md)
  Creates a convolution descriptor with given values for parameters.
- [convenience init?(strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, groups: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)](mpsgraphconvolution2dopdescriptor/init(strideinx:strideiny:dilationrateinx:dilationrateiny:groups:paddingstyle:datalayout:weightslayout:).md)
  Creates a convolution descriptor with given values for parameters.
### Instance Properties
- [var dataLayout: MPSGraphTensorNamedDataLayout](mpsgraphconvolution2dopdescriptor/datalayout.md)
  The named layout of data in the source tensor.
- [var dilationRateInX: Int](mpsgraphconvolution2dopdescriptor/dilationrateinx.md)
  The amount by which the weights tensor expands in the `x`-direction.
- [var dilationRateInY: Int](mpsgraphconvolution2dopdescriptor/dilationrateiny.md)
  The amount by which the weights tensor expands in the `y`-direction.
- [var groups: Int](mpsgraphconvolution2dopdescriptor/groups.md)
  The number of partitions of the input and output channels.
- [var paddingBottom: Int](mpsgraphconvolution2dopdescriptor/paddingbottom.md)
  The number of zeros added at the bottom of the source tensor.
- [var paddingLeft: Int](mpsgraphconvolution2dopdescriptor/paddingleft.md)
  The number of zeros added on the left side of the source tensor.
- [var paddingRight: Int](mpsgraphconvolution2dopdescriptor/paddingright.md)
  The number of zeros added on the right side of the source tensor.
- [var paddingStyle: MPSGraphPaddingStyle](mpsgraphconvolution2dopdescriptor/paddingstyle.md)
  The type of padding applied to the source tensor.
- [var paddingTop: Int](mpsgraphconvolution2dopdescriptor/paddingtop.md)
  The number of zeros added at the top of the source tensor.
- [var strideInX: Int](mpsgraphconvolution2dopdescriptor/strideinx.md)
  The scale that maps `x`-coordinate of the destination to `x`-coordinate of the source.
- [var strideInY: Int](mpsgraphconvolution2dopdescriptor/strideiny.md)
  The scale that maps `y`-coordinate of the destination to `y`-coordinate of the source.
- [var weightsLayout: MPSGraphTensorNamedDataLayout](mpsgraphconvolution2dopdescriptor/weightslayout.md)
  The named layout of data in the weights tensor.
### Instance Methods
- [func setExplicitPaddingWithPaddingLeft(Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int)](mpsgraphconvolution2dopdescriptor/setexplicitpaddingwithpaddingleft(_:paddingright:paddingtop:paddingbottom:).md)
  Sets the left, right, top, and bottom padding values.

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
- [class MPSGraphConvolution3DOpDescriptor](mpsgraphconvolution3dopdescriptor.md)
  A class that describes the properties of a 3D-convolution operator.
- [class MPSGraphCreateSparseOpDescriptor](mpsgraphcreatesparseopdescriptor.md)
  A class that describes the properties of a create sparse operation.
- [class MPSGraphDepthwiseConvolution2DOpDescriptor](mpsgraphdepthwiseconvolution2dopdescriptor.md)
  A class that defines the parameters for  a 2D-depthwise convolution operation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor)*