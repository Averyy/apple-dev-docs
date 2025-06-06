# MPSGraphPooling2DOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The class that defines the parameters for a 2D pooling operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphPooling2DOpDescriptor
```

#### Overview

Use this descriptor with the following methods:

- [`maxPooling2D(withSourceTensor:descriptor:name:)`](mpsgraph/maxpooling2d(withsourcetensor:descriptor:name:).md)
- [`maxPooling2DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling2dreturnindices(_:descriptor:name:).md)
- [`maxPooling2DGradient(withGradientTensor:sourceTensor:descriptor:name:)`](mpsgraph/maxpooling2dgradient(withgradienttensor:sourcetensor:descriptor:name:).md)
- [`maxPooling2DGradient(withGradientTensor:indicesTensor:outputShape:descriptor:name:)`](mpsgraph/maxpooling2dgradient(withgradienttensor:indicestensor:outputshape:descriptor:name:).md)
- [`maxPooling2DGradient(withGradientTensor:indicesTensor:outputShapeTensor:descriptor:name:)`](mpsgraph/maxpooling2dgradient(withgradienttensor:indicestensor:outputshapetensor:descriptor:name:).md)
- [`avgPooling2D(withSourceTensor:descriptor:name:)`](mpsgraph/avgpooling2d(withsourcetensor:descriptor:name:).md)
- [`avgPooling2DGradient(withGradientTensor:sourceTensor:descriptor:name:)`](mpsgraph/avgpooling2dgradient(withgradienttensor:sourcetensor:descriptor:name:).md)

## Topics

### Initializers
- [convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout)](mpsgraphpooling2dopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:dilationrateinx:dilationrateiny:paddingleft:paddingright:paddingtop:paddingbottom:paddingstyle:datalayout:).md)
  Creates a 2D pooling descriptor with given values.
- [convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout)](mpsgraphpooling2dopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:paddingstyle:datalayout:).md)
  Creates a 2D pooling descriptor with given values.
### Instance Properties
- [var ceilMode: Bool](mpsgraphpooling2dopdescriptor/ceilmode.md)
  Affects how the graph computes the output size.
- [var dataLayout: MPSGraphTensorNamedDataLayout](mpsgraphpooling2dopdescriptor/datalayout.md)
  Defines the data layout of the input data in the forward pass. See: [`MPSGraphTensorNamedDataLayout`](mpsgraphtensornameddatalayout.md).
- [var dilationRateInX: Int](mpsgraphpooling2dopdescriptor/dilationrateinx.md)
  Defines the dilation rate for the width dimension.
- [var dilationRateInY: Int](mpsgraphpooling2dopdescriptor/dilationrateiny.md)
  Defines the dilation rate for the height dimension.
- [var includeZeroPadToAverage: Bool](mpsgraphpooling2dopdescriptor/includezeropadtoaverage.md)
  Defines a mode for average pooling, where samples outside the input tensor count as zeroes in the average computation.
- [var kernelHeight: Int](mpsgraphpooling2dopdescriptor/kernelheight.md)
  Defines the pooling window size for the height dimension.
- [var kernelWidth: Int](mpsgraphpooling2dopdescriptor/kernelwidth.md)
  Defines the pooling window size for the width dimension.
- [var paddingBottom: Int](mpsgraphpooling2dopdescriptor/paddingbottom.md)
  Defines the explicit padding value for the height dimension to add after the data.
- [var paddingLeft: Int](mpsgraphpooling2dopdescriptor/paddingleft.md)
  Defines the explicit padding value for the width dimension to add before the data.
- [var paddingRight: Int](mpsgraphpooling2dopdescriptor/paddingright.md)
  Defines the explicit padding value for the width dimension to add after the data.
- [var paddingStyle: MPSGraphPaddingStyle](mpsgraphpooling2dopdescriptor/paddingstyle.md)
  Defines what kind of padding graph applies to the operation.
- [var paddingTop: Int](mpsgraphpooling2dopdescriptor/paddingtop.md)
  Defines the explicit padding value for the height dimension to add before the data.
- [var returnIndicesDataType: MPSDataType](mpsgraphpooling2dopdescriptor/returnindicesdatatype.md)
  Defines the data type for returned indices. Use this in conjunction with [`maxPooling2DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling2dreturnindices(_:descriptor:name:).md) API. Currently MPSGraph supports the following datatypes: `MPSDataTypeInt32`. Default value: `MPSDataTypeInt32`.
- [var returnIndicesMode: MPSGraphPoolingReturnIndicesMode](mpsgraphpooling2dopdescriptor/returnindicesmode.md)
  Defines the mode for returned indices of maximum values within each pooling window. Use this in conjunction with [`maxPooling2DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling2dreturnindices(_:descriptor:name:).md) API. If `returnIndicesMode = MPSGraphPoolingReturnIndicesNone` then only the first result MPSGraph returns from [`maxPooling2DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling2dreturnindices(_:descriptor:name:).md) will be valid and using the second result will assert. Default value: `MPSGraphPoolingReturnIndicesNone`.
- [var strideInX: Int](mpsgraphpooling2dopdescriptor/strideinx.md)
  Defines the stride for the width dimension.
- [var strideInY: Int](mpsgraphpooling2dopdescriptor/strideiny.md)
  Defines the stride for the height dimension.
### Instance Methods
- [func setExplicitPaddingWithPaddingLeft(Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int)](mpsgraphpooling2dopdescriptor/setexplicitpaddingwithpaddingleft(_:paddingright:paddingtop:paddingbottom:).md)
  Sets the explicit padding values and sets padding style to explicit.

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
- [class MPSGraphImToColOpDescriptor](mpsgraphimtocolopdescriptor.md)
  The class that defines the parameters for an image to column or column to image operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling2dopdescriptor)*