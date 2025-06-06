# MPSGraphExecutionDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

A class that consists of all the levers  to synchronize and schedule graph execution.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphExecutionDescriptor
```

## Topics

### Instance Properties
- [var compilationDescriptor: MPSGraphCompilationDescriptor?](mpsgraphexecutiondescriptor/compilationdescriptor.md)
  The compilation descriptor for the graph.
- [var completionHandler: MPSGraphCompletionHandler](mpsgraphexecutiondescriptor/completionhandler.md)
  The handler that graph calls at the completion of the execution.
- [var scheduledHandler: MPSGraphScheduledHandler](mpsgraphexecutiondescriptor/scheduledhandler.md)
  The handler that graph calls when it schedules the execution.
- [var waitUntilCompleted: Bool](mpsgraphexecutiondescriptor/waituntilcompleted.md)
  The flag that blocks the execution call until the entire execution is complete.
### Instance Methods
- [func signal(any MTLSharedEvent, atExecutionEvent: MPSGraphExecutionStage, value: UInt64)](mpsgraphexecutiondescriptor/signal(_:atexecutionevent:value:).md)
  Executable signals these shared events at execution stage and immediately proceeds.
- [func wait(for: any MTLSharedEvent, value: UInt64)](mpsgraphexecutiondescriptor/wait(for:value:).md)
  Executable waits on these shared events before scheduling execution on the HW, this does not include encoding which can still continue.

## Relationships

### Inherits From
- [MPSGraphObject](mpsgraphobject.md)
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
- [class MPSGraphFFTDescriptor](mpsgraphfftdescriptor.md)
  The class that defines the parameters for a fast Fourier transform (FFT) operation.
- [class MPSGraphGRUDescriptor](mpsgraphgrudescriptor.md)
  The class that defines the parameters for a gated recurrent unit (GRU) operation.
- [class MPSGraphImToColOpDescriptor](mpsgraphimtocolopdescriptor.md)
  The class that defines the parameters for an image to column or column to image operation.
- [class MPSGraphLSTMDescriptor](mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutiondescriptor)*