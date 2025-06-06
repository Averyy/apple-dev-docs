# MPSGraphObject

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The common base class for all Metal Performance Shaders Graph objects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphObject
```

#### Overview

Only the child classes should be used.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSGraph](mpsgraph.md)
- [MPSGraphCompilationDescriptor](mpsgraphcompilationdescriptor.md)
- [MPSGraphConvolution2DOpDescriptor](mpsgraphconvolution2dopdescriptor.md)
- [MPSGraphConvolution3DOpDescriptor](mpsgraphconvolution3dopdescriptor.md)
- [MPSGraphCreateSparseOpDescriptor](mpsgraphcreatesparseopdescriptor.md)
- [MPSGraphDepthwiseConvolution2DOpDescriptor](mpsgraphdepthwiseconvolution2dopdescriptor.md)
- [MPSGraphDepthwiseConvolution3DOpDescriptor](mpsgraphdepthwiseconvolution3dopdescriptor.md)
- [MPSGraphDevice](mpsgraphdevice.md)
- [MPSGraphExecutable](mpsgraphexecutable.md)
- [MPSGraphExecutableExecutionDescriptor](mpsgraphexecutableexecutiondescriptor.md)
- [MPSGraphExecutableSerializationDescriptor](mpsgraphexecutableserializationdescriptor.md)
- [MPSGraphExecutionDescriptor](mpsgraphexecutiondescriptor.md)
- [MPSGraphFFTDescriptor](mpsgraphfftdescriptor.md)
- [MPSGraphGRUDescriptor](mpsgraphgrudescriptor.md)
- [MPSGraphImToColOpDescriptor](mpsgraphimtocolopdescriptor.md)
- [MPSGraphLSTMDescriptor](mpsgraphlstmdescriptor.md)
- [MPSGraphOperation](mpsgraphoperation.md)
- [MPSGraphPooling2DOpDescriptor](mpsgraphpooling2dopdescriptor.md)
- [MPSGraphPooling4DOpDescriptor](mpsgraphpooling4dopdescriptor.md)
- [MPSGraphRandomOpDescriptor](mpsgraphrandomopdescriptor.md)
- [MPSGraphSingleGateRNNDescriptor](mpsgraphsinglegaternndescriptor.md)
- [MPSGraphStencilOpDescriptor](mpsgraphstencilopdescriptor.md)
- [MPSGraphTensor](mpsgraphtensor.md)
- [MPSGraphTensorData](mpsgraphtensordata.md)
- [MPSGraphType](mpsgraphtype.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphobject)*