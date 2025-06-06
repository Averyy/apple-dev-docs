# MPSGraphLSTMDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The class that defines the parameters for a long short-term memory (LSTM) operation.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphLSTMDescriptor
```

#### Overview

Use this descriptor with the following [`MPSGraph`](mpsgraph.md) methods:

- [`LSTM(_:recurrentWeight:initState:initCell:descriptor:name:)`](mpsgraph/lstm(_:recurrentweight:initstate:initcell:descriptor:name:).md)
- [`LSTM(_:recurrentWeight:inputWeight:bias:initState:initCell:descriptor:name:)`](mpsgraph/lstm(_:recurrentweight:inputweight:bias:initstate:initcell:descriptor:name:).md)
- [`LSTM(_:recurrentWeight:inputWeight:bias:initState:initCell:mask:peephole:descriptor:name:)`](mpsgraph/lstm(_:recurrentweight:inputweight:bias:initstate:initcell:mask:peephole:descriptor:name:).md)
- [`LSTMGradients(_:recurrentWeight:sourceGradient:zState:cellOutputFwd:descriptor:name:)`](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:descriptor:name:).md)
- [`LSTMGradients(_:recurrentWeight:sourceGradient:zState:cellOutputFwd:inputWeight:bias:initState:initCell:descriptor:name:)`](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:inputweight:bias:initstate:initcell:descriptor:name:).md)
- [`LSTMGradients(_:recurrentWeight:sourceGradient:zState:cellOutputFwd:inputWeight:bias:initState:initCell:mask:descriptor:name:)`](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:inputweight:bias:initstate:initcell:mask:descriptor:name:).md)
- [`LSTMGradients(_:recurrentWeight:sourceGradient:zState:cellOutputFwd:stateGradient:cellGradient:inputWeight:bias:initState:initCell:mask:peephole:descriptor:name:)`](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:stategradient:cellgradient:inputweight:bias:initstate:initcell:mask:peephole:descriptor:name:).md)

## Topics

### Instance Properties
- [var activation: MPSGraphRNNActivation](mpsgraphlstmdescriptor/activation.md)
  A parameter that defines the activation function used with the current cell value of the LSTM operation.
- [var bidirectional: Bool](mpsgraphlstmdescriptor/bidirectional.md)
  A parameter that defines a bidirectional LSTM layer.
- [var cellGateActivation: MPSGraphRNNActivation](mpsgraphlstmdescriptor/cellgateactivation.md)
  A parameter that defines the activation function used with the cell gate of the LSTM operation.
- [var forgetGateActivation: MPSGraphRNNActivation](mpsgraphlstmdescriptor/forgetgateactivation.md)
  A parameter that defines the activation function used with the forget gate of the LSTM operation.
- [var forgetGateLast: Bool](mpsgraphlstmdescriptor/forgetgatelast.md)
  A parameter that controls the internal order of the LSTM gates.
- [var inputGateActivation: MPSGraphRNNActivation](mpsgraphlstmdescriptor/inputgateactivation.md)
  A parameter that defines the activation function used with the input gate of the LSTM operation.
- [var outputGateActivation: MPSGraphRNNActivation](mpsgraphlstmdescriptor/outputgateactivation.md)
  A parameter that defines the activation function used with the output gate of the LSTM operation.
- [var produceCell: Bool](mpsgraphlstmdescriptor/producecell.md)
  A parameter that controls whether or not to return the output cell from the LSTM layer.
- [var reverse: Bool](mpsgraphlstmdescriptor/reverse.md)
  A parameter that defines time direction of the input sequence.
- [var training: Bool](mpsgraphlstmdescriptor/training.md)
  A parameter that enables the LSTM layer to support training.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlstmdescriptor)*