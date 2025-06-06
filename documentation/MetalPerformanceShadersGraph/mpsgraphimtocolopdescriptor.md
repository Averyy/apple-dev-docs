# MPSGraphImToColOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The class that defines the parameters for an image to column or column to image operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphImToColOpDescriptor
```

#### Overview

Use this descriptor with the following [`MPSGraph`](mpsgraph.md) methods:

- [`imToCol(_:descriptor:name:)`](mpsgraph/imtocol(_:descriptor:name:).md)
- [`colToIm(_:outputShape:descriptor:name:)`](mpsgraph/coltoim(_:outputshape:descriptor:name:).md)

## Topics

### Initializers
- [convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, dataLayout: MPSGraphTensorNamedDataLayout)](mpsgraphimtocolopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:dilationrateinx:dilationrateiny:datalayout:).md)
  Creates column to image descriptor with given values for parameters.
- [convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, dataLayout: MPSGraphTensorNamedDataLayout)](mpsgraphimtocolopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:dilationrateinx:dilationrateiny:paddingleft:paddingright:paddingtop:paddingbottom:datalayout:).md)
  Creates an image to column descriptor with given values for parameters.
### Instance Properties
- [var dataLayout: MPSGraphTensorNamedDataLayout](mpsgraphimtocolopdescriptor/datalayout.md)
  The property that defines the layout of source or output  tensor. e.g. `batch x channels x width x height` for `NCHW` layout
- [var dilationRateInX: Int](mpsgraphimtocolopdescriptor/dilationrateinx.md)
  The property that defines the dilation in width dimension.
- [var dilationRateInY: Int](mpsgraphimtocolopdescriptor/dilationrateiny.md)
  The property that defines the dilation in height dimension.
- [var kernelHeight: Int](mpsgraphimtocolopdescriptor/kernelheight.md)
  The property that defines the kernel size  in height dimension.
- [var kernelWidth: Int](mpsgraphimtocolopdescriptor/kernelwidth.md)
  The property that defines the kernel size in width dimension.
- [var paddingBottom: Int](mpsgraphimtocolopdescriptor/paddingbottom.md)
  The property that defines the padding in height dimension at the bottom.
- [var paddingLeft: Int](mpsgraphimtocolopdescriptor/paddingleft.md)
  The property that defines the padding in width dimension on the left side.
- [var paddingRight: Int](mpsgraphimtocolopdescriptor/paddingright.md)
  The property that defines the padding in width dimension on the right side.
- [var paddingTop: Int](mpsgraphimtocolopdescriptor/paddingtop.md)
  The property that defines the padding in height dimension at the top.
- [var strideInX: Int](mpsgraphimtocolopdescriptor/strideinx.md)
  The property that defines the stride in width dimension.
- [var strideInY: Int](mpsgraphimtocolopdescriptor/strideiny.md)
  The property that defines the stride in height dimension.
### Instance Methods
- [func setExplicitPaddingWithPaddingLeft(Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int)](mpsgraphimtocolopdescriptor/setexplicitpaddingwithpaddingleft(_:paddingright:paddingtop:paddingbottom:).md)
  Sets the descriptor’s padding to the given values.

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
- [class MPSGraphLSTMDescriptor](mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphimtocolopdescriptor)*