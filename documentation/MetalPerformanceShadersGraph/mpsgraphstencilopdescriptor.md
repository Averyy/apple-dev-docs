# MPSGraphStencilOpDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The class that defines the parameters for a stencil operation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphStencilOpDescriptor
```

#### Overview

Use this descriptor with the following [`MPSGraph`](mpsgraph.md) method:

- [`stencil(withSourceTensor:weightsTensor:descriptor:name:)`](mpsgraph/stencil(withsourcetensor:weightstensor:descriptor:name:).md)

## Topics

### Initializers
- [convenience init?(explicitPadding: [NSNumber])](mpsgraphstencilopdescriptor/init(explicitpadding:).md)
  Creates a stencil operation descriptor with default values.
- [convenience init?(offsets: [NSNumber], explicitPadding: [NSNumber])](mpsgraphstencilopdescriptor/init(offsets:explicitpadding:).md)
  Creates a stencil operation descriptor with default values.
- [convenience init?(paddingStyle: MPSGraphPaddingStyle)](mpsgraphstencilopdescriptor/init(paddingstyle:).md)
  Creates a stencil operation descriptor with default values.
- [convenience init?(reductionMode: MPSGraphReductionMode, offsets: [NSNumber], strides: [NSNumber], dilationRates: [NSNumber], explicitPadding: [NSNumber], boundaryMode: MPSGraphPaddingMode, paddingStyle: MPSGraphPaddingStyle, paddingConstant: Float)](mpsgraphstencilopdescriptor/init(reductionmode:offsets:strides:dilationrates:explicitpadding:boundarymode:paddingstyle:paddingconstant:).md)
  Creates a stencil operation descriptor with given values.
### Instance Properties
- [var boundaryMode: MPSGraphPaddingMode](mpsgraphstencilopdescriptor/boundarymode.md)
  The property that determines which values to use for padding the input tensor.
- [var dilationRates: [NSNumber]](mpsgraphstencilopdescriptor/dilationrates.md)
  The property that defines dilation rates for spatial dimensions.
- [var explicitPadding: [NSNumber]](mpsgraphstencilopdescriptor/explicitpadding.md)
  The property that defines padding values for spatial dimensions.
- [var offsets: [NSNumber]](mpsgraphstencilopdescriptor/offsets.md)
  An array of length four that determines from which offset to start reading the input tensor.
- [var paddingConstant: Float](mpsgraphstencilopdescriptor/paddingconstant.md)
  The padding value for `boundaryMode = MPSGraphPaddingModeConstant`.
- [var paddingStyle: MPSGraphPaddingStyle](mpsgraphstencilopdescriptor/paddingstyle.md)
  The property that defines what kind of padding to apply to the stencil operation.
- [var reductionMode: MPSGraphReductionMode](mpsgraphstencilopdescriptor/reductionmode.md)
  The reduction mode to use within the stencil window.
- [var strides: [NSNumber]](mpsgraphstencilopdescriptor/strides.md)
  The property that defines strides for spatial dimensions.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphstencilopdescriptor)*