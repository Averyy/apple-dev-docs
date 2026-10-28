# MPSGraph

**Framework**: Metal Performance Shaders Graph  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSGraph : MPSGraphObject
```

## Overview

An MPSGraph is a symbolic representation of operations to be utilized to execute compute graphs on a device.

## Topics

### Initializers
- [init()](./mpsgraph/init%28%29.md)
  Initialize an MPSGraph to insert nodes in.
### Instance Properties
- [var options: MPSGraphOptions](./mpsgraph/options.md)
  Options for the graph.
- [var placeholderTensors: [MPSGraphTensor]](./mpsgraph/placeholdertensors.md)
  Array of all the placeholder tensors.
### Instance Methods
- [func GRU(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/gru%28_,recurrentweight,inputweight,bias,descriptor,name%29.md)
  Creates a GRU operation and returns the value and optionally the training state tensor.
- [func GRU(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/gru%28_,recurrentweight,inputweight,bias,initstate,descriptor,name%29.md)
  Creates a GRU operation and returns the value and optionally the training state tensor.
- [func GRU(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, secondaryBias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/gru%28_,recurrentweight,inputweight,bias,initstate,mask,secondarybias,descriptor,name%29.md)
  Creates a GRU operation and returns the value and optionally the training state tensor.
- [func GRUGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, outputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/grugradients%28_,recurrentweight,sourcegradient,zstate,outputfwd,inputweight,bias,descriptor,name%29.md)
  Creates a GRU gradient operation and returns the gradient tensor values.
- [func GRUGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, outputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/grugradients%28_,recurrentweight,sourcegradient,zstate,outputfwd,inputweight,bias,initstate,descriptor,name%29.md)
  Creates a GRU gradient operation and returns the gradient tensor values.
- [func GRUGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, outputFwd: MPSGraphTensor, stateGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, secondaryBias: MPSGraphTensor?, descriptor: MPSGraphGRUDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/grugradients%28_,recurrentweight,sourcegradient,zstate,outputfwd,stategradient,inputweight,bias,initstate,mask,secondarybias,descriptor,name%29.md)
  Creates a GRU gradient operation and returns the gradient tensor values.
- [func HammingDistance(primary: MPSGraphTensor, secondary: MPSGraphTensor, resultDataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/hammingdistance%28primary,secondary,resultdatatype,name%29.md)
  Computes the hamming distance of two input tensors with support for broadcasting.
- [func HermiteanToRealFFT(MPSGraphTensor, axes: [NSNumber], descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/hermiteantorealfft%28_,axes,descriptor,name%29.md)
  Creates a Hermitean-to-real fast Fourier transform operation and returns the result tensor.
- [func HermiteanToRealFFT(MPSGraphTensor, axesTensor: MPSGraphTensor, descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/hermiteantorealfft%28_,axestensor,descriptor,name%29.md)
  Creates a Hermitean-to-real fast Fourier transform operation and returns the result tensor.
- [func L2NormPooling4D(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/l2normpooling4d%28_,descriptor,name%29.md)
  Creates a 4D L2-norm pooling operation and returns the result tensor.
- [func L2NormPooling4DGradient(MPSGraphTensor, source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/l2normpooling4dgradient%28_,source,descriptor,name%29.md)
  Creates a L2-Norm pooling gradient operation and returns the result tensor.
- [func LSTM(MPSGraphTensor, recurrentWeight: MPSGraphTensor, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/lstm%28_,recurrentweight,initstate,initcell,descriptor,name%29.md)
  Creates an LSTM operation and returns the value tensor and optionally the cell state tensor and  the training state tensor.
- [func LSTM(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/lstm%28_,recurrentweight,inputweight,bias,initstate,initcell,descriptor,name%29.md)
  Creates an LSTM operation and returns the value tensor and optionally the cell state tensor and  the training state tensor.
- [func LSTM(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, mask: MPSGraphTensor?, peephole: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/lstm%28_,recurrentweight,inputweight,bias,initstate,initcell,mask,peephole,descriptor,name%29.md)
  Creates an LSTM operation and returns the value tensor and optionally the cell state tensor and  the training state tensor.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/lstmgradients%28_,recurrentweight,sourcegradient,zstate,celloutputfwd,descriptor,name%29.md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/lstmgradients%28_,recurrentweight,sourcegradient,zstate,celloutputfwd,inputweight,bias,initstate,initcell,descriptor,name%29.md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/lstmgradients%28_,recurrentweight,sourcegradient,zstate,celloutputfwd,inputweight,bias,initstate,initcell,mask,descriptor,name%29.md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func LSTMGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, cellOutputFwd: MPSGraphTensor, stateGradient: MPSGraphTensor?, cellGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, initCell: MPSGraphTensor?, mask: MPSGraphTensor?, peephole: MPSGraphTensor?, descriptor: MPSGraphLSTMDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/lstmgradients%28_,recurrentweight,sourcegradient,zstate,celloutputfwd,stategradient,cellgradient,inputweight,bias,initstate,initcell,mask,peephole,descriptor,name%29.md)
  Creates an LSTM gradient operation and returns the gradient tensor values.
- [func absolute(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/absolute%28with,name%29.md)
  Returns the absolute values of the input tensor elements.
- [func absoluteSquare(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/absolutesquare%28tensor,name%29.md)
  Returns the absolute square of the input tensor elements.
- [func acos(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/acos%28with,name%29.md)
  Applies the inverse cosine operation to the input tensor elements.
- [func acosh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/acosh%28with,name%29.md)
  Applies the inverse hyperbolic cosine operation to the input tensor elements.
- [func adam(currentLearningRate: MPSGraphTensor, beta1: MPSGraphTensor, beta2: MPSGraphTensor, epsilon: MPSGraphTensor, values: MPSGraphTensor, momentum: MPSGraphTensor, velocity: MPSGraphTensor, maximumVelocity: MPSGraphTensor?, gradient: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/adam%28currentlearningrate,beta1,beta2,epsilon,values,momentum,velocity,maximumvelocity,gradient,name%29.md)
  Creates operations to apply Adam optimization.
- [func adam(learningRate: MPSGraphTensor, beta1: MPSGraphTensor, beta2: MPSGraphTensor, epsilon: MPSGraphTensor, beta1Power: MPSGraphTensor, beta2Power: MPSGraphTensor, values: MPSGraphTensor, momentum: MPSGraphTensor, velocity: MPSGraphTensor, maximumVelocity: MPSGraphTensor?, gradient: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/adam%28learningrate,beta1,beta2,epsilon,beta1power,beta2power,values,momentum,velocity,maximumvelocity,gradient,name%29.md)
  Creates operations to apply Adam optimization.
- [func addition(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/addition%28_,_,name%29.md)
  Adds two input tensors.
- [func applyStochasticGradientDescent(learningRate: MPSGraphTensor, variable: MPSGraphVariableOp, gradient: MPSGraphTensor, name: String?) -> MPSGraphOperation](./mpsgraph/applystochasticgradientdescent%28learningrate,variable,gradient,name%29.md)
  The Stochastic gradient descent performs a gradient descent `variable = variable - (learningRate * g)` where, `g` is gradient of error wrt variable this op directly writes to the variable
- [func argSort(MPSGraphTensor, axis: Int, descending: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/argsort%28_,axis,descending,name%29.md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func argSort(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/argsort%28_,axis,name%29.md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func argSort(MPSGraphTensor, axisTensor: MPSGraphTensor, descending: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/argsort%28_,axistensor,descending,name%29.md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func argSort(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/argsort%28_,axistensor,name%29.md)
  Computes the indices that sort the elements of the input tensor along the specified axis.
- [func asin(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/asin%28with,name%29.md)
  Applies the inverse sine operation to the input tensor elements.
- [func asinh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/asinh%28with,name%29.md)
  Applies the inverse hyperbolic sine operation to the input tensor elements.
- [func assign(MPSGraphTensor, tensor: MPSGraphTensor, name: String?) -> MPSGraphOperation](./mpsgraph/assign%28_,tensor,name%29.md)
  Creates an assign operation which writes at this point of execution of the graph.
- [func atan(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/atan%28with,name%29.md)
  Applies the inverse tangent operation to the input tensor elements.
- [func atan2(withPrimaryTensor: MPSGraphTensor, secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/atan2%28withprimarytensor,secondarytensor,name%29.md)
  Returns the elementwise two-argument arctangent of the input tensors.
- [func atanh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/atanh%28with,name%29.md)
  Applies the inverse hyperbolic tangent operation to the input tensor elements.
- [func avgPooling2D(withSourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/avgpooling2d%28withsourcetensor,descriptor,name%29.md)
  Creates a 2D average-pooling operation and returns the result tensor.
- [func avgPooling2DGradient(withGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/avgpooling2dgradient%28withgradienttensor,sourcetensor,descriptor,name%29.md)
  Creates a 2D average pooling gradient operation and returns the result tensor.
- [func avgPooling4D(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/avgpooling4d%28_,descriptor,name%29.md)
  Creates a 4D average pooling operation and returns the result tensor.
- [func avgPooling4DGradient(MPSGraphTensor, source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/avgpooling4dgradient%28_,source,descriptor,name%29.md)
  Creates an average pooling gradient operation and returns the result tensor.
- [func bandPart(MPSGraphTensor, numLower: Int, numUpper: Int, name: String?) -> MPSGraphTensor](./mpsgraph/bandpart%28_,numlower,numupper,name%29.md)
  Computes the band part of an input tensor.
- [func bandPart(MPSGraphTensor, numLowerTensor: MPSGraphTensor, numUpperTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bandpart%28_,numlowertensor,numuppertensor,name%29.md)
  Creates the band part operation and returns the result.
- [func batchToSpace(MPSGraphTensor, spatialAxes: [NSNumber], batchAxis: Int, blockDimensions: [NSNumber], usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/batchtospace%28_,spatialaxes,batchaxis,blockdimensions,usepixelshuffleorder,name%29.md)
  Creates a batch-to-space operation and returns the result tensor.
- [func batchToSpace(MPSGraphTensor, spatialAxesTensor: MPSGraphTensor, batchAxisTensor: MPSGraphTensor, blockDimensionsTensor: MPSGraphTensor, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/batchtospace%28_,spatialaxestensor,batchaxistensor,blockdimensionstensor,usepixelshuffleorder,name%29.md)
  Creates a batch-to-space operation and returns the result tensor.
- [func bitwiseAND(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bitwiseand%28_,_,name%29.md)
  Returns the elementwise bitwise AND of binary representations of two integer tensors.
- [func bitwiseLeftShift(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bitwiseleftshift%28_,_,name%29.md)
  Returns the elementwise left-shifted binary representations of the primary integer by the secondary tensor amount.
- [func bitwiseNOT(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bitwisenot%28_,name%29.md)
  Applies the bitwise NOT operation to the input tensor element.
- [func bitwiseOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bitwiseor%28_,_,name%29.md)
  Returns the elementwise bitwise OR of binary representations of two integer tensors.
- [func bitwisePopulationCount(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bitwisepopulationcount%28_,name%29.md)
  Returns the population count of the input tensor elements.
- [func bitwiseRightShift(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bitwiserightshift%28_,_,name%29.md)
  Returns the elementwise right-shifted binary representations of the primary integer by the secondary tensor amount.
- [func bitwiseXOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bitwisexor%28_,_,name%29.md)
  Returns the elementwise bitwise XOR of binary representations of two integer tensors.
- [func bottomK(MPSGraphTensor, axis: Int, k: Int, name: String?) -> [MPSGraphTensor]](./mpsgraph/bottomk%28_,axis,k,name%29.md)
  Creates a BottomK operation and returns the value and indices tensors.
- [func bottomK(MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/bottomk%28_,axistensor,ktensor,name%29.md)
  Creates a BottomK operation and returns the result tensor.
- [func bottomKGradient(MPSGraphTensor, source: MPSGraphTensor, axis: Int, k: Int, name: String?) -> MPSGraphTensor](./mpsgraph/bottomkgradient%28_,source,axis,k,name%29.md)
  Creates a BottomKGradient operation and returns the result tensor.
- [func bottomKGradient(MPSGraphTensor, source: MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/bottomkgradient%28_,source,axistensor,ktensor,name%29.md)
  Creates a BottomKGradient operation and returns the result tensor.
- [func broadcast(MPSGraphTensor, shape: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/broadcast%28_,shape,name%29.md)
  Creates a broadcast operation and returns the result tensor.
- [func broadcast(MPSGraphTensor, shapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/broadcast%28_,shapetensor,name%29.md)
  Creates a broadcast operation and returns the result tensor.
- [func call(symbolName: String, inputTensors: [MPSGraphTensor], outputTypes: [MPSGraphType], name: String?) -> [MPSGraphTensor]](./mpsgraph/call%28symbolname,inputtensors,outputtypes,name%29.md)
  Creates an operation which invokes another executable.
- [func cast(MPSGraphTensor, to: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/cast%28_,to,name%29.md)
  Creates a cast operation and returns the result tensor.
- [func ceil(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/ceil%28with,name%29.md)
  Applies the ceiling operation to the input tensor elements.
- [func clamp(MPSGraphTensor, min: MPSGraphTensor, max: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/clamp%28_,min,max,name%29.md)
  Clamps the values in the first tensor between the corresponding values in the minimum and maximum value tensor.
- [func colToIm(MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphImToColOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/coltoim%28_,outputshape,descriptor,name%29.md)
  Creates a column to image operation and returns the result tensor.
- [func compile(with: MPSGraphDevice?, feeds: [MPSGraphTensor : MPSGraphShapedType], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, compilationDescriptor: MPSGraphCompilationDescriptor?) -> MPSGraphExecutable](./mpsgraph/compile%28with,feeds,targettensors,targetoperations,compilationdescriptor%29.md)
  Compiles the graph for the given feeds to returns the target tensor values, ensuring all target operations would be executed.
- [func complexConstant(realPart: Double, imaginaryPart: Double) -> MPSGraphTensor](./mpsgraph/complexconstant%28realpart,imaginarypart%29.md)
  Creates a complex constant op with the MPSDataTypeComplexFloat32 data type and returns the result tensor.
- [func complexConstant(realPart: Double, imaginaryPart: Double, dataType: MPSDataType) -> MPSGraphTensor](./mpsgraph/complexconstant%28realpart,imaginarypart,datatype%29.md)
  Creates a complex constant operation and returns the result tensor.
- [func complexConstant(realPart: Double, imaginaryPart: Double, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor](./mpsgraph/complexconstant%28realpart,imaginarypart,shape,datatype%29.md)
  Creates a complex constant op with a given shape and returns the result tensor.
- [func complexTensor(realTensor: MPSGraphTensor, imaginaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/complextensor%28realtensor,imaginarytensor,name%29.md)
  Returns a complex tensor from the two input tensors.
- [func concatTensor(MPSGraphTensor, with: MPSGraphTensor, dimension: Int, name: String?) -> MPSGraphTensor](./mpsgraph/concattensor%28_,with,dimension,name%29.md)
  Creates a concatenation operation and returns the result tensor.
- [func concatTensors([MPSGraphTensor], dimension: Int, interleave: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/concattensors%28_,dimension,interleave,name%29.md)
  Creates a concatenation operation and returns the result tensor.
- [func concatTensors([MPSGraphTensor], dimension: Int, name: String?) -> MPSGraphTensor](./mpsgraph/concattensors%28_,dimension,name%29.md)
  Creates a concatenation operation and returns the result tensor.
- [func conjugate(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/conjugate%28tensor,name%29.md)
  Returns the complex conjugate of the input tensor elements.
- [func constant(Double, dataType: MPSDataType) -> MPSGraphTensor](./mpsgraph/constant%28_,datatype%29.md)
  Creates a constant operation and returns the result tensor.
- [func constant(Double, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor](./mpsgraph/constant%28_,shape,datatype%29-3wa0e.md)
  Creates a constant op with a given shape and returns the result tensor.
- [func constant(Data, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor](./mpsgraph/constant%28_,shape,datatype%29-ylr4.md)
  Creates a constant op with a given shape and data, and returns the result tensor.
- [func controlDependency(with: [MPSGraphOperation], dependentBlock: MPSGraphControlFlowDependencyBlock, name: String?) -> [MPSGraphTensor]](./mpsgraph/controldependency%28with,dependentblock,name%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func convolution2D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution2d%28_,weights,descriptor,name%29.md)
  Creates a 2D (forward) convolution operation and returns the result tensor.
- [func convolution2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution2ddatagradient%28_,weights,outputshape,forwardconvolutiondescriptor,name%29.md)
  Creates a 2D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution2ddatagradient%28_,weights,outputshapetensor,forwardconvolutiondescriptor,name%29.md)
  Creates a 2D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution2DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution2dweightsgradient%28_,source,outputshape,forwardconvolutiondescriptor,name%29.md)
  Creates a 2D convolution gradient operation with respect to the weights tensor of the forward convolution.
- [func convolution2DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution2dweightsgradient%28_,source,outputshapetensor,forwardconvolutiondescriptor,name%29.md)
  Creates a 2D convolution gradient operation with respect to weights tensor of forward convolution.
- [func convolution3D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution3d%28_,weights,descriptor,name%29.md)
  Creates a 3D forward convolution operation and returns the result tensor.
- [func convolution3DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution3ddatagradient%28_,weights,outputshape,forwardconvolutiondescriptor,name%29.md)
  Creates a 3D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution3DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution3ddatagradient%28_,weights,outputshapetensor,forwardconvolutiondescriptor,name%29.md)
  Creates a 3D convolution gradient operation with respect to the source tensor of the forward convolution.
- [func convolution3DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution3dweightsgradient%28_,source,outputshape,forwardconvolutiondescriptor,name%29.md)
  Creates a 3D convolution gradient operation with respect to the weights tensor of the forward convolution.
- [func convolution3DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolution3dweightsgradient%28_,source,outputshapetensor,forwardconvolutiondescriptor,name%29.md)
  Creates a 3D convolution gradient operation with respect to the weights tensor of the forward convolution.
- [func convolutionTranspose2D(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolutiontranspose2d%28_,weights,outputshape,descriptor,name%29.md)
  Creates a convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2D(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolutiontranspose2d%28_,weights,outputshapetensor,descriptor,name%29.md)
  Creates a convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolutiontranspose2ddatagradient%28_,weights,outputshape,forwardconvolutiondescriptor,name%29.md)
  Creates a convolution transpose gradient operation with respect to the source tensor of convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolutiontranspose2ddatagradient%28_,weights,outputshapetensor,forwardconvolutiondescriptor,name%29.md)
  Creates a convolution transpose gradient operation with respect to the source tensor of convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DWeightsGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolutiontranspose2dweightsgradient%28_,weights,outputshape,forwardconvolutiondescriptor,name%29.md)
  Creates a convolution transpose gradient operation with respect to the weights tensor of the convolution transpose operation and returns the result tensor.
- [func convolutionTranspose2DWeightsGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/convolutiontranspose2dweightsgradient%28_,weights,outputshapetensor,forwardconvolutiondescriptor,name%29.md)
  Creates a convolution transpose gradient operation with respect to the weights tensor of the convolution transpose operation and returns the result tensor.
- [func coordinate(alongAxis: Int, withShape: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/coordinate%28alongaxis,withshape,name%29.md)
  Creates a get-coordindate operation and returns the result tensor.
- [func coordinate(alongAxis: Int, withShapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/coordinate%28alongaxis,withshapetensor,name%29.md)
  Creates a get-coordindate operation and returns the result tensor.
- [func coordinate(alongAxisTensor: MPSGraphTensor, withShape: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/coordinate%28alongaxistensor,withshape,name%29.md)
  Creates a get-coordindate operation and returns the result tensor.
- [func coordinate(alongAxisTensor: MPSGraphTensor, withShapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/coordinate%28alongaxistensor,withshapetensor,name%29.md)
  Creates a get-coordindate operation and returns the result tensor.
- [func cos(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/cos%28with,name%29.md)
  Applies the cosine operation to the input tensor elements.
- [func cosh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/cosh%28with,name%29.md)
  Applies the hyperbolic cosine operation to the input tensor elements.
- [func cumulativeMaximum(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativemaximum%28_,axis,exclusive,reverse,name%29.md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMaximum(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativemaximum%28_,axis,name%29.md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMaximum(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativemaximum%28_,axistensor,exclusive,reverse,name%29.md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMaximum(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativemaximum%28_,axistensor,name%29.md)
  Computes the cumulative maximum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeminimum%28_,axis,exclusive,reverse,name%29.md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeminimum%28_,axis,name%29.md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeminimum%28_,axistensor,exclusive,reverse,name%29.md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeMinimum(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeminimum%28_,axistensor,name%29.md)
  Computes the cumulative minimum of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeproduct%28_,axis,exclusive,reverse,name%29.md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeproduct%28_,axis,name%29.md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeproduct%28_,axistensor,exclusive,reverse,name%29.md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeProduct(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativeproduct%28_,axistensor,name%29.md)
  Computes the cumulative product of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativesum%28_,axis,exclusive,reverse,name%29.md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativesum%28_,axis,name%29.md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativesum%28_,axistensor,exclusive,reverse,name%29.md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func cumulativeSum(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/cumulativesum%28_,axistensor,name%29.md)
  Computes the cumulative sum of the input tensor along the specified axis.
- [func depth(toSpace2DTensor: MPSGraphTensor, widthAxis: Int, heightAxis: Int, depthAxis: Int, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/depth%28tospace2dtensor,widthaxis,heightaxis,depthaxis,blocksize,usepixelshuffleorder,name%29.md)
  Creates a depth-to-space2D operation and returns the result tensor.
- [func depth(toSpace2DTensor: MPSGraphTensor, widthAxisTensor: MPSGraphTensor, heightAxisTensor: MPSGraphTensor, depthAxisTensor: MPSGraphTensor, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/depth%28tospace2dtensor,widthaxistensor,heightaxistensor,depthaxistensor,blocksize,usepixelshuffleorder,name%29.md)
  Creates a depth-to-space2D operation and returns the result tensor.
- [func depthwiseConvolution2D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/depthwiseconvolution2d%28_,weights,descriptor,name%29.md)
  Creates a 2D-depthwise convolution operation and returns the result tensor.
- [func depthwiseConvolution2DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/depthwiseconvolution2ddatagradient%28_,weights,outputshape,descriptor,name%29.md)
  Creates a 2D-depthwise convolution gradient for data operation and returns the result tensor.
- [func depthwiseConvolution2DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/depthwiseconvolution2dweightsgradient%28_,source,outputshape,descriptor,name%29.md)
  Creates a 2D-depthwise convolution gradient for weights operation and returns the result tensor.
- [func depthwiseConvolution3D(MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphDepthwiseConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/depthwiseconvolution3d%28_,weights,descriptor,name%29.md)
  Creates a 3D depthwise convolution operation and returns the result tensor.
- [func depthwiseConvolution3DDataGradient(MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber]?, descriptor: MPSGraphDepthwiseConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/depthwiseconvolution3ddatagradient%28_,weights,outputshape,descriptor,name%29.md)
  Creates a 3D depthwise convolution gradient for data operation and returns the result tensor.
- [func depthwiseConvolution3DWeightsGradient(MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphDepthwiseConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/depthwiseconvolution3dweightsgradient%28_,source,outputshape,descriptor,name%29.md)
  Creates a 3D depthwise convolution gradient for weights operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, LUTTensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/dequantize%28_,luttensor,axis,name%29.md)
  Creates a vector lookup-table based dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, LUTTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/dequantize%28_,luttensor,name%29.md)
  Creates a lookup-table based dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scale: Double, zeroPoint: Double, dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/dequantize%28_,scale,zeropoint,datatype,name%29.md)
  Creates Dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/dequantize%28_,scaletensor,datatype,name%29.md)
  Creates a dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPoint: Double, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/dequantize%28_,scaletensor,zeropoint,datatype,axis,name%29.md)
  Creates Dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPointTensor: MPSGraphTensor, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/dequantize%28_,scaletensor,zeropointtensor,datatype,axis,name%29.md)
  Creates a dequantize operation and returns the result tensor.
- [func dequantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPointTensor: MPSGraphTensor, dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/dequantize%28_,scaletensor,zeropointtensor,datatype,name%29.md)
  Creates a dequantize operation and returns the result tensor.
- [func division(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/division%28_,_,name%29.md)
  Divides the first input tensor by the second.
- [func divisionNoNaN(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/divisionnonan%28_,_,name%29.md)
  Divides the first input tensor by the second, with the result being 0 if the denominator is 0.
- [func dropout(MPSGraphTensor, rate: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/dropout%28_,rate,name%29-16cq4.md)
  Creates a dropout operation and returns the result
- [func dropout(MPSGraphTensor, rate: Double, name: String?) -> MPSGraphTensor](./mpsgraph/dropout%28_,rate,name%29-6hvf3.md)
  Creates a dropout operation and returns the result
- [func encode(to: MPSCommandBuffer, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData], executionDescriptor: MPSGraphExecutionDescriptor?)](./mpsgraph/encode%28to,feeds,targetoperations,resultsdictionary,executiondescriptor%29.md)
  Encodes the graph for the given feeds to returns the target tensor values in the results dictionary provided by the user.
- [func encode(to: MPSCommandBuffer, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]](./mpsgraph/encode%28to,feeds,targettensors,targetoperations,executiondescriptor%29.md)
  Encodes the graph for the given feeds to returns the target tensor values, ensuring all target operations also executed.
- [func equal(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/equal%28_,_,name%29.md)
  Returns the elementwise equality check of the input tensors.
- [func erf(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/erf%28with,name%29.md)
  Applies the error function to the input tensor elements.
- [func expandDims(MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/expanddims%28_,axes,name%29.md)
  Creates an expand-dimensions operation and returns the result tensor.
- [func expandDims(MPSGraphTensor, axesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/expanddims%28_,axestensor,name%29.md)
  Creates an expand-dimensions operation and returns the result tensor.
- [func expandDims(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/expanddims%28_,axis,name%29.md)
  Creates an expand-dimensions operation and returns the result tensor.
- [func exponent(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/exponent%28with,name%29.md)
  Applies the natural exponent to the input tensor elements.
- [func exponentBase10(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/exponentbase10%28with,name%29.md)
  Applies an exponent with base 10 to the input tensor elements.
- [func exponentBase2(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/exponentbase2%28with,name%29.md)
  Applies an exponent with base 2 to the input tensor elements.
- [func fastFourierTransform(MPSGraphTensor, axes: [NSNumber], descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/fastfouriertransform%28_,axes,descriptor,name%29.md)
  Creates a fast Fourier transform operation and returns the result tensor.
- [func fastFourierTransform(MPSGraphTensor, axesTensor: MPSGraphTensor, descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/fastfouriertransform%28_,axestensor,descriptor,name%29.md)
  Creates a fast Fourier transform operation and returns the result tensor.
- [func flatten2D(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/flatten2d%28_,axis,name%29.md)
  Creates a flatten2D operation and returns the result tensor.
- [func flatten2D(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/flatten2d%28_,axistensor,name%29.md)
  Creates a flatten2D operation and returns the result tensor.
- [func floor(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/floor%28with,name%29.md)
  Applies the floor operation to the input tensor elements.
- [func floorModulo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/floormodulo%28_,_,name%29.md)
  Returns the remainder of floor divison between the primary and secondary tensor.
- [func `for`(lowerBound: MPSGraphTensor, upperBound: MPSGraphTensor, step: MPSGraphTensor, initialBodyArguments: [MPSGraphTensor], body: MPSGraphForLoopBodyBlock, name: String?) -> [MPSGraphTensor]](./mpsgraph/for%28lowerbound,upperbound,step,initialbodyarguments,body,name%29.md)
  Adds a for loop operation, The lower and upper bounds specify a half-open range: the range includes the lower bound but does not include the upper bound.
- [func `for`(numberOfIterations: MPSGraphTensor, initialBodyArguments: [MPSGraphTensor], body: MPSGraphForLoopBodyBlock, name: String?) -> [MPSGraphTensor]](./mpsgraph/for%28numberofiterations,initialbodyarguments,body,name%29.md)
  Adds a for loop operation, with a specific number of iterations.
- [func gather(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, axis: Int, batchDimensions: Int, name: String?) -> MPSGraphTensor](./mpsgraph/gather%28withupdatestensor,indicestensor,axis,batchdimensions,name%29.md)
  Creates a Gather operation and returns the result tensor.
- [func gatherAlongAxis(Int, updates: MPSGraphTensor, indices: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/gatheralongaxis%28_,updates,indices,name%29.md)
  Creates a GatherAlongAxis operation and returns the result tensor.
- [func gatherAlongAxisTensor(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/gatheralongaxistensor%28_,updates,indices,name%29.md)
  Creates a GatherAlongAxis operation and returns the result tensor.
- [func gatherND(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, batchDimensions: Int, name: String?) -> MPSGraphTensor](./mpsgraph/gathernd%28withupdatestensor,indicestensor,batchdimensions,name%29.md)
  Creates a GatherND operation and returns the result tensor.
- [func gradients(of: MPSGraphTensor, with: [MPSGraphTensor], name: String?) -> [MPSGraphTensor : MPSGraphTensor]](./mpsgraph/gradients%28of,with,name%29.md)
  Calculates a partial derivative of primaryTensor with respect to the tensors.
- [func greaterThan(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/greaterthan%28_,_,name%29.md)
  Checks in an elementwise manner if the first input tensor is greater than the second.
- [func greaterThanOrEqualTo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/greaterthanorequalto%28_,_,name%29.md)
  Checks in an elementwise manner if the first input tensor is greater than or equal to the second.
- [func identity(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/identity%28with,name%29.md)
  Copies the input tensor values into the output, behaving as an identity operation.
- [func `if`(MPSGraphTensor, then: MPSGraphIfThenElseBlock, else: MPSGraphIfThenElseBlock?, name: String?) -> [MPSGraphTensor]](./mpsgraph/if%28_,then,else,name%29.md)
  Adds an if-then-else operation to the graph.
- [func imToCol(MPSGraphTensor, descriptor: MPSGraphImToColOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/imtocol%28_,descriptor,name%29.md)
  Creates an imToCol operation and returns the result tensor.
- [func imaginaryPartOfTensor(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/imaginarypartoftensor%28tensor,name%29.md)
  Returns the imaginary part of a tensor.
- [func inverse(input: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/inverse%28input,name%29.md)
  Computes the inverse of an input tensor.
- [func isFinite(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/isfinite%28with,name%29.md)
  Checks if the input tensor elements are finite or not.
- [func isInfinite(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/isinfinite%28with,name%29.md)
  Checks if the input tensor elements are infinite or not.
- [func isNaN(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/isnan%28with,name%29.md)
  Checks if the input tensor elements are `NaN` or not.
- [func leakyReLU(with: MPSGraphTensor, alpha: Double, name: String?) -> MPSGraphTensor](./mpsgraph/leakyrelu%28with,alpha,name%29.md)
  Computes the leaky rectified linear unit (ReLU) activation function on the input tensor.
- [func leakyReLU(with: MPSGraphTensor, alphaTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/leakyrelu%28with,alphatensor,name%29.md)
  Computes the leaky rectified linear unit (ReLU) activation function on the input tensor.
- [func leakyReLUGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, alphaTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/leakyrelugradient%28withincominggradient,sourcetensor,alphatensor,name%29.md)
  Computes the gradient of the leaky rectified linear unit (ReLU) activation.
- [func lessThan(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/lessthan%28_,_,name%29.md)
  Checks in an elementwise manner if the first input tensor is less than the second.
- [func lessThanOrEqualTo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/lessthanorequalto%28_,_,name%29.md)
  Checks in an elementwise manner if the first input tensor is less than or equal to the second.
- [func logarithm(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logarithm%28with,name%29.md)
  Computes the natural logarithm to the input tensor elements.
- [func logarithmBase10(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logarithmbase10%28with,name%29.md)
  Computes the logarithm with base 10 to the input tensor elements.
- [func logarithmBase2(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logarithmbase2%28with,name%29.md)
  Computes the logarithm with base 2 to the input tensor elements.
- [func logicalAND(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logicaland%28_,_,name%29.md)
  Returns the elementwise logical AND of the input tensors.
- [func logicalNAND(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logicalnand%28_,_,name%29.md)
  Returns the elementwise logical NAND of the input tensors.
- [func logicalNOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logicalnor%28_,_,name%29.md)
  Returns the elementwise logical NOR of the input tensors.
- [func logicalOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logicalor%28_,_,name%29.md)
  Returns the elementwise logical OR of the input tensors.
- [func logicalXNOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logicalxnor%28_,_,name%29.md)
  Returns the elementwise logical XNOR of the input tensors.
- [func logicalXOR(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/logicalxor%28_,_,name%29.md)
  Returns the elementwise logical XOR of the input tensors.
- [func matrixMultiplication(primary: MPSGraphTensor, secondary: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/matrixmultiplication%28primary,secondary,name%29.md)
  Computes the matrix multiplication of 2 input tensors with support for broadcasting.
- [func maxPooling2D(withSourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling2d%28withsourcetensor,descriptor,name%29.md)
  Creates a 2D max-pooling operation and returns the result tensor.
- [func maxPooling2DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling2dgradient%28withgradienttensor,indicestensor,outputshape,descriptor,name%29.md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling2DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling2dgradient%28withgradienttensor,indicestensor,outputshapetensor,descriptor,name%29.md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling2DGradient(withGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling2dgradient%28withgradienttensor,sourcetensor,descriptor,name%29.md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling2DReturnIndices(MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/maxpooling2dreturnindices%28_,descriptor,name%29.md)
  Creates a 2D max-pooling operation and returns the result tensor and the corresponding indices tensor.
- [func maxPooling4D(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling4d%28_,descriptor,name%29.md)
  Creates a 4D max-pooling operation and returns the result tensor.
- [func maxPooling4DGradient(MPSGraphTensor, source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling4dgradient%28_,source,descriptor,name%29.md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling4DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling4dgradient%28withgradienttensor,indicestensor,outputshape,descriptor,name%29.md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling4DGradient(withGradientTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/maxpooling4dgradient%28withgradienttensor,indicestensor,outputshapetensor,descriptor,name%29.md)
  Creates a max-pooling gradient operation and returns the result tensor.
- [func maxPooling4DReturnIndices(MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/maxpooling4dreturnindices%28_,descriptor,name%29.md)
  Creates a 4D max-pooling operation and returns the result tensor and the corresponding indices tensor.
- [func maximum(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/maximum%28_,_,name%29.md)
  Returns the elementwise maximum of the input tensors.
- [func maximumWithNaNPropagation(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/maximumwithnanpropagation%28_,_,name%29.md)
  Returns the elementwise maximum of the input tensors, while propagating `NaN` values.
- [func mean(of: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/mean%28of,axes,name%29.md)
  Returns the mean of the first input along the specified axes.
- [func minimum(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/minimum%28_,_,name%29.md)
  Returns the elementwise minimum of the input tensors.
- [func minimumWithNaNPropagation(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/minimumwithnanpropagation%28_,_,name%29.md)
  Returns the elementwise minimum of the input tensors, while propagating `NaN` values.
- [func modulo(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/modulo%28_,_,name%29.md)
  Returns the remainder obtained by dividing the first input tensor by the second.
- [func multiplication(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/multiplication%28_,_,name%29.md)
  Multiplies two input tensors.
- [func negative(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/negative%28with,name%29.md)
  Applies negative to the input tensor elements.
- [func nonMaximumSuppression(withBoxesTensor: MPSGraphTensor, scoresTensor: MPSGraphTensor, classIndicesTensor: MPSGraphTensor, iouThreshold: Float, scoreThreshold: Float, perClassSuppression: Bool, coordinateMode: MPSGraphNonMaximumSuppressionCoordinateMode, name: String?) -> MPSGraphTensor](./mpsgraph/nonmaximumsuppression%28withboxestensor,scorestensor,classindicestensor,iouthreshold,scorethreshold,perclasssuppression,coordinatemode,name%29.md)
  Creates a nonMaximumumSuppression operation and returns the result tensor.
- [func nonMaximumSuppression(withBoxesTensor: MPSGraphTensor, scoresTensor: MPSGraphTensor, iouThreshold: Float, scoreThreshold: Float, perClassSuppression: Bool, coordinateMode: MPSGraphNonMaximumSuppressionCoordinateMode, name: String?) -> MPSGraphTensor](./mpsgraph/nonmaximumsuppression%28withboxestensor,scorestensor,iouthreshold,scorethreshold,perclasssuppression,coordinatemode,name%29.md)
  Creates a nonMaximumumSuppression operation and returns the result tensor.
- [func nonZeroIndices(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/nonzeroindices%28_,name%29.md)
  Computes the indices of the non-zero elements of the input tensor.
- [func normalizationBetaGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, reductionAxes: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/normalizationbetagradient%28withincominggradienttensor,sourcetensor,reductionaxes,name%29.md)
  Creates a normalization beta-gradient operation and returns the result tensor.
- [func normalizationGammaGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, mean: MPSGraphTensor, varianceTensor: MPSGraphTensor, reductionAxes: [NSNumber], epsilon: Float, name: String?) -> MPSGraphTensor](./mpsgraph/normalizationgammagradient%28withincominggradienttensor,sourcetensor,mean,variancetensor,reductionaxes,epsilon,name%29.md)
  Creates a normalization gamma-gradient operation and returns the result tensor.
- [func normalizationGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, mean: MPSGraphTensor, varianceTensor: MPSGraphTensor, gammaTensor: MPSGraphTensor?, gammaGradientTensor: MPSGraphTensor?, betaGradientTensor: MPSGraphTensor?, reductionAxes: [NSNumber], epsilon: Float, name: String?) -> MPSGraphTensor](./mpsgraph/normalizationgradient%28withincominggradienttensor,sourcetensor,mean,variancetensor,gammatensor,gammagradienttensor,betagradienttensor,reductionaxes,epsilon,name%29.md)
  Creates a normalization input gradient operation and returns the result tensor.
- [func normalize(MPSGraphTensor, mean: MPSGraphTensor, variance: MPSGraphTensor, gamma: MPSGraphTensor?, beta: MPSGraphTensor?, epsilon: Float, name: String?) -> MPSGraphTensor](./mpsgraph/normalize%28_,mean,variance,gamma,beta,epsilon,name%29.md)
  Creates a batch normalization operation and returns the result tensor.
- [func not(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/not%28with,name%29.md)
  Applies the logical NOT operation to the input tensor elements.
- [func notEqual(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/notequal%28_,_,name%29.md)
  Returns the elementwise inequality check of the input tensors.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, axis: Int, dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/onehot%28withindicestensor,depth,axis,datatype,name%29.md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, axis: Int, dataType: MPSDataType, onValue: Double, offValue: Double, name: String?) -> MPSGraphTensor](./mpsgraph/onehot%28withindicestensor,depth,axis,datatype,onvalue,offvalue,name%29.md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/onehot%28withindicestensor,depth,axis,name%29.md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/onehot%28withindicestensor,depth,datatype,name%29.md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, dataType: MPSDataType, onValue: Double, offValue: Double, name: String?) -> MPSGraphTensor](./mpsgraph/onehot%28withindicestensor,depth,datatype,onvalue,offvalue,name%29.md)
  Creates a oneHot operation and returns the result tensor.
- [func oneHot(withIndicesTensor: MPSGraphTensor, depth: Int, name: String?) -> MPSGraphTensor](./mpsgraph/onehot%28withindicestensor,depth,name%29.md)
  Creates a oneHot operation and returns the result tensor.
- [func padGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, paddingMode: MPSGraphPaddingMode, leftPadding: [NSNumber], rightPadding: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/padgradient%28withincominggradienttensor,sourcetensor,paddingmode,leftpadding,rightpadding,name%29.md)
  Creates a padding gradient operation and returns the result tensor.
- [func padTensor(MPSGraphTensor, with: MPSGraphPaddingMode, leftPadding: [NSNumber], rightPadding: [NSNumber], constantValue: Double, name: String?) -> MPSGraphTensor](./mpsgraph/padtensor%28_,with,leftpadding,rightpadding,constantvalue,name%29.md)
  Creates a padding operation and returns the result tensor.
- [func placeholder(shape: [NSNumber]?, dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/placeholder%28shape,datatype,name%29.md)
  Creates a placeholder operation and returns the result tensor.
- [func placeholder(shape: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/placeholder%28shape,name%29.md)
  Creates a placeholder operation and returns the result tensor with the dataType of the placeholder tensor set to 32 bit float.
- [func planarTensor(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/planartensor%28tensor,name%29.md)
  Returns a real-valued tensor from a complex-valued tensor with real and imaginary planes separated.
- [func power(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/power%28_,_,name%29.md)
  Returns the elementwise result of raising the first tensor to the power of the second tensor.
- [func quantize(MPSGraphTensor, scale: Double, zeroPoint: Double, dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/quantize%28_,scale,zeropoint,datatype,name%29.md)
  Creates a Quantize operation and returns the result tensor.
- [func quantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPoint: Double, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/quantize%28_,scaletensor,zeropoint,datatype,axis,name%29.md)
  Creates a Quantize operation and returns the result tensor.
- [func quantize(MPSGraphTensor, scaleTensor: MPSGraphTensor, zeroPointTensor: MPSGraphTensor, dataType: MPSDataType, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/quantize%28_,scaletensor,zeropointtensor,datatype,axis,name%29.md)
  Creates a Quantize operation and returns the result tensor.
- [func randomPhiloxStateTensor(withCounterLow: Int, counterHigh: Int, key: Int, name: String?) -> MPSGraphTensor](./mpsgraph/randomphiloxstatetensor%28withcounterlow,counterhigh,key,name%29.md)
  Creates a tensor representing state using the Philox algorithm with given counter and key values.
- [func randomPhiloxStateTensor(withSeed: Int, name: String?) -> MPSGraphTensor](./mpsgraph/randomphiloxstatetensor%28withseed,name%29.md)
  Creates a tensor representing state using the Philox algorithm with given counter and key values.
- [func randomTensor(withShape: [NSNumber], descriptor: MPSGraphRandomOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/randomtensor%28withshape,descriptor,name%29.md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShape: [NSNumber], descriptor: MPSGraphRandomOpDescriptor, seed: Int, name: String?) -> MPSGraphTensor](./mpsgraph/randomtensor%28withshape,descriptor,seed,name%29.md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShape: [NSNumber], descriptor: MPSGraphRandomOpDescriptor, stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/randomtensor%28withshape,descriptor,statetensor,name%29.md)
  Creates a Random op of type matching distribution in descriptor, and returns random values and updated state.
- [func randomTensor(withShapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/randomtensor%28withshapetensor,descriptor,name%29.md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, seed: Int, name: String?) -> MPSGraphTensor](./mpsgraph/randomtensor%28withshapetensor,descriptor,seed,name%29.md)
  Creates a Random op of type matching distribution in descriptor and returns random values.
- [func randomTensor(withShapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/randomtensor%28withshapetensor,descriptor,statetensor,name%29.md)
  Creates a Random op of type matching distribution in descriptor, and returns random values and updated state.
- [func randomUniformTensor(withShape: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/randomuniformtensor%28withshape,name%29.md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShape: [NSNumber], seed: Int, name: String?) -> MPSGraphTensor](./mpsgraph/randomuniformtensor%28withshape,seed,name%29.md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShape: [NSNumber], stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/randomuniformtensor%28withshape,statetensor,name%29.md)
  Creates a RandomUniform operation and returns random uniform values and updated state
- [func randomUniformTensor(withShapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/randomuniformtensor%28withshapetensor,name%29.md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShapeTensor: MPSGraphTensor, seed: Int, name: String?) -> MPSGraphTensor](./mpsgraph/randomuniformtensor%28withshapetensor,seed,name%29.md)
  Creates a RandomUniform operation and returns random uniform values
- [func randomUniformTensor(withShapeTensor: MPSGraphTensor, stateTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/randomuniformtensor%28withshapetensor,statetensor,name%29.md)
  Creates a RandomUniform operation and returns random uniform values and updated state
- [func reLU(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/relu%28with,name%29.md)
  Computes the ReLU (rectified linear activation unit) function with the input tensor.
- [func reLUGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/relugradient%28withincominggradient,sourcetensor,name%29.md)
  Computes the gradient of the ReLU  (rectified linear activation unit) function using the incoming gradient.
- [func read(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/read%28_,name%29.md)
  Creates a read op which reads at this point of execution of the graph and returns the result tensor.
- [func realPartOfTensor(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/realpartoftensor%28tensor,name%29.md)
  Returns the real part of a tensor.
- [func realToHermiteanFFT(MPSGraphTensor, axes: [NSNumber], descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/realtohermiteanfft%28_,axes,descriptor,name%29.md)
  Creates a Real-to-Hermitean fast Fourier transform operation and returns the result tensor.
- [func realToHermiteanFFT(MPSGraphTensor, axesTensor: MPSGraphTensor, descriptor: MPSGraphFFTDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/realtohermiteanfft%28_,axestensor,descriptor,name%29.md)
  Creates a Real-to-Hermitean fast Fourier transform operation and returns the result tensor.
- [func reciprocal(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/reciprocal%28with,name%29.md)
  Applies the reciprocal operation to the input tensor elements.
- [func reciprocalSquareRoot(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/reciprocalsquareroot%28_,name%29.md)
  Applies the reciprocal square root operation to the input tensor elements.
- [func reductionAnd(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionand%28with,axes,name%29.md)
  Creates a reduction and operation and returns the result tensor.
- [func reductionAnd(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionand%28with,axis,name%29.md)
  Creates a reduction and operation and returns the result tensor.
- [func reductionArgMaximum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionargmaximum%28with,axis,name%29.md)
  Creates a reduction argMax operation and returns the result tensor.
- [func reductionArgMinimum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionargminimum%28with,axis,name%29.md)
  Creates a reduction argMin operation and returns the result tensor.
- [func reductionMaximum(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionmaximum%28with,axes,name%29.md)
  Creates a reduction max operation and returns the result tensor.
- [func reductionMaximum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionmaximum%28with,axis,name%29.md)
  Creates a reduction max operation and returns the result tensor.
- [func reductionMaximumPropagateNaN(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionmaximumpropagatenan%28with,axes,name%29.md)
  Creates a reduction max propagate NaN operation and returns the result tensor.
- [func reductionMaximumPropagateNaN(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionmaximumpropagatenan%28with,axis,name%29.md)
  Creates a reduction max propagate NaN operation and returns the result tensor.
- [func reductionMinimum(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionminimum%28with,axes,name%29.md)
  Creates a reduction min operation and returns the result tensor.
- [func reductionMinimum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionminimum%28with,axis,name%29.md)
  Creates a reduction minimum operation and returns the result tensor.
- [func reductionMinimumPropagateNaN(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionminimumpropagatenan%28with,axes,name%29.md)
  Creates a reduction min propagate NaN operation and returns the result tensor.
- [func reductionMinimumPropagateNaN(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionminimumpropagatenan%28with,axis,name%29.md)
  Creates a reduction min propagate NaN operation and returns the result tensor.
- [func reductionOr(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionor%28with,axes,name%29.md)
  Creates a reduction or operation and returns the result tensor.
- [func reductionOr(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionor%28with,axis,name%29.md)
  Creates a reduction or operation and returns the result tensor.
- [func reductionProduct(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionproduct%28with,axes,name%29.md)
  Creates a reduction product operation and returns the result tensor.
- [func reductionProduct(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionproduct%28with,axis,name%29.md)
  Creates a reduction product operation and returns the result tensor.
- [func reductionSum(with: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor](./mpsgraph/reductionsum%28with,axes,name%29.md)
  Creates a reduction sum operation and returns the result tensor.
- [func reductionSum(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/reductionsum%28with,axis,name%29.md)
  Creates a reduction sum operation and returns the result tensor.
- [func reinterpretCast(MPSGraphTensor, to: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/reinterpretcast%28_,to,name%29.md)
  Creates a reinterpret cast operation and returns the result tensor.
- [func reshape(MPSGraphTensor, shape: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/reshape%28_,shape,name%29.md)
  Creates a reshape operation and returns the result tensor.
- [func reshape(MPSGraphTensor, shapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/reshape%28_,shapetensor,name%29.md)
  Creates a reshape operation and returns the result tensor.
- [func resize(MPSGraphTensor, size: [NSNumber], mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28_,size,mode,centerresult,aligncorners,layout,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28_,sizetensor,mode,centerresult,aligncorners,layout,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28_,sizetensor,mode,centerresult,aligncorners,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, mode: MPSGraphResizeMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28_,sizetensor,scaleoffsettensor,mode,layout,name%29.md)
  Resamples input images to given size using the provided scale and offset. Destination indices are computed using
- [func resize(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, offsetTenor: MPSGraphTensor, mode: MPSGraphResizeMode, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28_,sizetensor,scaletensor,offsettenor,mode,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resize(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, mode: MPSGraphResizeMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28withgradienttensor,input,mode,centerresult,aligncorners,layout,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resize(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor: MPSGraphTensor, mode: MPSGraphResizeMode, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28withgradienttensor,input,scale,offsettensor,mode,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resize(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, mode: MPSGraphResizeMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resize%28withgradienttensor,input,scaleoffsettensor,mode,layout,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizebilinear%28_,sizetensor,centerresult,aligncorners,layout,name%29.md)
  Resamples input images to given size using bilinear sampling.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, centerResult: Bool, alignCorners: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/resizebilinear%28_,sizetensor,centerresult,aligncorners,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizebilinear%28_,sizetensor,scaleoffsettensor,layout,name%29.md)
  Resamples input images to given size using the provided scale and offset and bilinear sampling See above discussion for more details.
- [func resizeBilinear(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, offsetTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/resizebilinear%28_,sizetensor,scaletensor,offsettensor,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resizeBilinear(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizebilinear%28withgradienttensor,input,centerresult,aligncorners,layout,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeBilinear(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/resizebilinear%28withgradienttensor,input,scale,offsettensor,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeBilinear(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizebilinear%28withgradienttensor,input,scaleoffsettensor,layout,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizenearest%28_,sizetensor,nearestroundingmode,centerresult,aligncorners,layout,name%29.md)
  Resamples input images to given size using nearest neighbor sampling.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, centerResult: Bool, alignCorners: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/resizenearest%28_,sizetensor,nearestroundingmode,centerresult,aligncorners,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizenearest%28_,sizetensor,scaleoffsettensor,nearestroundingmode,layout,name%29.md)
  Resamples input images to given size using the provided scale and offset and nearest neighbor sampling See above discussion for more details.
- [func resizeNearest(MPSGraphTensor, sizeTensor: MPSGraphTensor, scaleTensor: MPSGraphTensor, offsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, name: String?) -> MPSGraphTensor](./mpsgraph/resizenearest%28_,sizetensor,scaletensor,offsettensor,nearestroundingmode,name%29.md)
  Creates a Resize operation and returns the result tensor.
- [func resizeNearest(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, centerResult: Bool, alignCorners: Bool, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizenearest%28withgradienttensor,input,nearestroundingmode,centerresult,aligncorners,layout,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeNearest(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, name: String?) -> MPSGraphTensor](./mpsgraph/resizenearest%28withgradienttensor,input,scale,offsettensor,nearestroundingmode,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func resizeNearest(withGradientTensor: MPSGraphTensor, input: MPSGraphTensor, scaleOffsetTensor: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, layout: MPSGraphTensorNamedDataLayout, name: String?) -> MPSGraphTensor](./mpsgraph/resizenearest%28withgradienttensor,input,scaleoffsettensor,nearestroundingmode,layout,name%29.md)
  Creates a Resize gradient operation and returns the result tensor.
- [func reverse(MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/reverse%28_,axes,name%29.md)
  Creates a reverse operation and returns the result tensor.
- [func reverse(MPSGraphTensor, axesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/reverse%28_,axestensor,name%29.md)
  Creates a reverse operation and returns the result tensor.
- [func reverse(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/reverse%28_,name%29.md)
  Creates a reverse operation and returns the result tensor.
- [func reverseSquareRoot(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/reversesquareroot%28with,name%29.md)
  Applies the reverse square root operation to the input tensor elements.
- [func rint(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/rint%28with,name%29.md)
  Rounds the input tensor elements by rounding to nearest even.
- [func round(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/round%28with,name%29.md)
  Rounds the input tensor elements.
- [func run(feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?) -> [MPSGraphTensor : MPSGraphTensorData]](./mpsgraph/run%28feeds,targettensors,targetoperations%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func run(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData])](./mpsgraph/run%28with,feeds,targetoperations,resultsdictionary%29.md)
  Runs the graph for the given feeds and returns the target tensor values in the results dictionary provided by the user.
- [func run(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?) -> [MPSGraphTensor : MPSGraphTensorData]](./mpsgraph/run%28with,feeds,targettensors,targetoperations%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func runAsync(feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]](./mpsgraph/runasync%28feeds,targettensors,targetoperations,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func runAsync(on: any MTL4CommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData], executionDescriptor: MPSGraphExecutionDescriptor?)](./mpsgraph/runasync%28on,feeds,targetoperations,resultsdictionary,executiondescriptor%29.md)
  Encodes the graph for the given feeds to returns the target tensor values in the results dictionary provided by the user.
- [func runAsync(on: any MTL4CommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]](./mpsgraph/runasync%28on,feeds,targettensors,targetoperations,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func runAsync(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData], executionDescriptor: MPSGraphExecutionDescriptor?)](./mpsgraph/runasync%28with,feeds,targetoperations,resultsdictionary,executiondescriptor%29.md)
  Encodes the graph for the given feeds to returns the target tensor values in the results dictionary provided by the user.
- [func runAsync(with: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]](./mpsgraph/runasync%28with,feeds,targettensors,targetoperations,executiondescriptor%29.md)
  Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.
- [func sampleGrid(withSourceTensor: MPSGraphTensor, coordinateTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, normalizeCoordinates: Bool, relativeCoordinates: Bool, alignCorners: Bool, paddingMode: MPSGraphPaddingMode, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, constantValue: Double, name: String?) -> MPSGraphTensor](./mpsgraph/samplegrid%28withsourcetensor,coordinatetensor,layout,normalizecoordinates,relativecoordinates,aligncorners,paddingmode,nearestroundingmode,constantvalue,name%29.md)
  Samples a tensor using the coordinates provided, using nearest neighbor sampling with specified rounding mode.
- [func sampleGrid(withSourceTensor: MPSGraphTensor, coordinateTensor: MPSGraphTensor, layout: MPSGraphTensorNamedDataLayout, normalizeCoordinates: Bool, relativeCoordinates: Bool, alignCorners: Bool, paddingMode: MPSGraphPaddingMode, samplingMode: MPSGraphResizeMode, constantValue: Double, name: String?) -> MPSGraphTensor](./mpsgraph/samplegrid%28withsourcetensor,coordinatetensor,layout,normalizecoordinates,relativecoordinates,aligncorners,paddingmode,samplingmode,constantvalue,name%29.md)
  Samples a tensor using the coordinates provided.
- [func scaledDotProductAttention(query: MPSGraphTensor, key: MPSGraphTensor, value: MPSGraphTensor, descriptor: MPSGraphSDPADescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/scaleddotproductattention%28query,key,value,descriptor,name%29.md)
  Creates a scaled dot product attention (SDPA) operation using a descriptor and returns the result tensor.
- [func scaledDotProductAttention(query: MPSGraphTensor, key: MPSGraphTensor, value: MPSGraphTensor, mask: MPSGraphTensor?, scale: Float, name: String?) -> MPSGraphTensor](./mpsgraph/scaleddotproductattention%28query,key,value,mask,scale,name%29.md)
  Creates a scaled dot product attention (SDPA) operation and returns the result tensor.
- [func scaledDotProductAttention(query: MPSGraphTensor, key: MPSGraphTensor, value: MPSGraphTensor, scale: Float, name: String?) -> MPSGraphTensor](./mpsgraph/scaleddotproductattention%28query,key,value,scale,name%29.md)
  Creates a scaled dot product attention (SDPA) operation (without a mask) and returns the result tensor.
- [func scatter(MPSGraphTensor, indices: MPSGraphTensor, shape: [NSNumber], axis: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatter%28_,indices,shape,axis,mode,name%29.md)
  Creates a Scatter operation and returns the result tensor.
- [func scatterAlongAxis(Int, data: MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatteralongaxis%28_,data,updates,indices,mode,name%29.md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterAlongAxis(Int, updates: MPSGraphTensor, indices: MPSGraphTensor, shape: [NSNumber], mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatteralongaxis%28_,updates,indices,shape,mode,name%29.md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterAlongAxisTensor(MPSGraphTensor, data: MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatteralongaxistensor%28_,data,updates,indices,mode,name%29.md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterAlongAxisTensor(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, shape: [NSNumber], mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatteralongaxistensor%28_,updates,indices,shape,mode,name%29.md)
  Creates a ScatterAlongAxis operation and returns the result tensor.
- [func scatterND(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, shape: [NSNumber], batchDimensions: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatternd%28withupdatestensor,indicestensor,shape,batchdimensions,mode,name%29.md)
  Creates a ScatterND operation and returns the result tensor.
- [func scatterND(withUpdatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, shape: [NSNumber], batchDimensions: Int, name: String?) -> MPSGraphTensor](./mpsgraph/scatternd%28withupdatestensor,indicestensor,shape,batchdimensions,name%29.md)
  Creates a ScatterND operation and returns the result tensor.
- [func scatterNDWithData(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, batchDimensions: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatterndwithdata%28_,updates,indices,batchdimensions,mode,name%29.md)
  Creates a ScatterND operation and returns the result tensor.
- [func scatterWithData(MPSGraphTensor, updates: MPSGraphTensor, indices: MPSGraphTensor, axis: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor](./mpsgraph/scatterwithdata%28_,updates,indices,axis,mode,name%29.md)
  Creates a Scatter operation and returns the result tensor.
- [func select(predicate: MPSGraphTensor, trueTensor: MPSGraphTensor, falseTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/select%28predicate,truetensor,falsetensor,name%29.md)
  Selects values from either the true or false predicate tensor, depending on the values in the first input.
- [func shapeOf(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/shapeof%28_,name%29.md)
  Creates a shape-of operation and returns the result tensor.
- [func sigmoid(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/sigmoid%28with,name%29.md)
  Computes the sigmoid operation on an input tensor.
- [func sigmoidGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/sigmoidgradient%28withincominggradient,sourcetensor,name%29.md)
  Computes the gradient of the sigmoid function using the incoming gradient tensor.
- [func sign(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/sign%28with,name%29.md)
  Returns the sign of the input tensor elements.
- [func signbit(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/signbit%28with,name%29.md)
  Returns the sign bit of the input tensor elements.
- [func sin(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/sin%28with,name%29.md)
  Applies the sine operation to the input tensor elements.
- [func singleGateRNN(MPSGraphTensor, recurrentWeight: MPSGraphTensor, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/singlegaternn%28_,recurrentweight,initstate,descriptor,name%29.md)
  Creates a single-gate RNN operation and returns the value and optionally the training state tensor.
- [func singleGateRNN(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/singlegaternn%28_,recurrentweight,inputweight,bias,initstate,descriptor,name%29.md)
  Creates a single-gate RNN operation and returns the value and optionally the training state tensor.
- [func singleGateRNN(MPSGraphTensor, recurrentWeight: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/singlegaternn%28_,recurrentweight,inputweight,bias,initstate,mask,descriptor,name%29.md)
  Creates a single-gate RNN operation and returns the value and optionally the training state tensor.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/singlegaternngradients%28_,recurrentweight,sourcegradient,zstate,initstate,descriptor,name%29.md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/singlegaternngradients%28_,recurrentweight,sourcegradient,zstate,inputweight,bias,initstate,descriptor,name%29.md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/singlegaternngradients%28_,recurrentweight,sourcegradient,zstate,inputweight,bias,initstate,mask,descriptor,name%29.md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func singleGateRNNGradients(MPSGraphTensor, recurrentWeight: MPSGraphTensor, sourceGradient: MPSGraphTensor, zState: MPSGraphTensor, stateGradient: MPSGraphTensor?, inputWeight: MPSGraphTensor?, bias: MPSGraphTensor?, initState: MPSGraphTensor?, mask: MPSGraphTensor?, descriptor: MPSGraphSingleGateRNNDescriptor, name: String?) -> [MPSGraphTensor]](./mpsgraph/singlegaternngradients%28_,recurrentweight,sourcegradient,zstate,stategradient,inputweight,bias,initstate,mask,descriptor,name%29.md)
  Creates a single-gate RNN gradient operation and returns the gradient tensor values.
- [func sinh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/sinh%28with,name%29.md)
  Applies the hyperbolic sine operation to the input tensor elements.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, start: MPSGraphTensor, end: MPSGraphTensor, strideTensor: MPSGraphTensor, startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/slicegradienttensor%28_,fwdinshapetensor,start,end,stridetensor,startmask,endmask,squeezemask,name%29.md)
  Creates a strided-slice gradient operation and returns the result tensor.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, start: MPSGraphTensor, sizeTensor: MPSGraphTensor, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/slicegradienttensor%28_,fwdinshapetensor,start,sizetensor,squeezemask,name%29.md)
  Creates a slice gradient operation and returns the result tensor.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/slicegradienttensor%28_,fwdinshapetensor,starts,ends,strides,name%29.md)
  Creates a strided-slice gradient operation and returns the result tensor.
- [func sliceGradientTensor(MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/slicegradienttensor%28_,fwdinshapetensor,starts,ends,strides,startmask,endmask,squeezemask,name%29.md)
  Creates a strided-slice gradient operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, dimension: Int, start: Int, length: Int, name: String?) -> MPSGraphTensor](./mpsgraph/slicetensor%28_,dimension,start,length,name%29.md)
  Creates a slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, start: MPSGraphTensor, end: MPSGraphTensor, strideTensor: MPSGraphTensor, startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/slicetensor%28_,start,end,stridetensor,startmask,endmask,squeezemask,name%29.md)
  Creates a strided-slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, start: MPSGraphTensor, sizeTensor: MPSGraphTensor, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/slicetensor%28_,start,sizetensor,squeezemask,name%29.md)
  Creates a slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/slicetensor%28_,starts,ends,strides,name%29.md)
  Creates a strided-slice operation and returns the result tensor.
- [func sliceTensor(MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/slicetensor%28_,starts,ends,strides,startmask,endmask,squeezemask,name%29.md)
  Creates a strided-slice operation and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/sliceupdatedatatensor%28_,update,starts,ends,strides,name%29.md)
  Creates a strided-slice update operation with zero masks and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/sliceupdatedatatensor%28_,update,starts,ends,strides,startmask,endmask,squeezemask,name%29.md)
  Creates a strided-slice update operation and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, startsTensor: MPSGraphTensor, endsTensor: MPSGraphTensor, stridesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/sliceupdatedatatensor%28_,update,startstensor,endstensor,stridestensor,name%29.md)
  Creates a strided-slice update operation with zero masks and returns the result tensor.
- [func sliceUpdateDataTensor(MPSGraphTensor, update: MPSGraphTensor, startsTensor: MPSGraphTensor, endsTensor: MPSGraphTensor, stridesTensor: MPSGraphTensor, startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor](./mpsgraph/sliceupdatedatatensor%28_,update,startstensor,endstensor,stridestensor,startmask,endmask,squeezemask,name%29.md)
  Creates a strided-slice update operation and returns the result tensor.
- [func softMax(with: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/softmax%28with,axis,name%29.md)
  Computes the softmax function on the input tensor along the specified axis.
- [func softMaxCrossEntropy(MPSGraphTensor, labels: MPSGraphTensor, axis: Int, reuctionType: MPSGraphLossReductionType, name: String?) -> MPSGraphTensor](./mpsgraph/softmaxcrossentropy%28_,labels,axis,reuctiontype,name%29.md)
  Creates a softmax cross-entropy loss operation and returns the result tensor.
- [func softMaxCrossEntropyGradient(MPSGraphTensor, source: MPSGraphTensor, labels: MPSGraphTensor, axis: Int, reuctionType: MPSGraphLossReductionType, name: String?) -> MPSGraphTensor](./mpsgraph/softmaxcrossentropygradient%28_,source,labels,axis,reuctiontype,name%29.md)
  Creates the gradient of a softmax cross-entropy loss operation and returns the result tensor.
- [func softMaxGradient(withIncomingGradient: MPSGraphTensor, sourceTensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/softmaxgradient%28withincominggradient,sourcetensor,axis,name%29.md)
  Computes the gradient of the softmax function along the specified axis using the incoming gradient tensor.
- [func sort(MPSGraphTensor, axis: Int, descending: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/sort%28_,axis,descending,name%29.md)
  Sorts the elements of the input tensor along the specified axis.
- [func sort(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/sort%28_,axis,name%29.md)
  Sorts the elements of the input tensor along the specified axis.
- [func sort(MPSGraphTensor, axisTensor: MPSGraphTensor, descending: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/sort%28_,axistensor,descending,name%29.md)
  Sorts the elements of the input tensor along the specified axis.
- [func sort(MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/sort%28_,axistensor,name%29.md)
  Sorts the elements of the input tensor along the specified axis.
- [func space(toDepth2DTensor: MPSGraphTensor, widthAxis: Int, heightAxis: Int, depthAxis: Int, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/space%28todepth2dtensor,widthaxis,heightaxis,depthaxis,blocksize,usepixelshuffleorder,name%29.md)
  Creates a space-to-depth2D operation and returns the result tensor.
- [func space(toDepth2DTensor: MPSGraphTensor, widthAxisTensor: MPSGraphTensor, heightAxisTensor: MPSGraphTensor, depthAxisTensor: MPSGraphTensor, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/space%28todepth2dtensor,widthaxistensor,heightaxistensor,depthaxistensor,blocksize,usepixelshuffleorder,name%29.md)
  Creates a space-to-depth2D operation and returns the result tensor.
- [func spaceToBatch(MPSGraphTensor, spatialAxes: [NSNumber], batchAxis: Int, blockDimensions: [NSNumber], usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/spacetobatch%28_,spatialaxes,batchaxis,blockdimensions,usepixelshuffleorder,name%29.md)
  Creates a space-to-batch operation and returns the result tensor.
- [func spaceToBatch(MPSGraphTensor, spatialAxesTensor: MPSGraphTensor, batchAxisTensor: MPSGraphTensor, blockDimensionsTensor: MPSGraphTensor, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor](./mpsgraph/spacetobatch%28_,spatialaxestensor,batchaxistensor,blockdimensionstensor,usepixelshuffleorder,name%29.md)
  Creates a space-to-batch operation and returns the result tensor.
- [func sparseTensor(sparseTensorWithDescriptor: MPSGraphCreateSparseOpDescriptor, tensors: [MPSGraphTensor], shape: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/sparsetensor%28sparsetensorwithdescriptor,tensors,shape,name%29.md)
  Creates a sparse tensor representation.
- [func sparseTensor(sparseTensorWithType: MPSGraphSparseStorageType, tensors: [MPSGraphTensor], shape: [NSNumber], dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/sparsetensor%28sparsetensorwithtype,tensors,shape,datatype,name%29.md)
  Creates a sparse tensor representation.
- [func split(MPSGraphTensor, numSplits: Int, axis: Int, name: String?) -> [MPSGraphTensor]](./mpsgraph/split%28_,numsplits,axis,name%29.md)
  Creates a split operation and returns the result tensor.
- [func split(MPSGraphTensor, splitSizes: [NSNumber], axis: Int, name: String?) -> [MPSGraphTensor]](./mpsgraph/split%28_,splitsizes,axis,name%29.md)
  Creates a split operation and returns the result tensor.
- [func split(MPSGraphTensor, splitSizesTensor: MPSGraphTensor, axis: Int, name: String?) -> [MPSGraphTensor]](./mpsgraph/split%28_,splitsizestensor,axis,name%29.md)
  Creates a split operation and returns the result tensor.
- [func square(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/square%28with,name%29.md)
  Applies the square operation to the input tensor elements.
- [func squareRoot(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/squareroot%28with,name%29.md)
  Applies the square root operation to the input tensor elements.
- [func squeeze(MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/squeeze%28_,axes,name%29.md)
  Creates a squeeze operation and returns the result tensor.
- [func squeeze(MPSGraphTensor, axesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/squeeze%28_,axestensor,name%29.md)
  Creates a squeeze operation and returns the result tensor.
- [func squeeze(MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/squeeze%28_,axis,name%29.md)
  Creates a squeeze operation and returns the result tensor.
- [func squeeze(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/squeeze%28_,name%29.md)
  Creates a squeeze operation and returns the result tensor.
- [func stack([MPSGraphTensor], axis: Int, name: String?) -> MPSGraphTensor](./mpsgraph/stack%28_,axis,name%29.md)
  Creates a stack operation and returns the result tensor.
- [func stencil(withSourceTensor: MPSGraphTensor, weightsTensor: MPSGraphTensor, descriptor: MPSGraphStencilOpDescriptor, name: String?) -> MPSGraphTensor](./mpsgraph/stencil%28withsourcetensor,weightstensor,descriptor,name%29.md)
  Creates a stencil operation and returns the result tensor.
- [func stochasticGradientDescent(learningRate: MPSGraphTensor, values: MPSGraphTensor, gradient: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/stochasticgradientdescent%28learningrate,values,gradient,name%29.md)
  The Stochastic gradient descent performs a gradient descent.
- [func subtraction(MPSGraphTensor, MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/subtraction%28_,_,name%29.md)
  Subtracts the second input tensor from the first.
- [func tan(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/tan%28with,name%29.md)
  Applies the tangent operation to the input tensor elements.
- [func tanh(with: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/tanh%28with,name%29.md)
  Applies the hyperbolic tangent operation to the input tensor elements.
- [func tileGradient(withIncomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, withMultiplier: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/tilegradient%28withincominggradienttensor,sourcetensor,withmultiplier,name%29.md)
  Creates a tile gradient operation and returns the result tensor.
- [func tileTensor(MPSGraphTensor, withMultiplier: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/tiletensor%28_,withmultiplier,name%29.md)
  Creates a tile operation and returns the result tensor.
- [func topK(MPSGraphTensor, axis: Int, k: Int, name: String?) -> [MPSGraphTensor]](./mpsgraph/topk%28_,axis,k,name%29.md)
  Creates a TopK operation and returns the value and indices tensors.
- [func topK(MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/topk%28_,axistensor,ktensor,name%29.md)
  Creates a TopK operation and returns the result tensor.
- [func topK(MPSGraphTensor, k: Int, name: String?) -> [MPSGraphTensor]](./mpsgraph/topk%28_,k,name%29.md)
  Creates a TopK operation and returns the value and indices tensors
- [func topK(MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]](./mpsgraph/topk%28_,ktensor,name%29.md)
  Creates a TopK operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, input: MPSGraphTensor, k: Int, name: String?) -> MPSGraphTensor](./mpsgraph/topkgradient%28_,input,k,name%29.md)
  Creates a TopKGradient operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, input: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/topkgradient%28_,input,ktensor,name%29.md)
  Creates a TopKGradient operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, source: MPSGraphTensor, axis: Int, k: Int, name: String?) -> MPSGraphTensor](./mpsgraph/topkgradient%28_,source,axis,k,name%29.md)
  Creates a TopKGradient operation and returns the result tensor.
- [func topKGradient(MPSGraphTensor, source: MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/topkgradient%28_,source,axistensor,ktensor,name%29.md)
  Creates a TopKGradient operation and returns the result tensor.
- [func transpose(MPSGraphTensor, permutation: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/transpose%28_,permutation,name%29.md)
  Creates a permutation operation and returns the result tensor.
- [func transposeTensor(MPSGraphTensor, dimension: Int, withDimension: Int, name: String?) -> MPSGraphTensor](./mpsgraph/transposetensor%28_,dimension,withdimension,name%29.md)
  Creates a transpose operation and returns the result tensor.
- [func truncate(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/truncate%28_,name%29.md)
  Applies the truncate operation to the input tensor elements.
- [func variable(with: Data, shape: [NSNumber], dataType: MPSDataType, name: String?) -> MPSGraphTensor](./mpsgraph/variable%28with,shape,datatype,name%29.md)
  Creates a variable operation and returns the result tensor.
- [func variableFromTensor(MPSGraphTensor, name: String?) -> MPSGraphTensor](./mpsgraph/variablefromtensor%28_,name%29.md)
  Creates a variable from an input tensor.
- [func variance(of: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/variance%28of,axes,name%29.md)
  Returns the variance of the first input along the specified axes.
- [func variance(of: MPSGraphTensor, mean: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor](./mpsgraph/variance%28of,mean,axes,name%29.md)
  Returns the variance of the first input along the specified axes when the mean has been precomputed.
- [func `while`(initialInputs: [MPSGraphTensor], before: MPSGraphWhileBeforeBlock, after: MPSGraphWhileAfterBlock, name: String?) -> [MPSGraphTensor]](./mpsgraph/while%28initialinputs,before,after,name%29.md)
  Adds a while loop operation.
### Type Methods
- [class func new() -> Self](./mpsgraph/new%28%29.md)
  Creates a new graph to insert nodes in.

## Relationships

### Inherits From
- [MPSGraphObject](./mpsgraphobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
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
- [class MPSGraphGRUDescriptor](./mpsgraphgrudescriptor.md)
  The class that defines the parameters for a gated recurrent unit (GRU) operation.
- [class MPSGraphImToColOpDescriptor](./mpsgraphimtocolopdescriptor.md)
  The class that defines the parameters for an image to column or column to image operation.
- [class MPSGraphLSTMDescriptor](./mpsgraphlstmdescriptor.md)
  The class that defines the parameters for a long short-term memory (LSTM) operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph)*