# MPSGraphGRUDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class  
**Role**: Class

The class that defines the parameters for a gated recurrent unit (GRU) operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphGRUDescriptor
```

```objc
@interface MPSGraphGRUDescriptor : MPSGraphObject
```

## Overview

Use this descriptor with the following [`MPSGraph`](./mpsgraph.md) methods:

- [`GRU(_:recurrentWeight:inputWeight:bias:descriptor:name:)`](./mpsgraph/gru%28_,recurrentweight,inputweight,bias,descriptor,name%29.md)
- [`GRU(_:recurrentWeight:inputWeight:bias:initState:descriptor:name:)`](./mpsgraph/gru%28_,recurrentweight,inputweight,bias,initstate,descriptor,name%29.md)
- [`GRU(_:recurrentWeight:inputWeight:bias:initState:mask:secondaryBias:descriptor:name:)`](./mpsgraph/gru%28_,recurrentweight,inputweight,bias,initstate,mask,secondarybias,descriptor,name%29.md)
- [`GRUGradients(_:recurrentWeight:sourceGradient:zState:outputFwd:inputWeight:bias:descriptor:name:)`](./mpsgraph/grugradients%28_,recurrentweight,sourcegradient,zstate,outputfwd,inputweight,bias,descriptor,name%29.md)
- [`GRUGradients(_:recurrentWeight:sourceGradient:zState:outputFwd:inputWeight:bias:initState:descriptor:name:)`](./mpsgraph/grugradients%28_,recurrentweight,sourcegradient,zstate,outputfwd,inputweight,bias,initstate,descriptor,name%29.md)
- [`GRUGradients(_:recurrentWeight:sourceGradient:zState:outputFwd:stateGradient:inputWeight:bias:initState:mask:secondaryBias:descriptor:name:)`](./mpsgraph/grugradients%28_,recurrentweight,sourcegradient,zstate,outputfwd,stategradient,inputweight,bias,initstate,mask,secondarybias,descriptor,name%29.md)

## Topics

### Instance Properties
- [var bidirectional: Bool](./mpsgraphgrudescriptor/bidirectional.md)
  A parameter that defines a bidirectional GRU layer.
- [var flipZ: Bool](./mpsgraphgrudescriptor/flipz.md)
  A parameter that chooses between two variants for the final output computation.
- [var outputGateActivation: MPSGraphRNNActivation](./mpsgraphgrudescriptor/outputgateactivation.md)
  A parameter that defines the activation function to use with the output-gate of the GRU operation.
- [var resetAfter: Bool](./mpsgraphgrudescriptor/resetafter.md)
  A parameter that chooses between two variants for the reset gate computation.
- [var resetGateActivation: MPSGraphRNNActivation](./mpsgraphgrudescriptor/resetgateactivation.md)
  A parameter that defines the activation function to use with the reset-gate of the GRU operation.
- [var resetGateFirst: Bool](./mpsgraphgrudescriptor/resetgatefirst.md)
  A parameter that controls the internal order of the GRU gates.
- [var reverse: Bool](./mpsgraphgrudescriptor/reverse.md)
  A parameter that defines the time direction of the input sequence.
- [var training: Bool](./mpsgraphgrudescriptor/training.md)
  A parameter that enables the GRU layer to support training.
- [var updateGateActivation: MPSGraphRNNActivation](./mpsgraphgrudescriptor/updategateactivation.md)
  A parameter that defines the activation function to use with the update-gate of the GRU operation.
### Type Methods
- [+ descriptor](./mpsgraphgrudescriptor/descriptor.md)
  Creates an GRU descriptor with default values.

## Relationships

### Inherits From
- [MPSGraphObject](./mpsgraphobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class MPSGraph](./mpsgraph.md)
  The optimized representation of a compute graph of operations and tensors.
- [class MPSGraphCompilationDescriptor](./mpsgraphcompilationdescriptor.md)
  A class that consists of all the levers for compiling graphs.
- [class MPSGraphConvolution2DOpDescriptor](./mpsgraphconvolution2dopdescriptor.md)
  A class that describes the properties of a 2D-convolution operator.
- [class MPSGraphConvolution3DOpDescriptor](./mpsgraphconvolution3dopdescriptor.md)
  A class that describes the properties of a 3D-convolution operator.
- [class MPSGraphCreateSparseOpDescriptor](./mpsgraphcreatesparseopdescriptor.md)
  A class that describes the properties of a create sparse operation.
- [class MPSGraphDepthwiseConvolution2DOpDescriptor](./mpsgraphdepthwiseconvolution2dopdescriptor.md)
  A class that defines the parameters for  a 2D-depthwise convolution operation.
- [class MPSGraphDepthwiseConvolution3DOpDescriptor](./mpsgraphdepthwiseconvolution3dopdescriptor.md)
  The class that defines the parameters for a 3D-depthwise convolution operation.
- [class MPSGraphDevice](./mpsgraphdevice.md)
  A class that describes the compute device.
- [class MPSGraphExecutable](./mpsgraphexecutable.md)
  The compiled representation of a compute graph executable.
- [class MPSGraphExecutableExecutionDescriptor](./mpsgraphexecutableexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule executable execution.
- [class MPSGraphExecutableSerializationDescriptor](./mpsgraphexecutableserializationdescriptor.md)
  A class that consists of all the levers  to serialize an executable.
- [class MPSGraphExecutionDescriptor](./mpsgraphexecutiondescriptor.md)
  A class that consists of all the levers  to synchronize and schedule graph execution.
- [class MPSGraphFFTDescriptor](./mpsgraphfftdescriptor.md)
  The class that defines the parameters for a fast Fourier transform (FFT) operation.
- [class MPSGraphImToColOpDescriptor](./mpsgraphimtocolopdescriptor.md)
  The class that defines the parameters for an image to column or column to image operation.
- [class MPSGraphLSTMDescriptor](./mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor)*