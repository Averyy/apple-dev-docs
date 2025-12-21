# MPSGraphCompilationDescriptor

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

A class that consists of all the levers for compiling graphs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraphCompilationDescriptor
```

## Topics

### Instance Properties
- [var callables: [String : MPSGraphExecutable]?](mpsgraphcompilationdescriptor/callables.md)
  The dictionary used during runtime to lookup the [`MPSGraphExecutable`](mpsgraphexecutable.md) which correspond to the `symbolName`.
- [var compilationCompletionHandler: MPSGraphCompilationCompletionHandler](mpsgraphcompilationdescriptor/compilationcompletionhandler.md)
  The handler that the graph calls when the compilation completes.
- [var dispatchQueue: dispatch_queue_t](mpsgraphcompilationdescriptor/dispatchqueue.md)
  The dispatch queue used for the compilation.
- [var optimizationLevel: MPSGraphOptimization](mpsgraphcompilationdescriptor/optimizationlevel.md)
  The optimization level for the graph execution, default is MPSGraphOptimizationLevel1.
- [var optimizationProfile: MPSGraphOptimizationProfile](mpsgraphcompilationdescriptor/optimizationprofile.md)
  The optimization profile for the graph optimization.
- [var reducedPrecisionFastMath: MPSGraphReducedPrecisionFastMath](mpsgraphcompilationdescriptor/reducedprecisionfastmath.md)
  Across the executable allow reduced precision fast math optimizations.
- [var waitForCompilationCompletion: Bool](mpsgraphcompilationdescriptor/waitforcompilationcompletion.md)
  Flag that makes the compile or specialize call blocking till the entire compilation is complete, defaults to NO.
### Instance Methods
- [func disableTypeInference()](mpsgraphcompilationdescriptor/disabletypeinference.md)
  Turns off type inference and relies on type inference during runtime.

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
- [class MPSGraphLSTMDescriptor](mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompilationdescriptor)*