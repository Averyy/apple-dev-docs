# Metal Performance Shaders Graph

**Framework**: Metal Performance Shaders Graph  
**Kind**: module

Build, compile, and execute compute graphs utilizing all the different compute devices on the platform, including GPU, CPU, and Neural Engine.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

#### Overview

Metal Performance Shaders Graph provides high-performance, energy-efficient computation on Apple platforms by leveraging different hardware compute blocks. You can use this framework to generate a symbolic compute graph of operations, where each operation can output a set of tensors used as edges of the graph. The tensors represent multidimensional data that objects like [`MTLBuffer`](https://developer.apple.com/documentation/Metal/MTLBuffer) or [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) can back. After you construct the graph, you can compile it into an executable to optimize for performance and subsequently run the executable on your input data. This framework also provides the ability to serialize the executables and load executables from a serialized `.mpsgraphpackage`.

## Topics

### Essentials
- [Adding Custom Functions to a Shader Graph](adding_custom_functions_to_a_shader_graph.md)
  Run your own graph functions on the GPU by building the function programmatically.
- [Training a Neural Network using MPS Graph](training_a_neural_network_using_mps_graph.md)
  Train a simple neural network digit classifier.
- [Filtering Images with MPSGraph FFT Operations](filtering_images_with_mpsgraph_fft_operations.md)
  Filter an image with MPSGraph fast Fourier transforms using the convolutional theorem.
### Classes
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
- [class MPSGraphLSTMDescriptor](mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.
- [class MPSGraphObject](mpsgraphobject.md)
  The common base class for all Metal Performance Shaders Graph objects.
- [class MPSGraphOperation](mpsgraphoperation.md)
  A symbolic representation of a compute operation.
- [class MPSGraphPooling2DOpDescriptor](mpsgraphpooling2dopdescriptor.md)
  The class that defines the parameters for a 2D pooling operation.
- [class MPSGraphPooling4DOpDescriptor](mpsgraphpooling4dopdescriptor.md)
  The class that defines the parameters for a 4D pooling operation.
- [class MPSGraphRandomOpDescriptor](mpsgraphrandomopdescriptor.md)
  A class that describes the random operation.
- [class MPSGraphShapedType](mpsgraphshapedtype.md)
  The shaped type class for types on tensors with a shape and data type.
- [class MPSGraphSingleGateRNNDescriptor](mpsgraphsinglegaternndescriptor.md)
  The class that defines the parameters for a single gate RNN operation.
- [class MPSGraphStencilOpDescriptor](mpsgraphstencilopdescriptor.md)
  The class that defines the parameters for a stencil operation.
- [class MPSGraphTensor](mpsgraphtensor.md)
  The symbolic representation of a compute data type.
- [class MPSGraphTensorData](mpsgraphtensordata.md)
  The representation of a compute data type.
- [class MPSGraphType](mpsgraphtype.md)
  The base type class for types on tensors.
- [class MPSGraphVariableOp](mpsgraphvariableop.md)
  The class that defines the parameters for a variable.
### Type Aliases
- [typealias MPSGraphCompilationCompletionHandler](mpsgraphcompilationcompletionhandler.md)
  A notification that appears when compilation finishes.
- [typealias MPSGraphCompletionHandler](mpsgraphcompletionhandler.md)
  A notification that appears when graph execution finishes.
- [typealias MPSGraphControlFlowDependencyBlock](mpsgraphcontrolflowdependencyblock.md)
  The scope where all the operations defined in this block get control-dependency operations.
- [typealias MPSGraphExecutableCompletionHandler](mpsgraphexecutablecompletionhandler.md)
  A notification when graph executable execution finishes.
- [typealias MPSGraphExecutableScheduledHandler](mpsgraphexecutablescheduledhandler.md)
  A notification when graph executable execution schedules.
- [typealias MPSGraphForLoopBodyBlock](mpsgraphforloopbodyblock.md)
  A block for the body in the for loop.
- [typealias MPSGraphIfThenElseBlock](mpsgraphifthenelseblock.md)
  A block of operations executed under either the if or else condition.
- [typealias MPSGraphScheduledHandler](mpsgraphscheduledhandler.md)
  A notification that appears when graph execution schedules.
- [typealias MPSGraphWhileAfterBlock](mpsgraphwhileafterblock.md)
  The block that executes after the condition evaluates for each iteration.
- [typealias MPSGraphWhileBeforeBlock](mpsgraphwhilebeforeblock.md)
  The block that executes before the condition evaluates for each iteration.
### Enumerations
- [enum MPSGraphDeploymentPlatform](mpsgraphdeploymentplatform.md)
  The options available to a graph.
- [enum MPSGraphDeviceType](mpsgraphdevicetype.md)
  The device type.
- [enum MPSGraphExecutionStage](mpsgraphexecutionstage.md)
  Execution events that can be used with shared events.
- [enum MPSGraphFFTScalingMode](mpsgraphfftscalingmode.md)
  The scaling modes for Fourier transform operations.
- [enum MPSGraphLossReductionType](mpsgraphlossreductiontype.md)
  The type of the reduction the graph applies in the loss operations.
- [enum MPSGraphNonMaximumSuppressionCoordinateMode](mpsgraphnonmaximumsuppressioncoordinatemode.md)
  The non-maximum suppression coordinate mode.
- [enum MPSGraphOptimization](mpsgraphoptimization.md)
  The optimization levels to trade compilation time for even more runtime performance by running more passes.
- [enum MPSGraphOptimizationProfile](mpsgraphoptimizationprofile.md)
  The optimization profile used as a heuristic as the graph compiler optimizes the network.
- [enum MPSGraphOptions](mpsgraphoptions.md)
  The options available to a graph.
- [enum MPSGraphPaddingMode](mpsgraphpaddingmode.md)
  The tensor padding mode.
- [enum MPSGraphPaddingStyle](mpsgraphpaddingstyle.md)
  The tensor padding style.
- [enum MPSGraphPoolingReturnIndicesMode](mpsgraphpoolingreturnindicesmode.md)
  The flattening mode for returned indices with max-pooling.
- [enum MPSGraphRNNActivation](mpsgraphrnnactivation.md)
  The activation modes for RNN operations.
- [enum MPSGraphRandomDistribution](mpsgraphrandomdistribution.md)
  The distributions supported by random operations.
- [enum MPSGraphRandomNormalSamplingMethod](mpsgraphrandomnormalsamplingmethod.md)
  The sampling method to use when generating values in the normal distribution.
- [enum MPSGraphReductionMode](mpsgraphreductionmode.md)
  The reduction mode.
- [enum MPSGraphResizeMode](mpsgraphresizemode.md)
  The resize mode to use for resizing.
- [enum MPSGraphResizeNearestRoundingMode](mpsgraphresizenearestroundingmode.md)
  The rounding mode to use when using nearest resize mode.
- [enum MPSGraphScatterMode](mpsgraphscattermode.md)
  The scatter mode.
- [enum MPSGraphSparseStorageType](mpsgraphsparsestoragetype.md)
  The sparse storage options in the Metal Performance Shaders Graph framework.
- [enum MPSGraphTensorNamedDataLayout](mpsgraphtensornameddatalayout.md)
  The tensor layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MetalPerformanceShadersGraph)*