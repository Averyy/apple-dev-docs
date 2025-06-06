# MPSGraphPooling4DOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The class that defines the parameters for a 4D pooling operation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphPooling4DOpDescriptor
```

#### Overview

Use this descriptor with the following methods:

- [`maxPooling4D(_:descriptor:name:)`](mpsgraph/maxpooling4d(_:descriptor:name:).md)
- [`maxPooling4DReturnIndices(_:descriptor:name:)`](mpsgraph/maxpooling4dreturnindices(_:descriptor:name:).md)
- [`maxPooling4DGradient(_:source:descriptor:name:)`](mpsgraph/maxpooling4dgradient(_:source:descriptor:name:).md)
- [`maxPooling4DGradient(withGradientTensor:indicesTensor:outputShape:descriptor:name:)`](mpsgraph/maxpooling4dgradient(withgradienttensor:indicestensor:outputshape:descriptor:name:).md)
- [`maxPooling4DGradient(withGradientTensor:indicesTensor:outputShapeTensor:descriptor:name:)`](mpsgraph/maxpooling4dgradient(withgradienttensor:indicestensor:outputshapetensor:descriptor:name:).md)
- [`avgPooling4D(_:descriptor:name:)`](mpsgraph/avgpooling4d(_:descriptor:name:).md)
- [`avgPooling4DGradient(_:source:descriptor:name:)`](mpsgraph/avgpooling4dgradient(_:source:descriptor:name:).md)
- [`L2NormPooling4D(_:descriptor:name:)`](mpsgraph/l2normpooling4d(_:descriptor:name:).md)
- [`L2NormPooling4DGradient(_:source:descriptor:name:)`](mpsgraph/l2normpooling4dgradient(_:source:descriptor:name:).md)

## Topics

### Initializers
- [convenience init?(kernelSizes: [NSNumber], paddingStyle: MPSGraphPaddingStyle)](mpsgraphpooling4dopdescriptor/init(kernelsizes:paddingstyle:).md)
  Creates a 4D pooling descriptor with default values.
- [convenience init?(kernelSizes: [NSNumber], strides: [NSNumber], dilationRates: [NSNumber], paddingValues: [NSNumber], paddingStyle: MPSGraphPaddingStyle)](mpsgraphpooling4dopdescriptor/init(kernelsizes:strides:dilationrates:paddingvalues:paddingstyle:).md)
  Creates a 4D pooling descriptor with given values.
### Instance Properties
- [var ceilMode: Bool](mpsgraphpooling4dopdescriptor/ceilmode.md)
  Affects how MPSGraph computes the output size: if set to `YES` then output size is computed by rounding up instead of down when dividing input size by stride.
- [var dilationRates: [NSNumber]](mpsgraphpooling4dopdescriptor/dilationrates.md)
  Defines dilation rates for spatial dimensions. Must be four numbers, one for each spatial dimension, fastest running index last.
- [var includeZeroPadToAverage: Bool](mpsgraphpooling4dopdescriptor/includezeropadtoaverage.md)
  Defines a mode for average pooling, where samples outside the input tensor count as zeroes in the average computation.
- [var kernelSizes: [NSNumber]](mpsgraphpooling4dopdescriptor/kernelsizes.md)
  Defines the pooling window size.
- [var paddingStyle: MPSGraphPaddingStyle](mpsgraphpooling4dopdescriptor/paddingstyle.md)
  Defines what kind of padding graph applies to the operation.
- [var paddingValues: [NSNumber]](mpsgraphpooling4dopdescriptor/paddingvalues.md)
  Defines padding values for spatial dimensions which must be eight numbers, two for each spatial dimension.
- [var returnIndicesDataType: MPSDataType](mpsgraphpooling4dopdescriptor/returnindicesdatatype.md)
  Defines the data type for returned indices.
- [var returnIndicesMode: MPSGraphPoolingReturnIndicesMode](mpsgraphpooling4dopdescriptor/returnindicesmode.md)
  Defines the mode for returned indices of maximum values within each pooling window.
- [var strides: [NSNumber]](mpsgraphpooling4dopdescriptor/strides.md)
  Defines strides for spatial dimensions. Must be four numbers, one for each spatial dimension, fastest running index last.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor)*