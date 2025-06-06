# MPSGraphConvolution3DOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

A class that describes the properties of a 3D-convolution operator.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphConvolution3DOpDescriptor
```

#### Overview

Use an instance of this class is to add a 3D-convolution operator with desired properties to the graph.

## Topics

### Initializers
- [convenience init?(strideInX: Int, strideInY: Int, strideInZ: Int, dilationRateInX: Int, dilationRateInY: Int, dilationRateInZ: Int, groups: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingFront: Int, paddingBack: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)](mpsgraphconvolution3dopdescriptor/init(strideinx:strideiny:strideinz:dilationrateinx:dilationrateiny:dilationrateinz:groups:paddingleft:paddingright:paddingtop:paddingbottom:paddingfront:paddingback:paddingstyle:datalayout:weightslayout:).md)
  Creates a convolution descriptor with given values for parameters.
- [convenience init?(strideInX: Int, strideInY: Int, strideInZ: Int, dilationRateInX: Int, dilationRateInY: Int, dilationRateInZ: Int, groups: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)](mpsgraphconvolution3dopdescriptor/init(strideinx:strideiny:strideinz:dilationrateinx:dilationrateiny:dilationrateinz:groups:paddingstyle:datalayout:weightslayout:).md)
  Creates a convolution descriptor with given values for parameters.
### Instance Properties
- [var dataLayout: MPSGraphTensorNamedDataLayout](mpsgraphconvolution3dopdescriptor/datalayout.md)
  The named layout of data in the source tensor.
- [var dilationRateInX: Int](mpsgraphconvolution3dopdescriptor/dilationrateinx.md)
  The amount by which weights tensor expands in the `x`-direction.
- [var dilationRateInY: Int](mpsgraphconvolution3dopdescriptor/dilationrateiny.md)
  The amount by which weights tensor expands in the `y`-direction.
- [var dilationRateInZ: Int](mpsgraphconvolution3dopdescriptor/dilationrateinz.md)
  The amount by which weights tensor expands in the `z`-direction.
- [var groups: Int](mpsgraphconvolution3dopdescriptor/groups.md)
  The number of partitions of the input and output channels.
- [var paddingBack: Int](mpsgraphconvolution3dopdescriptor/paddingback.md)
  The number of zeros added at the back of the source tensor.
- [var paddingBottom: Int](mpsgraphconvolution3dopdescriptor/paddingbottom.md)
  The number of zeros added at the bottom of the source tensor.
- [var paddingFront: Int](mpsgraphconvolution3dopdescriptor/paddingfront.md)
  The number of zeros added at the front of the source tensor.
- [var paddingLeft: Int](mpsgraphconvolution3dopdescriptor/paddingleft.md)
  The number of zeros added on the left side of the source tensor.
- [var paddingRight: Int](mpsgraphconvolution3dopdescriptor/paddingright.md)
  The number of zeros added on the right side of the source tensor.
- [var paddingStyle: MPSGraphPaddingStyle](mpsgraphconvolution3dopdescriptor/paddingstyle.md)
  The type of padding that is applied to the source tensor.
- [var paddingTop: Int](mpsgraphconvolution3dopdescriptor/paddingtop.md)
  The number of zeros added at the top of the source tensor.
- [var strideInX: Int](mpsgraphconvolution3dopdescriptor/strideinx.md)
  The scale that maps`x`-coordinate of destination to `x`-coordinate of source.
- [var strideInY: Int](mpsgraphconvolution3dopdescriptor/strideiny.md)
  The scale that maps`y`-coordinate of destination to `y`-coordinate of source.
- [var strideInZ: Int](mpsgraphconvolution3dopdescriptor/strideinz.md)
  The scale that maps`z`-coordinate of destination to `z`-coordinate of source.
- [var weightsLayout: MPSGraphTensorNamedDataLayout](mpsgraphconvolution3dopdescriptor/weightslayout.md)
  The named layout of data in the weights tensor.
### Instance Methods
- [func setExplicitPaddingWithPaddingLeft(Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingFront: Int, paddingBack: Int)](mpsgraphconvolution3dopdescriptor/setexplicitpaddingwithpaddingleft(_:paddingright:paddingtop:paddingbottom:paddingfront:paddingback:).md)
  Sets the left, right, top, bottom, front, and back padding values.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor)*