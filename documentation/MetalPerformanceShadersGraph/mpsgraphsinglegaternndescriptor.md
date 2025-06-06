# MPSGraphSingleGateRNNDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The class that defines the parameters for a single gate RNN operation.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphSingleGateRNNDescriptor
```

#### Overview

Use this descriptor with the following [`MPSGraph`](mpsgraph.md) methods:

- [`singleGateRNN(_:recurrentWeight:initState:descriptor:name:)`](mpsgraph/singlegaternn(_:recurrentweight:initstate:descriptor:name:).md)
- [`singleGateRNN(_:recurrentWeight:inputWeight:bias:initState:descriptor:name:)`](mpsgraph/singlegaternn(_:recurrentweight:inputweight:bias:initstate:descriptor:name:).md)
- [`singleGateRNN(_:recurrentWeight:inputWeight:bias:initState:mask:descriptor:name:)`](mpsgraph/singlegaternn(_:recurrentweight:inputweight:bias:initstate:mask:descriptor:name:).md)
- [`singleGateRNNGradients(_:recurrentWeight:sourceGradient:zState:initState:descriptor:name:)`](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:initstate:descriptor:name:).md)
- [`singleGateRNNGradients(_:recurrentWeight:sourceGradient:zState:inputWeight:bias:initState:descriptor:name:)`](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:inputweight:bias:initstate:descriptor:name:).md)
- [`singleGateRNNGradients(_:recurrentWeight:sourceGradient:zState:inputWeight:bias:initState:mask:descriptor:name:)`](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:inputweight:bias:initstate:mask:descriptor:name:).md)
- [`singleGateRNNGradients(_:recurrentWeight:sourceGradient:zState:stateGradient:inputWeight:bias:initState:mask:descriptor:name:)`](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:stategradient:inputweight:bias:initstate:mask:descriptor:name:).md)

## Topics

### Instance Properties
- [var activation: MPSGraphRNNActivation](mpsgraphsinglegaternndescriptor/activation.md)
  A parameter that defines the activation function to use with the RNN operation.
- [var bidirectional: Bool](mpsgraphsinglegaternndescriptor/bidirectional.md)
  A parameter that defines a bidirectional RNN layer.
- [var reverse: Bool](mpsgraphsinglegaternndescriptor/reverse.md)
  A parameter that defines time direction of the input sequence.
- [var training: Bool](mpsgraphsinglegaternndescriptor/training.md)
  A parameter that makes the RNN layer support training.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsinglegaternndescriptor)*