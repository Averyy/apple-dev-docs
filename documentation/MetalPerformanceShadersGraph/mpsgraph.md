# MPSGraph

**Framework**: Metal Performance Shaders Graph  
**Kind**: class

The optimized representation of a compute graph of operations and tensors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSGraph
```

#### Overview

An MPSGraph is a symbolic representation of operations to be utilized to execute compute graphs on a device.

## Topics

### Initializers
- [init()](mpsgraph/init.md)
  Initialize an MPSGraph to insert nodes in.
### Instance Properties
- [var options: MPSGraphOptions](mpsgraph/options.md)
  Options for the graph.
- [var placeholderTensors: [MPSGraphTensor]](mpsgraph/placeholdertensors.md)
  Array of all the placeholder tensors.
### Instance Methods
- [func GRU(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/gru(_:recurrentweight:inputweight:bias:descriptor:name:).md)
  Creates a GRU operation and returns the value and optionally the training state tensor.
- [func GRU(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/gru(_:recurrentweight:inputweight:bias:initstate:descriptor:name:).md)
  Creates a GRU operation and returns the value and optionally the training state tensor.
- [func GRU(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, secondaryBias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/gru(_:recurrentweight:inputweight:bias:initstate:mask:secondarybias:descriptor:name:).md)
  Creates a GRU operation and returns the value and optionally the training state tensor.
- [func GRUGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, outputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/grugradients(_:recurrentweight:sourcegradient:zstate:outputfwd:inputweight:bias:descriptor:name:).md)
  Creates a GRU gradient operation and returns the gradient tensor values.
- [func GRUGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, outputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/grugradients(_:recurrentweight:sourcegradient:zstate:outputfwd:inputweight:bias:initstate:descriptor:name:).md)
  Creates a GRU gradient operation and returns the gradient tensor values.
- [func GRUGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, outputFwd: MPSGraphTensor, stateGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, secondaryBias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/grugradients(_:recurrentweight:sourcegradient:zstate:outputfwd:stategradient:inputweight:bias:initstate:mask:secondarybias:descriptor:name:).md)
  Creates a GRU gradient operation and returns the gradient tensor values.
- [func HammingDistance(primary: MPSGraphTensor, secondary: MPSGraphTensor, resultDataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/hammingdistance(primary:secondary:resultdatatype:name:).md)
  Computes the hamming distance of two input tensors with support for broadcasting.
- [func HermiteanToRealFFT(MPSGraphTensor, axes: [NSNumber], descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/hermiteantorealfft(_:axes:descriptor:name:).md)
  Creates a Hermitean-to-real fast Fourier transform operation and returns the result tensor.
- [func HermiteanToRealFFT(MPSGraphTensor, axesTensor: MPSGraphTensor, descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/hermiteantorealfft(_:axestensor:descriptor:name:).md)
  Creates a Hermitean-to-real fast Fourier transform operation and returns the result tensor.
- [func L2NormPooling4D(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/l2normpooling4d(_:descriptor:name:).md)
  Creates a 4D L2-norm pooling operation and returns the result tensor.
- [func L2NormPooling4DGradient(MPSGraphTensor, source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/l2normpooling4dgradient(_:source:descriptor:name:).md)
  Creates a L2-Norm pooling gradient operation and returns the result tensor.
- [func LSTM(MPSGraphTensor, recurrentWeight: MPSGraphTensor, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/lstm(_:recurrentweight:initstate:initcell:descriptor:name:).md)
  Creates an LSTM operation and returns the value tensor and optionally the cell state tensor and  the training state tensor.
- [func LSTM(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/lstm(_:recurrentweight:inputweight:bias:initstate:initcell:descriptor:name:).md)
  Creates an LSTM operation and returns the value tensor and optionally the cell state tensor and  the training state tensor.
- [func LSTM(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, mask: MPSGraphTensor?, peephole: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/lstm(_:recurrentweight:inputweight:bias:initstate:initcell:mask:peephole:descriptor:name:).md)
  Creates an LSTM operation and returns the value tensor and optionally the cell state tensor and  the training state tensor.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:descriptor:name:).md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:inputweight:bias:initstate:initcell:descriptor:name:).md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:inputweight:bias:initstate:initcell:mask:descriptor:name:).md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, stateGradient: MPSGraphTensor?, cellGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, mask: MPSGraphTensor?, peephole: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/lstmgradients(_:recurrentweight:sourcegradient:zstate:celloutputfwd:stategradient:cellgradient:inputweight:bias:initstate:initcell:mask:peephole:descriptor:name:).md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func absolute(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/absolute(with:name:).md)
  Returns the absolute values of the input tensor elements.
- [func absoluteSquare(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/absolutesquare(tensor:name:).md)
  Returns the absolute square of the input tensor elements.
- [func acos(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/acos(with:name:).md)
  Applies the inverse cosine operation to the input tensor elements.
- [func acosh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/acosh(with:name:).md)
  Applies the inverse hyperbolic cosine operation to the input tensor elements.
- [func adam(currentLearningRate: MPSGraphTensor, beta1: MPSGraphTensor, beta2: MPSGraphTensor, epsilon: MPSGraphTensor, values: MPSGraphTensor, momentum: MPSGraphTensor, velocity: MPSGraphTensor, maximumVelocity: MPSGraphTensor?, gradient: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/adam(currentlearningrate:beta1:beta2:epsilon:values:momentum:velocity:maximumvelocity:gradient:name:).md)
  Creates operations to apply Adam optimization.
- [func adam(learningRate: MPSGraphTensor, beta1: MPSGraphTensor, beta2: MPSGraphTensor, epsilon: MPSGraphTensor, beta1Power: MPSGraphTensor, beta2Power: MPSGraphTensor, values: MPSGraphTensor, momentum: MPSGraphTensor, velocity: MPSGraphTensor, maximumVelocity: MPSGraphTensor?, gradient: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/adam(learningrate:beta1:beta2:epsilon:beta1power:beta2power:values:momentum:velocity:maximumvelocity:gradient:name:).md)
  Creates operations to apply Adam optimization.
- [func addition(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/addition(_:_:name:).md)
  Adds two input tensors.
- [func applyStochasticGradientDescent(learningRate: MPSGraphTensor, variable: MPSGraphVariableOp, gradient: MPSGraphTensor, name: String?) -> MPSGraphOperation](mpsgraph/applystochasticgradientdescent(learningrate:variable:gradient:name:).md)
  The Stochastic gradient descent performs a gradient descent `variable = variable - (learningRate * g)` where, `g` is gradient of error wrt variable this op directly writes to the variable
- [func argSort(MPSGraphTensor, axis: Int, descending: Bool, name: String?) -> MPSGraphTensor](mpsgraph/argsort(_:axis:descending:name:).md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func argSort(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/argsort(_:axis:name:).md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func argSort(MPSGraphTensor, axisTensor: MPSGraphTensor, descending: Bool, name: String?) -> MPSGraphTensor](mpsgraph/argsort(_:axistensor:descending:name:).md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func argSort(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/argsort(_:axistensor:name:).md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func asin(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/asin(with:name:).md)
  Applies the inverse sine operation to the input tensor elements.
- [func asinh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/asinh(with:name:).md)
  Applies the inverse hyperbolic sine operation to the input tensor elements.
- [func assign(MPSGraphTensor, tensor: MPSGraphTensor, name: String?) -> MPSGraphOperation](mpsgraph/assign(_:tensor:name:).md)
  Creates an assign operation which writes at this point of execution of the graph.
- [func atan(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/atan(with:name:).md)
  Applies the inverse tangent operation to the input tensor elements.
- [func atan2(withPrimaryTensor: MPSGraphTensor, secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/atan2(withprimarytensor:secondarytensor:name:).md)
  Returns the elementwise two-argument arctangent of the input tensors.
- [func atanh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/atanh(with:name:).md)
  Applies the inverse hyperbolic tangent operation to the input tensor elements.
- [func avgPooling2D(withSourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/avgpooling2d(withsourcetensor:descriptor:name:).md)
  Creates a 2D average-pooling operation and returns the result tensor.
- [func avgPooling2DGradient(withGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/avgpooling2dgradient(withgradienttensor:sourcetensor:descriptor:name:).md)
  Creates a 2D average pooling gradient operation and returns the result tensor.
- [func avgPooling4D(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/avgpooling4d(_:descriptor:name:).md)
  Creates a 4D average pooling operation and returns the result tensor.
- [func avgPooling4DGradient(MPSGraphTensor, source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/avgpooling4dgradient(_:source:descriptor:name:).md)
  Creates an average pooling gradient operation and returns the result tensor.
- [func bandPart(MPSGraphTensor, numLower: Int, numUpper: Int, name: String?) -> MPSGraphTensor](mpsgraph/bandpart(_:numlower:numupper:name:).md)
  Computes the band part of an input tensor.
- [func bandPart(MPSGraphTensor, numLowerTensor: MPSGraphTensor, numUpperTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bandpart(_:numlowertensor:numuppertensor:name:).md)
  Creates the band part operation and returns the result.
- [func batchToSpace(MPSGraphTensor, spatialAxes: [NSNumber], batchAxis: Int, blockDimensions: [NSNumber], usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/batchtospace(_:spatialaxes:batchaxis:blockdimensions:usepixelshuffleorder:name:).md)
  Creates a batch-to-space operation and returns the result tensor.
- [func batchToSpace(MPSGraphTensor, spatialAxesTensor: MPSGraphTensor, batchAxisTensor: MPSGraphTensor, blockDimensionsTensor: MPSGraphTensor, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/batchtospace(_:spatialaxestensor:batchaxistensor:blockdimensionstensor:usepixelshuffleorder:name:).md)
  Creates a batch-to-space operation and returns the result tensor.
- [func bitwiseAND(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bitwiseand(_:_:name:).md)
  Returns the elementwise bitwise AND of binary representations of two integer tensors.
- [func bitwiseLeftShift(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bitwiseleftshift(_:_:name:).md)
  Returns the elementwise left-shifted binary representations of the primary integer by the secondary tensor amount.
- [func bitwiseNOT(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bitwisenot(_:name:).md)
  Applies the bitwise NOT operation to the input tensor element.
- [func bitwiseOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bitwiseor(_:_:name:).md)
  Returns the elementwise bitwise OR of binary representations of two integer tensors.
- [func bitwisePopulationCount(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bitwisepopulationcount(_:name:).md)
  Returns the population count of the input tensor elements.
- [func bitwiseRightShift(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bitwiserightshift(_:_:name:).md)
  Returns the elementwise right-shifted binary representations of the primary integer by the secondary tensor amount.
- [func bitwiseXOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bitwisexor(_:_:name:).md)
  Returns the elementwise bitwise XOR of binary representations of two integer tensors.
- [func bottomK(MPSGraphTensor, axis: Int, k: Int, name: String?) -> [MPSGraphTensor]](mpsgraph/bottomk(_:axis:k:name:).md)
  Creates a BottomK operation and returns the value and indices tensors.
- [func bottomK(MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/bottomk(_:axistensor:ktensor:name:).md)
  Creates a BottomK operation and returns the result tensor.
- [func bottomKGradient(MPSGraphTensor, source: MPSGraphTensor, axis: Int, k: Int, name: String?) -> MPSGraphTensor](mpsgraph/bottomkgradient(_:source:axis:k:name:).md)
  Creates a BottomKGradient operation and returns the result tensor.
- [func bottomKGradient(MPSGraphTensor, source: MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/bottomkgradient(_:source:axistensor:ktensor:name:).md)
  Creates a BottomKGradient operation and returns the result tensor.
- [func broadcast(MPSGraphTensor, shape: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/broadcast(_:shape:name:).md)
  Creates a broadcast operation and returns the result tensor.
- [func broadcast(MPSGraphTensor, shapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/broadcast(_:shapetensor:name:).md)
  Creates a broadcast operation and returns the result tensor.
- [func call(symbolName: String, inputTensors: [MPSGraphTensor], outputTypes: [MPSGraphType], name: String?) -> [MPSGraphTensor]](mpsgraph/call(symbolname:inputtensors:outputtypes:name:).md)
  Creates an operation which invokes another executable.
- [func cast(MPSGraphTensor, to: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/cast(_:to:name:).md)
  Creates a cast operation and returns the result tensor.
- [func ceil(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/ceil(with:name:).md)
  Applies the ceiling operation to the input tensor elements.
- [func clamp(MPSGraphTensor, min: MPSGraphTensor, max: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/clamp(_:min:max:name:).md)
  Clamps the values in the first tensor between the corresponding values in the minimum and maximum value tensor.
- [func colToIm(MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphImToColOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/coltoim(_:outputshape:descriptor:name:).md)
  Creates a column to image operation and returns the result tensor.
- [func compile(with: MPSGraphDevice?, feeds: [MPSGraphTensor : MPSGraphShapedType], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, compilationDescriptor: MPSGraphCompilationDescriptor?) -> MPSGraphExecutable](mpsgraph/compile(with:feeds:targettensors:targetoperations:compilationdescriptor:).md)
  Compiles the graph for the given feeds to returns the target tensor values, ensuring all target operations would be executed.
- [func complexConstant(realPart: Double, imaginaryPart: Double) -> MPSGraphTensor](mpsgraph/complexconstant(realpart:imaginarypart:).md)
  Creates a complex constant op with the MPSDataTypeComplexFloat32 data type and returns the result tensor.
- [func complexConstant(realPart: Double, imaginaryPart: Double, dataType: MPSDataType) -> MPSGraphTensor](mpsgraph/complexconstant(realpart:imaginarypart:datatype:).md)
  Creates a complex constant operation and returns the result tensor.
- [func complexConstant(realPart: Double, imaginaryPart: Double, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor](mpsgraph/complexconstant(realpart:imaginarypart:shape:datatype:).md)
  Creates a complex constant op with a given shape and returns the result tensor.
- [func complexTensor(realTensor: MPSGraphTensor, imaginaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/complextensor(realtensor:imaginarytensor:name:).md)
  Returns a complex tensor from the two input tensors.
- [func concatTensor(MPSGraphTensor, with: MPSGraphTensor, dimension: Int, name: String?) -> MPSGraphTensor](mpsgraph/concattensor(_:with:dimension:name:).md)
  Creates a concatenation operation and returns the result tensor.
- [func concatTensors([MPSGraphTensor], dimension: Int, interleave: Bool, name: String?) -> MPSGraphTensor](mpsgraph/concattensors(_:dimension:interleave:name:).md)
  Creates a concatenation operation and returns the result tensor.
- [func concatTensors([MPSGraphTensor], dimension: Int, name: String?) -> MPSGraphTensor](mpsgraph/concattensors(_:dimension:name:).md)
  Creates a concatenation operation and returns the result tensor.
- [func conjugate(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/conjugate(tensor:name:).md)
  Returns the complex conjugate of the input tensor elements.
- [func constant(Double, dataType: MPSDataType) -> MPSGraphTensor](mpsgraph/constant(_:datatype:).md)
  Creates a constant operation and returns the result tensor.
- [func constant(Double, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor](mpsgraph/constant(_:shape:datatype:)-3wa0e.md)
  Creates a constant op with a given shape and returns the result tensor.
- [func constant(Data, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor](mpsgraph/constant(_:shape:datatype:)-ylr4.md)
  Creates a constant op with a given shape and data, and returns the result tensor.
- [func controlDependency(with: [MPSGraphOperation], dependentBlock: MPSGraphControlFlowDependencyBlock, name: String?) -> [MPSGraphTensor]](mpsgraph/controldependency(with:dependentblock:name:).md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func convolution2D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution2d(_:weights:descriptor:name:).md)
  Creates a 2D (forward) convolution operation and returns the result tensor.
- [func convolution2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution2ddatagradient(_:weights:outputshape:forwardconvolutiondescriptor:name:).md)
  Creates a 2D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution2ddatagradient(_:weights:outputshapetensor:forwardconvolutiondescriptor:name:).md)
  Creates a 2D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution2DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution2dweightsgradient(_:source:outputshape:forwardconvolutiondescriptor:name:).md)
  Creates a 2D convolution gradient operation with respect to the weights tensor of the forward convolution.
- [func convolution2DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution2dweightsgradient(_:source:outputshapetensor:forwardconvolutiondescriptor:name:).md)
  Creates a 2D convolution gradient operation with respect to weights tensor of forward convolution.
- [func convolution3D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution3d(_:weights:descriptor:name:).md)
  Creates a 3D forward convolution operation and returns the result tensor.
- [func convolution3DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution3ddatagradient(_:weights:outputshape:forwardconvolutiondescriptor:name:).md)
  Creates a 3D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution3DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution3ddatagradient(_:weights:outputshapetensor:forwardconvolutiondescriptor:name:).md)
  Creates a 3D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution3DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution3dweightsgradient(_:source:outputshape:forwardconvolutiondescriptor:name:).md)
  Creates a 3D convolution gradient operation with respect to the weights tensor of the forward convolution.
- [func convolution3DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolution3dweightsgradient(_:source:outputshapetensor:forwardconvolutiondescriptor:name:).md)
  Creates a 3D convolution gradient operation with respect to the weights tensor of the forward convolution.
- [func convolutionTranspose2D(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolutiontranspose2d(_:weights:outputshape:descriptor:name:).md)
  Creates a convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2D(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolutiontranspose2d(_:weights:outputshapetensor:descriptor:name:).md)
  Creates a convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolutiontranspose2ddatagradient(_:weights:outputshape:forwardconvolutiondescriptor:name:).md)
  Creates a convolution transpose gradient operation with respect to the source tensor of convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolutiontranspose2ddatagradient(_:weights:outputshapetensor:forwardconvolutiondescriptor:name:).md)
  Creates a convolution transpose gradient operation with respect to the source tensor of convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DWeightsGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolutiontranspose2dweightsgradient(_:weights:outputshape:forwardconvolutiondescriptor:name:).md)
  Creates a convolution transpose gradient operation with respect to the weights tensor of the convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DWeightsGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/convolutiontranspose2dweightsgradient(_:weights:outputshapetensor:forwardconvolutiondescriptor:name:).md)
  Creates a convolution transpose gradient operation with respect to the weights tensor of the convolution transpose operation and returns the result tensor.
- [func coordinate(alongAxis: Int, withShape: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/coordinate(alongaxis:withshape:name:).md)
  Creates a get-coordindate operation and returns the result tensor.
- [func coordinate(alongAxis: Int, withShapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/coordinate(alongaxis:withshapetensor:name:).md)
  Creates a get-coordindate operation and returns the result tensor.
- [func coordinate(alongAxisTensor: MPSGraphTensor, withShape: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/coordinate(alongaxistensor:withshape:name:).md)
  Creates a get-coordindate operation and returns the result tensor.
- [func coordinate(alongAxisTensor: MPSGraphTensor, withShapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/coordinate(alongaxistensor:withshapetensor:name:).md)
  Creates a get-coordindate operation and returns the result tensor.
- [func cos(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/cos(with:name:).md)
  Applies the cosine operation to the input tensor elements.
- [func cosh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/cosh(with:name:).md)
  Applies the hyperbolic cosine operation to the input tensor elements.
- [func cumulativeMaximum(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativemaximum(_:axis:exclusive:reverse:name:).md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMaximum(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/cumulativemaximum(_:axis:name:).md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMaximum(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativemaximum(_:axistensor:exclusive:reverse:name:).md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMaximum(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/cumulativemaximum(_:axistensor:name:).md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeminimum(_:axis:exclusive:reverse:name:).md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeminimum(_:axis:name:).md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeminimum(_:axistensor:exclusive:reverse:name:).md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeminimum(_:axistensor:name:).md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeproduct(_:axis:exclusive:reverse:name:).md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeproduct(_:axis:name:).md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeproduct(_:axistensor:exclusive:reverse:name:).md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/cumulativeproduct(_:axistensor:name:).md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativesum(_:axis:exclusive:reverse:name:).md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/cumulativesum(_:axis:name:).md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](mpsgraph/cumulativesum(_:axistensor:exclusive:reverse:name:).md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/cumulativesum(_:axistensor:name:).md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func depth(toSpace2DTensor: MPSGraphTensor, widthAxis: Int, heightAxis: Int, depthAxis: Int, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/depth(tospace2dtensor:widthaxis:heightaxis:depthaxis:blocksize:usepixelshuffleorder:name:).md)
  Creates a depth-to-space2D operation and returns the result tensor.
- [func depth(toSpace2DTensor: MPSGraphTensor, widthAxisTensor: MPSGraphTensor, heightAxisTensor: MPSGraphTensor, depthAxisTensor: MPSGraphTensor, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/depth(tospace2dtensor:widthaxistensor:heightaxistensor:depthaxistensor:blocksize:usepixelshuffleorder:name:).md)
  Creates a depth-to-space2D operation and returns the result tensor.
- [func depthwiseConvolution2D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/depthwiseconvolution2d(_:weights:descriptor:name:).md)
  Creates a 2D-depthwise convolution operation and returns the result tensor.
- [func depthwiseConvolution2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/depthwiseconvolution2ddatagradient(_:weights:outputshape:descriptor:name:).md)
  Creates a 2D-depthwise convolution gradient for data operation and returns the result tensor.
- [func depthwiseConvolution2DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/depthwiseconvolution2dweightsgradient(_:source:outputshape:descriptor:name:).md)
  Creates a 2D-depthwise convolution gradient for weights operation and returns the result tensor.
- [func depthwiseConvolution3D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphDepthwiseConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/depthwiseconvolution3d(_:weights:descriptor:name:).md)
  Creates a 3D depthwise convolution operation and returns the result tensor.
- [func depthwiseConvolution3DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber]?, descriptor: MPSGraphDepthwiseConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/depthwiseconvolution3ddatagradient(_:weights:outputshape:descriptor:name:).md)
  Creates a 3D depthwise convolution gradient for data operation and returns the result tensor.
- [func depthwiseConvolution3DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphDepthwiseConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/depthwiseconvolution3dweightsgradient(_:source:outputshape:descriptor:name:).md)
  Creates a 3D depthwise convolution gradient for weights operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, LUTTensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/dequantize(_:luttensor:axis:name:).md)
  Creates a vector lookup-table based quantization operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, LUTTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/dequantize(_:luttensor:name:).md)
  Creates a lookup-table based quantization operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scale: Double, zeroPoint: Double, dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/dequantize(_:scale:zeropoint:datatype:name:).md)
  Creates Dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/dequantize(_:scaletensor:datatype:name:).md)
  Creates a dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPoint: Double, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/dequantize(_:scaletensor:zeropoint:datatype:axis:name:).md)
  Creates Dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPointTensor: MPSGraphTensor, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/dequantize(_:scaletensor:zeropointtensor:datatype:axis:name:).md)
  Creates a dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPointTensor: MPSGraphTensor, dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/dequantize(_:scaletensor:zeropointtensor:datatype:name:).md)
  Creates a dequantize operation and returns the result tensor.
- [func division(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/division(_:_:name:).md)
  Divides the first input tensor by the second.
- [func divisionNoNaN(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/divisionnonan(_:_:name:).md)
  Divides the first input tensor by the second, with the result being 0 if the denominator is 0.
- [func dropout(MPSGraphTensor, rate: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/dropout(_:rate:name:)-16cq4.md)
  Creates a dropout operation and returns the result
- [func dropout(MPSGraphTensor, rate: Double, name: String?) -> MPSGraphTensor](mpsgraph/dropout(_:rate:name:)-6hvf3.md)
  Creates a dropout operation and returns the result
- [func encode(to: MPSCommandBuffer, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData], executionDescriptor: MPSGraphExecutionDescriptor?)](mpsgraph/encode(to:feeds:targetoperations:resultsdictionary:executiondescriptor:).md)
  Encodes the graph for the given feeds to returns the target tensor values in the results dictionary provided by the user.
- [func encode(to: MPSCommandBuffer, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]](mpsgraph/encode(to:feeds:targettensors:targetoperations:executiondescriptor:).md)
  Encodes the graph for the given feeds to returns the target tensor values, ensuring all target operations also executed.
- [func equal(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/equal(_:_:name:).md)
  Returns the elementwise equality check of the input tensors.
- [func erf(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/erf(with:name:).md)
  Applies the error function to the input tensor elements.
- [func expandDims(MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/expanddims(_:axes:name:).md)
  Creates an expand-dimensions operation and returns the result tensor.
- [func expandDims(MPSGraphTensor, axesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/expanddims(_:axestensor:name:).md)
  Creates an expand-dimensions operation and returns the result tensor.
- [func expandDims(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/expanddims(_:axis:name:).md)
  Creates an expand-dimensions operation and returns the result tensor.
- [func exponent(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/exponent(with:name:).md)
  Applies the natural exponent to the input tensor elements.
- [func exponentBase10(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/exponentbase10(with:name:).md)
  Applies an exponent with base 10 to the input tensor elements.
- [func exponentBase2(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/exponentbase2(with:name:).md)
  Applies an exponent with base 2 to the input tensor elements.
- [func fastFourierTransform(MPSGraphTensor, axes: [NSNumber], descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/fastfouriertransform(_:axes:descriptor:name:).md)
  Creates a fast Fourier transform operation and returns the result tensor.
- [func fastFourierTransform(MPSGraphTensor, axesTensor: MPSGraphTensor, descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/fastfouriertransform(_:axestensor:descriptor:name:).md)
  Creates a fast Fourier transform operation and returns the result tensor.
- [func flatten2D(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/flatten2d(_:axis:name:).md)
  Creates a flatten2D operation and returns the result tensor.
- [func flatten2D(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/flatten2d(_:axistensor:name:).md)
  Creates a flatten2D operation and returns the result tensor.
- [func floor(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/floor(with:name:).md)
  Applies the floor operation to the input tensor elements.
- [func floorModulo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/floormodulo(_:_:name:).md)
  Returns the remainder of floor divison between the primary and secondary tensor.
- [func `for`(lowerBound: MPSGraphTensor, upperBound: MPSGraphTensor, step: MPSGraphTensor, initialBodyArguments: [MPSGraphTensor], body: MPSGraphForLoopBodyBlock, name: String?) -> [MPSGraphTensor]](mpsgraph/for(lowerbound:upperbound:step:initialbodyarguments:body:name:).md)
  Adds a for loop operation, The lower and upper bounds specify a half-open range: the range includes the lower bound but does not include the upper bound.
- [func `for`(numberOfIterations: MPSGraphTensor, initialBodyArguments: [MPSGraphTensor], body: MPSGraphForLoopBodyBlock, name: String?) -> [MPSGraphTensor]](mpsgraph/for(numberofiterations:initialbodyarguments:body:name:).md)
  Adds a for loop operation, with a specific number of iterations.
- [func gather(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, axis: Int, batchDimensions: Int, name: String?) -> MPSGraphTensor](mpsgraph/gather(withupdatestensor:indicestensor:axis:batchdimensions:name:).md)
  Creates a Gather operation and returns the result tensor.
- [func gatherAlongAxis(Int, updates: MPSGraphTensor, indices: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/gatheralongaxis(_:updates:indices:name:).md)
  Creates a GatherAlongAxis operation and returns the result tensor.
- [func gatherAlongAxisTensor(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/gatheralongaxistensor(_:updates:indices:name:).md)
  Creates a GatherAlongAxis operation and returns the result tensor.
- [func gatherND(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, batchDimensions: Int, name: String?) -> MPSGraphTensor](mpsgraph/gathernd(withupdatestensor:indicestensor:batchdimensions:name:).md)
  Creates a GatherND operation and returns the result tensor.
- [func gradients(of: MPSGraphTensor, with: [MPSGraphTensor], name: String?) -> [MPSGraphTensor : MPSGraphTensor]](mpsgraph/gradients(of:with:name:).md)
  Calculates a partial derivative of primaryTensor with respect to the tensors.
- [func greaterThan(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/greaterthan(_:_:name:).md)
  Checks in an elementwise manner if the first input tensor is greater than the second.
- [func greaterThanOrEqualTo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/greaterthanorequalto(_:_:name:).md)
  Checks in an elementwise manner if the first input tensor is greater than or equal to the second.
- [func identity(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/identity(with:name:).md)
  Copies the input tensor values into the output, behaving as an identity operation.
- [func `if`(MPSGraphTensor, then: MPSGraphIfThenElseBlock, else: MPSGraphIfThenElseBlock?, name: String?) -> [MPSGraphTensor]](mpsgraph/if(_:then:else:name:).md)
  Adds an if-then-else operation to the graph.
- [func imToCol(MPSGraphTensor, descriptor: MPSGraphImToColOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/imtocol(_:descriptor:name:).md)
  Creates an imToCol operation and returns the result tensor.
- [func imaginaryPartOfTensor(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/imaginarypartoftensor(tensor:name:).md)
  Returns the imaginary part of a tensor.
- [func inverse(input: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/inverse(input:name:).md)
  Computes the inverse of an input tensor.
- [func isFinite(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/isfinite(with:name:).md)
  Checks if the input tensor elements are finite or not.
- [func isInfinite(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/isinfinite(with:name:).md)
  Checks if the input tensor elements are infinite or not.
- [func isNaN(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/isnan(with:name:).md)
  Checks if the input tensor elements are `NaN` or not.
- [func leakyReLU(with: MPSGraphTensor, alpha: Double, name: String?) -> MPSGraphTensor](mpsgraph/leakyrelu(with:alpha:name:).md)
  Computes the leaky rectified linear unit (ReLU) activation function on the input tensor.
- [func leakyReLU(with: MPSGraphTensor, alphaTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/leakyrelu(with:alphatensor:name:).md)
  Computes the leaky rectified linear unit (ReLU) activation function on the input tensor.
- [func leakyReLUGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, alphaTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/leakyrelugradient(withincominggradient:sourcetensor:alphatensor:name:).md)
  Computes the gradient of the leaky rectified linear unit (ReLU) activation.
- [func lessThan(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/lessthan(_:_:name:).md)
  Checks in an elementwise manner if the first input tensor is less than the second.
- [func lessThanOrEqualTo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/lessthanorequalto(_:_:name:).md)
  Checks in an elementwise manner if the first input tensor is less than or equal to the second.
- [func logarithm(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logarithm(with:name:).md)
  Computes the natural logarithm to the input tensor elements.
- [func logarithmBase10(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logarithmbase10(with:name:).md)
  Computes the logarithm with base 10 to the input tensor elements.
- [func logarithmBase2(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logarithmbase2(with:name:).md)
  Computes the logarithm with base 2 to the input tensor elements.
- [func logicalAND(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logicaland(_:_:name:).md)
  Returns the elementwise logical AND of the input tensors.
- [func logicalNAND(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logicalnand(_:_:name:).md)
  Returns the elementwise logical NAND of the input tensors.
- [func logicalNOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logicalnor(_:_:name:).md)
  Returns the elementwise logical NOR of the input tensors.
- [func logicalOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logicalor(_:_:name:).md)
  Returns the elementwise logical OR of the input tensors.
- [func logicalXNOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logicalxnor(_:_:name:).md)
  Returns the elementwise logical XNOR of the input tensors.
- [func logicalXOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/logicalxor(_:_:name:).md)
  Returns the elementwise logical XOR of the input tensors.
- [func matrixMultiplication(primary: MPSGraphTensor, secondary: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/matrixmultiplication(primary:secondary:name:).md)
  Computes the matrix multiplication of 2 input tensors with support for broadcasting.
- [func maxPooling2D(withSourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling2d(withsourcetensor:descriptor:name:).md)
  Creates a 2D max-pooling operation and returns the result tensor.
- [func maxPooling2DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling2dgradient(withgradienttensor:indicestensor:outputshape:descriptor:name:).md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling2DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling2dgradient(withgradienttensor:indicestensor:outputshapetensor:descriptor:name:).md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling2DGradient(withGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling2dgradient(withgradienttensor:sourcetensor:descriptor:name:).md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling2DReturnIndices(MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/maxpooling2dreturnindices(_:descriptor:name:).md)
  Creates a 2D max-pooling operation and returns the result tensor and the corresponding indices tensor.
- [func maxPooling4D(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling4d(_:descriptor:name:).md)
  Creates a 4D max-pooling operation and returns the result tensor.
- [func maxPooling4DGradient(MPSGraphTensor, source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling4dgradient(_:source:descriptor:name:).md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling4DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling4dgradient(withgradienttensor:indicestensor:outputshape:descriptor:name:).md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling4DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/maxpooling4dgradient(withgradienttensor:indicestensor:outputshapetensor:descriptor:name:).md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling4DReturnIndices(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/maxpooling4dreturnindices(_:descriptor:name:).md)
  Creates a 4D max-pooling operation and returns the result tensor and the corresponding indices tensor.
- [func maximum(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/maximum(_:_:name:).md)
  Returns the elementwise maximum of the input tensors.
- [func maximumWithNaNPropagation(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/maximumwithnanpropagation(_:_:name:).md)
  Returns the elementwise maximum of the input tensors, while propagating `NaN` values.
- [func mean(of: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/mean(of:axes:name:).md)
  Returns the mean of the first input along the specified axes.
- [func minimum(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/minimum(_:_:name:).md)
  Returns the elementwise minimum of the input tensors.
- [func minimumWithNaNPropagation(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/minimumwithnanpropagation(_:_:name:).md)
  Returns the elementwise minimum of the input tensors, while propagating `NaN` values.
- [func modulo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/modulo(_:_:name:).md)
  Returns the remainder obtained by dividing the first input tensor by the second.
- [func multiplication(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/multiplication(_:_:name:).md)
  Multiplies two input tensors.
- [func negative(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/negative(with:name:).md)
  Applies negative to the input tensor elements.
- [func nonMaximumSuppression(withBoxesTensor: MPSGraphTensor, scoresTensor: MPSGraphTensor, classIndicesTensor: MPSGraphTensor, iouThreshold: Float, scoreThreshold: Float, perClassSuppression: Bool, coordinateMode: MPSGraphNonMaximumSuppressionCoordinateMode, name: String?) -> MPSGraphTensor](mpsgraph/nonmaximumsuppression(withboxestensor:scorestensor:classindicestensor:iouthreshold:scorethreshold:perclasssuppression:coordinatemode:name:).md)
  Creates a nonMaximumumSuppression operation and returns the result tensor.
- [func nonMaximumSuppression(withBoxesTensor: MPSGraphTensor, scoresTensor: MPSGraphTensor, iouThreshold: Float, scoreThreshold: Float, perClassSuppression: Bool, coordinateMode: MPSGraphNonMaximumSuppressionCoordinateMode, name: String?) -> MPSGraphTensor](mpsgraph/nonmaximumsuppression(withboxestensor:scorestensor:iouthreshold:scorethreshold:perclasssuppression:coordinatemode:name:).md)
  Creates a nonMaximumumSuppression operation and returns the result tensor.
- [func nonZeroIndices(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/nonzeroindices(_:name:).md)
  Computes the indices of the non-zero elements of the input tensor.
- [func normalizationBetaGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, reductionAxes: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/normalizationbetagradient(withincominggradienttensor:sourcetensor:reductionaxes:name:).md)
  Creates a normalization beta-gradient operation and returns the result tensor.
- [func normalizationGammaGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, mean: MPSGraphTensor, varianceTensor: MPSGraphTensor, reductionAxes: [NSNumber], epsilon: Float, name: String?) -> MPSGraphTensor](mpsgraph/normalizationgammagradient(withincominggradienttensor:sourcetensor:mean:variancetensor:reductionaxes:epsilon:name:).md)
  Creates a normalization gamma-gradient operation and returns the result tensor.
- [func normalizationGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, mean: MPSGraphTensor, varianceTensor: MPSGraphTensor, gammaTensor: MPSGraphTensor?, gammaGradientTensor: MPSGraphTensor?, betaGradientTensor: MPSGraphTensor?, reductionAxes: [NSNumber], epsilon: Float, name: String?) -> MPSGraphTensor](mpsgraph/normalizationgradient(withincominggradienttensor:sourcetensor:mean:variancetensor:gammatensor:gammagradienttensor:betagradienttensor:reductionaxes:epsilon:name:).md)
  Creates a normalization input gradient operation and returns the result tensor.
- [func normalize(MPSGraphTensor, mean: MPSGraphTensor, variance: MPSGraphTensor, gamma: MPSGraphTensor?, beta: MPSGraphTensor?, epsilon: Float, name: String?) -> MPSGraphTensor](mpsgraph/normalize(_:mean:variance:gamma:beta:epsilon:name:).md)
  Creates a batch normalization operation and returns the result tensor.
- [func not(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/not(with:name:).md)
  Applies the logical NOT operation to the input tensor elements.
- [func notEqual(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/notequal(_:_:name:).md)
  Returns the elementwise inequality check of the input tensors.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, axis: Int, dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/onehot(withindicestensor:depth:axis:datatype:name:).md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, axis: Int, dataType: MPSDataType, onValue: Double, offValue: Double, name: String?) -> MPSGraphTensor](mpsgraph/onehot(withindicestensor:depth:axis:datatype:onvalue:offvalue:name:).md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/onehot(withindicestensor:depth:axis:name:).md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/onehot(withindicestensor:depth:datatype:name:).md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, dataType: MPSDataType, onValue: Double, offValue: Double, name: String?) -> MPSGraphTensor](mpsgraph/onehot(withindicestensor:depth:datatype:onvalue:offvalue:name:).md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, name: String?) -> MPSGraphTensor](mpsgraph/onehot(withindicestensor:depth:name:).md)
  Creates a oneHot operation and returns the result tensor.
- [func padGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, paddingMode: MPSGraphPaddingMode, leftPadding: [NSNumber], rightPadding: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/padgradient(withincominggradienttensor:sourcetensor:paddingmode:leftpadding:rightpadding:name:).md)
  Creates a padding gradient operation and returns the result tensor.
- [func padTensor(MPSGraphTensor, with: MPSGraphPaddingMode, leftPadding: [NSNumber], rightPadding: [NSNumber], constantValue: Double, name: String?) -> MPSGraphTensor](mpsgraph/padtensor(_:with:leftpadding:rightpadding:constantvalue:name:).md)
  Creates a padding operation and returns the result tensor.
- [func placeholder(shape: [NSNumber]?, dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/placeholder(shape:datatype:name:).md)
  Creates a placeholder operation and returns the result tensor.
- [func placeholder(shape: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/placeholder(shape:name:).md)
  Creates a placeholder operation and returns the result tensor with the dataType of the placeholder tensor set to 32 bit float.
- [func power(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/power(_:_:name:).md)
  Returns the elementwise result of raising the first tensor to the power of the second tensor.
- [func quantize(MPSGraphTensor, scale: Double, zeroPoint: Double, dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/quantize(_:scale:zeropoint:datatype:name:).md)
  Creates a Quantize operation and returns the result tensor.
- [func quantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPoint: Double, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/quantize(_:scaletensor:zeropoint:datatype:axis:name:).md)
  Creates a Quantize operation and returns the result tensor.
- [func quantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPointTensor: MPSGraphTensor, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/quantize(_:scaletensor:zeropointtensor:datatype:axis:name:).md)
  Creates a Quantize operation and returns the result tensor.
- [func randomPhiloxStateTensor(withCounterLow: Int, counterHigh: Int, key: Int, name: String?) -> MPSGraphTensor](mpsgraph/randomphiloxstatetensor(withcounterlow:counterhigh:key:name:).md)
  Creates a tensor representing state using the Philox algorithm with given counter and key values.
- [func randomPhiloxStateTensor(withSeed: Int, name: String?) -> MPSGraphTensor](mpsgraph/randomphiloxstatetensor(withseed:name:).md)
  Creates a tensor representing state using the Philox algorithm with given counter and key values.
- [func randomTensor(withShape: [NSNumber], descriptor: MPSGraphRandomOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/randomtensor(withshape:descriptor:name:).md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShape: [NSNumber], descriptor: MPSGraphRandomOpDescriptor, seed: Int, name: String?) -> MPSGraphTensor](mpsgraph/randomtensor(withshape:descriptor:seed:name:).md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShape: [NSNumber], descriptor: MPSGraphRandomOpDescriptor, stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/randomtensor(withshape:descriptor:statetensor:name:).md)
  Creates a Random op of type matching distribution in descriptor, and returns random values and updated state.
- [func randomTensor(withShapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/randomtensor(withshapetensor:descriptor:name:).md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, seed: Int, name: String?) -> MPSGraphTensor](mpsgraph/randomtensor(withshapetensor:descriptor:seed:name:).md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/randomtensor(withshapetensor:descriptor:statetensor:name:).md)
  Creates a Random op of type matching distribution in descriptor, and returns random values and updated state.
- [func randomUniformTensor(withShape: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/randomuniformtensor(withshape:name:).md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShape: [NSNumber], seed: Int, name: String?) -> MPSGraphTensor](mpsgraph/randomuniformtensor(withshape:seed:name:).md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShape: [NSNumber], stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/randomuniformtensor(withshape:statetensor:name:).md)
  Creates a RandomUniform operation and returns random uniform values and updated state
- [func randomUniformTensor(withShapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/randomuniformtensor(withshapetensor:name:).md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShapeTensor: MPSGraphTensor, seed: Int, name: String?) -> MPSGraphTensor](mpsgraph/randomuniformtensor(withshapetensor:seed:name:).md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShapeTensor: MPSGraphTensor, stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/randomuniformtensor(withshapetensor:statetensor:name:).md)
  Creates a RandomUniform operation and returns random uniform values and updated state
- [func reLU(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/relu(with:name:).md)
  Computes the ReLU (rectified linear activation unit) function with the input tensor.
- [func reLUGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/relugradient(withincominggradient:sourcetensor:name:).md)
  Computes the gradient of the ReLU  (rectified linear activation unit) function using the incoming gradient.
- [func read(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/read(_:name:).md)
  Creates a read op which reads at this point of execution of the graph and returns the result tensor.
- [func realPartOfTensor(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/realpartoftensor(tensor:name:).md)
  Returns the real part of a tensor.
- [func realToHermiteanFFT(MPSGraphTensor, axes: [NSNumber], descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/realtohermiteanfft(_:axes:descriptor:name:).md)
  Creates a Real-to-Hermitean fast Fourier transform operation and returns the result tensor.
- [func realToHermiteanFFT(MPSGraphTensor, axesTensor: MPSGraphTensor, descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/realtohermiteanfft(_:axestensor:descriptor:name:).md)
  Creates a Real-to-Hermitean fast Fourier transform operation and returns the result tensor.
- [func reciprocal(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/reciprocal(with:name:).md)
  Applies the reciprocal operation to the input tensor elements.
- [func reciprocalSquareRoot(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/reciprocalsquareroot(_:name:).md)
  Applies the reciprocal square root operation to the input tensor elements.
- [func reductionAnd(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionand(with:axes:name:).md)
  Creates a reduction and operation and returns the result tensor.
- [func reductionAnd(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionand(with:axis:name:).md)
  Creates a reduction and operation and returns the result tensor.
- [func reductionArgMaximum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionargmaximum(with:axis:name:).md)
  Creates a reduction argMax operation and returns the result tensor.
- [func reductionArgMinimum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionargminimum(with:axis:name:).md)
  Creates a reduction argMin operation and returns the result tensor.
- [func reductionMaximum(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionmaximum(with:axes:name:).md)
  Creates a reduction max operation and returns the result tensor.
- [func reductionMaximum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionmaximum(with:axis:name:).md)
  Creates a reduction max operation and returns the result tensor.
- [func reductionMaximumPropagateNaN(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionmaximumpropagatenan(with:axes:name:).md)
  Creates a reduction max propagate NaN operation and returns the result tensor.
- [func reductionMaximumPropagateNaN(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionmaximumpropagatenan(with:axis:name:).md)
  Creates a reduction max propagate NaN operation and returns the result tensor.
- [func reductionMinimum(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionminimum(with:axes:name:).md)
  Creates a reduction min operation and returns the result tensor.
- [func reductionMinimum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionminimum(with:axis:name:).md)
  Creates a reduction minimum operation and returns the result tensor.
- [func reductionMinimumPropagateNaN(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionminimumpropagatenan(with:axes:name:).md)
  Creates a reduction min propagate NaN operation and returns the result tensor.
- [func reductionMinimumPropagateNaN(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionminimumpropagatenan(with:axis:name:).md)
  Creates a reduction min propagate NaN operation and returns the result tensor.
- [func reductionOr(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionor(with:axes:name:).md)
  Creates a reduction or operation and returns the result tensor.
- [func reductionOr(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionor(with:axis:name:).md)
  Creates a reduction or operation and returns the result tensor.
- [func reductionProduct(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionproduct(with:axes:name:).md)
  Creates a reduction product operation and returns the result tensor.
- [func reductionProduct(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionproduct(with:axis:name:).md)
  Creates a reduction product operation and returns the result tensor.
- [func reductionSum(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](mpsgraph/reductionsum(with:axes:name:).md)
  Creates a reduction sum operation and returns the result tensor.
- [func reductionSum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/reductionsum(with:axis:name:).md)
  Creates a reduction sum operation and returns the result tensor.
- [func reinterpretCast(MPSGraphTensor, to: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/reinterpretcast(_:to:name:).md)
  Creates a reinterpret cast operation and returns the result tensor.
- [func reshape(MPSGraphTensor, shape: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/reshape(_:shape:name:).md)
  Creates a reshape operation and returns the result tensor.
- [func reshape(MPSGraphTensor, shapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/reshape(_:shapetensor:name:).md)
  Creates a reshape operation and returns the result tensor.
- [func resize(MPSGraphTensor, size: [NSNumber], mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resize(_:size:mode:centerresult:aligncorners:layout:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resize(_:sizetensor:mode:centerresult:aligncorners:layout:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, name: String?) -> MPSGraphTensor](mpsgraph/resize(_:sizetensor:mode:centerresult:aligncorners:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, mode: MPSGraphResizeMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resize(_:sizetensor:scaleoffsettensor:mode:layout:name:).md)
  Resamples input images to given size using the provided scale and offset. Destination indices are computed using
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, offsetTenor: MPSGraphTensor, mode: MPSGraphResizeMode, name: String?) -> MPSGraphTensor](mpsgraph/resize(_:sizetensor:scaletensor:offsettenor:mode:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resize(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resize(withgradienttensor:input:mode:centerresult:aligncorners:layout:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resize(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor: MPSGraphTensor, mode: MPSGraphResizeMode, name: String?) -> MPSGraphTensor](mpsgraph/resize(withgradienttensor:input:scale:offsettensor:mode:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resize(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, mode: MPSGraphResizeMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resize(withgradienttensor:input:scaleoffsettensor:mode:layout:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizebilinear(_:sizetensor:centerresult:aligncorners:layout:name:).md)
  Resamples input images to given size using bilinear sampling.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, centerResult: Bool, alignCorners: Bool, name: String?) -> MPSGraphTensor](mpsgraph/resizebilinear(_:sizetensor:centerresult:aligncorners:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizebilinear(_:sizetensor:scaleoffsettensor:layout:name:).md)
  Resamples input images to given size using the provided scale and offset and bilinear sampling See above discussion for more details.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, offsetTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/resizebilinear(_:sizetensor:scaletensor:offsettensor:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resizeBilinear(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizebilinear(withgradienttensor:input:centerresult:aligncorners:layout:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeBilinear(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/resizebilinear(withgradienttensor:input:scale:offsettensor:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeBilinear(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizebilinear(withgradienttensor:input:scaleoffsettensor:layout:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizenearest(_:sizetensor:nearestroundingmode:centerresult:aligncorners:layout:name:).md)
  Resamples input images to given size using nearest neighbor sampling.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, centerResult: Bool, alignCorners: Bool, name: String?) -> MPSGraphTensor](mpsgraph/resizenearest(_:sizetensor:nearestroundingmode:centerresult:aligncorners:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizenearest(_:sizetensor:scaleoffsettensor:nearestroundingmode:layout:name:).md)
  Resamples input images to given size using the provided scale and offset and nearest neighbor sampling See above discussion for more details.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, offsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, name: String?) -> MPSGraphTensor](mpsgraph/resizenearest(_:sizetensor:scaletensor:offsettensor:nearestroundingmode:name:).md)
  Creates a Resize operation and returns the result tensor.
- [func resizeNearest(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizenearest(withgradienttensor:input:nearestroundingmode:centerresult:aligncorners:layout:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeNearest(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, name: String?) -> MPSGraphTensor](mpsgraph/resizenearest(withgradienttensor:input:scale:offsettensor:nearestroundingmode:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeNearest(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](mpsgraph/resizenearest(withgradienttensor:input:scaleoffsettensor:nearestroundingmode:layout:name:).md)
  Creates a Resize gradient operation and returns the result tensor.
- [func reverse(MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/reverse(_:axes:name:).md)
  Creates a reverse operation and returns the result tensor.
- [func reverse(MPSGraphTensor, axesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/reverse(_:axestensor:name:).md)
  Creates a reverse operation and returns the result tensor.
- [func reverse(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/reverse(_:name:).md)
  Creates a reverse operation and returns the result tensor.
- [func reverseSquareRoot(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/reversesquareroot(with:name:).md)
  Applies the reverse square root operation to the input tensor elements.
- [func rint(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/rint(with:name:).md)
  Rounds the input tensor elements by rounding to nearest even.
- [func round(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/round(with:name:).md)
  Rounds the input tensor elements.
- [func run(feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?) -> [MPSGraphTensor : MPSGraphTensorData]](mpsgraph/run(feeds:targettensors:targetoperations:).md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func run(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData])](mpsgraph/run(with:feeds:targetoperations:resultsdictionary:).md)
  Runs the graph for the given feeds and returns the target tensor values in the results dictionary provided by the user.
- [func run(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?) -> [MPSGraphTensor : MPSGraphTensorData]](mpsgraph/run(with:feeds:targettensors:targetoperations:).md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func runAsync(feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]](mpsgraph/runasync(feeds:targettensors:targetoperations:executiondescriptor:).md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func runAsync(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData], executionDescriptor: MPSGraphExecutionDescriptor?)](mpsgraph/runasync(with:feeds:targetoperations:resultsdictionary:executiondescriptor:).md)
  Encodes the graph for the given feeds to returns the target tensor values in the results dictionary provided by the user.
- [func runAsync(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]](mpsgraph/runasync(with:feeds:targettensors:targetoperations:executiondescriptor:).md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func sampleGrid(withSourceTensor: MPSGraphTensor, coordinateTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, normalizeCoordinates: Bool, relativeCoordinates: Bool, alignCorners: Bool, paddingMode: MPSGraphPaddingMode, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, constantValue: Double, name: String?) -> MPSGraphTensor](mpsgraph/samplegrid(withsourcetensor:coordinatetensor:layout:normalizecoordinates:relativecoordinates:aligncorners:paddingmode:nearestroundingmode:constantvalue:name:).md)
  Samples a tensor using the coordinates provided, using nearest neighbor sampling with specified rounding mode.
- [func sampleGrid(withSourceTensor: MPSGraphTensor, coordinateTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, normalizeCoordinates: Bool, relativeCoordinates: Bool, alignCorners: Bool, paddingMode: MPSGraphPaddingMode, samplingMode: MPSGraphResizeMode, constantValue: Double, name: String?) -> MPSGraphTensor](mpsgraph/samplegrid(withsourcetensor:coordinatetensor:layout:normalizecoordinates:relativecoordinates:aligncorners:paddingmode:samplingmode:constantvalue:name:).md)
  Samples a tensor using the coordinates provided.
- [func scaledDotProductAttention(query: MPSGraphTensor, key: MPSGraphTensor, value: MPSGraphTensor, mask: MPSGraphTensor?, scale: Float, name: String?) -> MPSGraphTensor](mpsgraph/scaleddotproductattention(query:key:value:mask:scale:name:).md)
  Creates a scaled dot product attention (SDPA) operation and returns the result tensor.
- [func scaledDotProductAttention(query: MPSGraphTensor, key: MPSGraphTensor, value: MPSGraphTensor, scale: Float, name: String?) -> MPSGraphTensor](mpsgraph/scaleddotproductattention(query:key:value:scale:name:).md)
  Creates a scaled dot product attention (SDPA) operation (without a mask) and returns the result tensor.
- [func scatter(MPSGraphTensor, indices: MPSGraphTensor, shape: [NSNumber], axis: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatter(_:indices:shape:axis:mode:name:).md)
  Creates a Scatter operation and returns the result tensor.
- [func scatterAlongAxis(Int, data: MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatteralongaxis(_:data:updates:indices:mode:name:).md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterAlongAxis(Int, updates: MPSGraphTensor, indices: MPSGraphTensor, shape: [NSNumber], mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatteralongaxis(_:updates:indices:shape:mode:name:).md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterAlongAxisTensor(MPSGraphTensor, data: MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatteralongaxistensor(_:data:updates:indices:mode:name:).md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterAlongAxisTensor(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, shape: [NSNumber], mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatteralongaxistensor(_:updates:indices:shape:mode:name:).md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterND(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, shape: [NSNumber], batchDimensions: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatternd(withupdatestensor:indicestensor:shape:batchdimensions:mode:name:).md)
  Creates a ScatterND operation and returns the result tensor.
- [func scatterND(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, shape: [NSNumber], batchDimensions: Int, name: String?) -> MPSGraphTensor](mpsgraph/scatternd(withupdatestensor:indicestensor:shape:batchdimensions:name:).md)
  Creates a ScatterND operation and returns the result tensor.
- [func scatterNDWithData(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, batchDimensions: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatterndwithdata(_:updates:indices:batchdimensions:mode:name:).md)
  Creates a ScatterND operation and returns the result tensor.
- [func scatterWithData(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, axis: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](mpsgraph/scatterwithdata(_:updates:indices:axis:mode:name:).md)
  Creates a Scatter operation and returns the result tensor.
- [func select(predicate: MPSGraphTensor, trueTensor: MPSGraphTensor, falseTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/select(predicate:truetensor:falsetensor:name:).md)
  Selects values from either the true or false predicate tensor, depending on the values in the first input.
- [func shapeOf(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/shapeof(_:name:).md)
  Creates a shape-of operation and returns the result tensor.
- [func sigmoid(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/sigmoid(with:name:).md)
  Computes the sigmoid operation on an input tensor.
- [func sigmoidGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/sigmoidgradient(withincominggradient:sourcetensor:name:).md)
  Computes the gradient of the sigmoid function using the incoming gradient tensor.
- [func sign(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/sign(with:name:).md)
  Returns the sign of the input tensor elements.
- [func signbit(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/signbit(with:name:).md)
  Returns the sign bit of the input tensor elements.
- [func sin(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/sin(with:name:).md)
  Applies the sine operation to the input tensor elements.
- [func singleGateRNN(MPSGraphTensor, recurrentWeight: MPSGraphTensor, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/singlegaternn(_:recurrentweight:initstate:descriptor:name:).md)
  Creates a single-gate RNN operation and returns the value and optionally the training state tensor.
- [func singleGateRNN(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/singlegaternn(_:recurrentweight:inputweight:bias:initstate:descriptor:name:).md)
  Creates a single-gate RNN operation and returns the value and optionally the training state tensor.
- [func singleGateRNN(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/singlegaternn(_:recurrentweight:inputweight:bias:initstate:mask:descriptor:name:).md)
  Creates a single-gate RNN operation and returns the value and optionally the training state tensor.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:initstate:descriptor:name:).md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:inputweight:bias:initstate:descriptor:name:).md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:inputweight:bias:initstate:mask:descriptor:name:).md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, stateGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](mpsgraph/singlegaternngradients(_:recurrentweight:sourcegradient:zstate:stategradient:inputweight:bias:initstate:mask:descriptor:name:).md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func sinh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/sinh(with:name:).md)
  Applies the hyperbolic sine operation to the input tensor elements.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, start: MPSGraphTensor, end: MPSGraphTensor, strideTensor: MPSGraphTensor, startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/slicegradienttensor(_:fwdinshapetensor:start:end:stridetensor:startmask:endmask:squeezemask:name:).md)
  Creates a strided-slice gradient operation and returns the result tensor.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, start: MPSGraphTensor, sizeTensor: MPSGraphTensor, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/slicegradienttensor(_:fwdinshapetensor:start:sizetensor:squeezemask:name:).md)
  Creates a slice gradient operation and returns the result tensor.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/slicegradienttensor(_:fwdinshapetensor:starts:ends:strides:name:).md)
  Creates a strided-slice gradient operation and returns the result tensor.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/slicegradienttensor(_:fwdinshapetensor:starts:ends:strides:startmask:endmask:squeezemask:name:).md)
  Creates a strided-slice gradient operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, dimension: Int, start: Int, length: Int, name: String?) -> MPSGraphTensor](mpsgraph/slicetensor(_:dimension:start:length:name:).md)
  Creates a slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, start: MPSGraphTensor, end: MPSGraphTensor, strideTensor: MPSGraphTensor, startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/slicetensor(_:start:end:stridetensor:startmask:endmask:squeezemask:name:).md)
  Creates a strided-slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, start: MPSGraphTensor, sizeTensor: MPSGraphTensor, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/slicetensor(_:start:sizetensor:squeezemask:name:).md)
  Creates a slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/slicetensor(_:starts:ends:strides:name:).md)
  Creates a strided-slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/slicetensor(_:starts:ends:strides:startmask:endmask:squeezemask:name:).md)
  Creates a strided-slice operation and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/sliceupdatedatatensor(_:update:starts:ends:strides:name:).md)
  Creates a strided-slice update operation with zero masks and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/sliceupdatedatatensor(_:update:starts:ends:strides:startmask:endmask:squeezemask:name:).md)
  Creates a strided-slice update operation and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, startsTensor: MPSGraphTensor, endsTensor: MPSGraphTensor, stridesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/sliceupdatedatatensor(_:update:startstensor:endstensor:stridestensor:name:).md)
  Creates a strided-slice update operation with zero masks and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, startsTensor: MPSGraphTensor, endsTensor: MPSGraphTensor, stridesTensor: MPSGraphTensor, startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](mpsgraph/sliceupdatedatatensor(_:update:startstensor:endstensor:stridestensor:startmask:endmask:squeezemask:name:).md)
  Creates a strided-slice update operation and returns the result tensor.
- [func softMax(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/softmax(with:axis:name:).md)
  Computes the softmax function on the input tensor along the specified axis.
- [func softMaxCrossEntropy(MPSGraphTensor, labels: MPSGraphTensor, axis: Int, reuctionType: MPSGraphLossReductionType, name: String?) -> MPSGraphTensor](mpsgraph/softmaxcrossentropy(_:labels:axis:reuctiontype:name:).md)
  Creates a softmax cross-entropy loss operation and returns the result tensor.
- [func softMaxCrossEntropyGradient(MPSGraphTensor, source: MPSGraphTensor, labels: MPSGraphTensor, axis: Int, reuctionType: MPSGraphLossReductionType, name: String?) -> MPSGraphTensor](mpsgraph/softmaxcrossentropygradient(_:source:labels:axis:reuctiontype:name:).md)
  Creates the gradient of a softmax cross-entropy loss operation and returns the result tensor.
- [func softMaxGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/softmaxgradient(withincominggradient:sourcetensor:axis:name:).md)
  Computes the gradient of the softmax function along the specified axis using the incoming gradient tensor.
- [func sort(MPSGraphTensor, axis: Int, descending: Bool, name: String?) -> MPSGraphTensor](mpsgraph/sort(_:axis:descending:name:).md)
  Sorts the elements of the input tensor along the specified axis.
- [func sort(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/sort(_:axis:name:).md)
  Sorts the elements of the input tensor along the specified axis.
- [func sort(MPSGraphTensor, axisTensor: MPSGraphTensor, descending: Bool, name: String?) -> MPSGraphTensor](mpsgraph/sort(_:axistensor:descending:name:).md)
  Sorts the elements of the input tensor along the specified axis.
- [func sort(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/sort(_:axistensor:name:).md)
  Sorts the elements of the input tensor along the specified axis.
- [func space(toDepth2DTensor: MPSGraphTensor, widthAxis: Int, heightAxis: Int, depthAxis: Int, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/space(todepth2dtensor:widthaxis:heightaxis:depthaxis:blocksize:usepixelshuffleorder:name:).md)
  Creates a space-to-depth2D operation and returns the result tensor.
- [func space(toDepth2DTensor: MPSGraphTensor, widthAxisTensor: MPSGraphTensor, heightAxisTensor: MPSGraphTensor, depthAxisTensor: MPSGraphTensor, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/space(todepth2dtensor:widthaxistensor:heightaxistensor:depthaxistensor:blocksize:usepixelshuffleorder:name:).md)
  Creates a space-to-depth2D operation and returns the result tensor.
- [func spaceToBatch(MPSGraphTensor, spatialAxes: [NSNumber], batchAxis: Int, blockDimensions: [NSNumber], usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/spacetobatch(_:spatialaxes:batchaxis:blockdimensions:usepixelshuffleorder:name:).md)
  Creates a space-to-batch operation and returns the result tensor.
- [func spaceToBatch(MPSGraphTensor, spatialAxesTensor: MPSGraphTensor, batchAxisTensor: MPSGraphTensor, blockDimensionsTensor: MPSGraphTensor, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](mpsgraph/spacetobatch(_:spatialaxestensor:batchaxistensor:blockdimensionstensor:usepixelshuffleorder:name:).md)
  Creates a space-to-batch operation and returns the result tensor.
- [func sparseTensor(sparseTensorWithDescriptor: MPSGraphCreateSparseOpDescriptor, tensors: [MPSGraphTensor], shape: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/sparsetensor(sparsetensorwithdescriptor:tensors:shape:name:).md)
  Creates a sparse tensor representation.
- [func sparseTensor(sparseTensorWithType: MPSGraphSparseStorageType, tensors: [MPSGraphTensor], shape: [NSNumber], dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/sparsetensor(sparsetensorwithtype:tensors:shape:datatype:name:).md)
  Creates a sparse tensor representation.
- [func split(MPSGraphTensor, numSplits: Int, axis: Int, name: String?) -> [MPSGraphTensor]](mpsgraph/split(_:numsplits:axis:name:).md)
  Creates a split operation and returns the result tensor.
- [func split(MPSGraphTensor, splitSizes: [NSNumber], axis: Int, name: String?) -> [MPSGraphTensor]](mpsgraph/split(_:splitsizes:axis:name:).md)
  Creates a split operation and returns the result tensor.
- [func split(MPSGraphTensor, splitSizesTensor: MPSGraphTensor, axis: Int, name: String?) -> [MPSGraphTensor]](mpsgraph/split(_:splitsizestensor:axis:name:).md)
  Creates a split operation and returns the result tensor.
- [func square(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/square(with:name:).md)
  Applies the square operation to the input tensor elements.
- [func squareRoot(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/squareroot(with:name:).md)
  Applies the square root operation to the input tensor elements.
- [func squeeze(MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/squeeze(_:axes:name:).md)
  Creates a squeeze operation and returns the result tensor.
- [func squeeze(MPSGraphTensor, axesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/squeeze(_:axestensor:name:).md)
  Creates a squeeze operation and returns the result tensor.
- [func squeeze(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/squeeze(_:axis:name:).md)
  Creates a squeeze operation and returns the result tensor.
- [func squeeze(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/squeeze(_:name:).md)
  Creates a squeeze operation and returns the result tensor.
- [func stack([MPSGraphTensor], axis: Int, name: String?) -> MPSGraphTensor](mpsgraph/stack(_:axis:name:).md)
  Creates a stack operation and returns the result tensor.
- [func stencil(withSourceTensor: MPSGraphTensor, weightsTensor: MPSGraphTensor, descriptor: MPSGraphStencilOpDescriptor, name: String?) -> MPSGraphTensor](mpsgraph/stencil(withsourcetensor:weightstensor:descriptor:name:).md)
  Creates a stencil operation and returns the result tensor.
- [func stochasticGradientDescent(learningRate: MPSGraphTensor, values: MPSGraphTensor, gradient: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/stochasticgradientdescent(learningrate:values:gradient:name:).md)
  The Stochastic gradient descent performs a gradient descent.
- [func subtraction(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/subtraction(_:_:name:).md)
  Subtracts the second input tensor from the first.
- [func tan(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/tan(with:name:).md)
  Applies the tangent operation to the input tensor elements.
- [func tanh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/tanh(with:name:).md)
  Applies the hyperbolic tangent operation to the input tensor elements.
- [func tileGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, withMultiplier: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/tilegradient(withincominggradienttensor:sourcetensor:withmultiplier:name:).md)
  Creates a tile gradient operation and returns the result tensor.
- [func tileTensor(MPSGraphTensor, withMultiplier: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/tiletensor(_:withmultiplier:name:).md)
  Creates a tile operation and returns the result tensor.
- [func topK(MPSGraphTensor, axis: Int, k: Int, name: String?) -> [MPSGraphTensor]](mpsgraph/topk(_:axis:k:name:).md)
  Creates a TopK operation and returns the value and indices tensors.
- [func topK(MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/topk(_:axistensor:ktensor:name:).md)
  Creates a TopK operation and returns the result tensor.
- [func topK(MPSGraphTensor, k: Int, name: String?) -> [MPSGraphTensor]](mpsgraph/topk(_:k:name:).md)
  Creates a TopK operation and returns the value and indices tensors
- [func topK(MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](mpsgraph/topk(_:ktensor:name:).md)
  Creates a TopK operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, input: MPSGraphTensor, k: Int, name: String?) -> MPSGraphTensor](mpsgraph/topkgradient(_:input:k:name:).md)
  Creates a TopKGradient operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, input: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/topkgradient(_:input:ktensor:name:).md)
  Creates a TopKGradient operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, source: MPSGraphTensor, axis: Int, k: Int, name: String?) -> MPSGraphTensor](mpsgraph/topkgradient(_:source:axis:k:name:).md)
  Creates a TopKGradient operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, source: MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/topkgradient(_:source:axistensor:ktensor:name:).md)
  Creates a TopKGradient operation and returns the result tensor.
- [func transpose(MPSGraphTensor, permutation: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/transpose(_:permutation:name:).md)
  Creates a permutation operation and returns the result tensor.
- [func transposeTensor(MPSGraphTensor, dimension: Int, withDimension: Int, name: String?) -> MPSGraphTensor](mpsgraph/transposetensor(_:dimension:withdimension:name:).md)
  Creates a transpose operation and returns the result tensor.
- [func truncate(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/truncate(_:name:).md)
  Applies the truncate operation to the input tensor elements.
- [func variable(with: Data, shape: [NSNumber], dataType: MPSDataType, name: String?) -> MPSGraphTensor](mpsgraph/variable(with:shape:datatype:name:).md)
  Creates a variable operation and returns the result tensor.
- [func variableFromTensor(MPSGraphTensor, name: String?) -> MPSGraphTensor](mpsgraph/variablefromtensor(_:name:).md)
  Creates a variable from an input tensor.
- [func variance(of: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/variance(of:axes:name:).md)
  Returns the variance of the first input along the specified axes.
- [func variance(of: MPSGraphTensor, mean: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](mpsgraph/variance(of:mean:axes:name:).md)
  Returns the variance of the first input along the specified axes when the mean has been precomputed.
- [func `while`(initialInputs: [MPSGraphTensor], before: MPSGraphWhileBeforeBlock, after: MPSGraphWhileAfterBlock, name: String?) -> [MPSGraphTensor]](mpsgraph/while(initialinputs:before:after:name:).md)
  Adds a while loop operation.
### Type Methods
- [class func new() -> Self](mpsgraph/new.md)
  Creates a new graph to insert nodes in.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph)*