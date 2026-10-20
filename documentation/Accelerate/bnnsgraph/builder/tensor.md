# BNNSGraph.Builder.Tensor

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Tensor<T> where T : BNNSScalar
```

## Topics

### Operators
- [static func .! (BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotnot%28_%29.md)
  Adds an element-wise logical not operation to the current graph.
- [static func .!= (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotnoteq%28_,_%29.md)
  Adds an element-wise inequality operation to the current graph.
- [static func .& (BNNSGraph.Builder.Tensor<Bool>, BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotamp%28_,_%29.md)
  Adds an element-wise logical and operation to the current graph.
- [static func .== (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/doteqeq%28_,_%29.md)
  Adds an element-wise equality operation to the current graph.
- [static func .| (BNNSGraph.Builder.Tensor<Bool>, BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotop%28_,_%29-171l2.md)
  Adds an element-wise logical or operation to the current graph.
- [static func .< (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotop%28_,_%29-6sgl6.md)
  Adds an element-wise less than comparison operation to the current graph.
- [static func .^ (BNNSGraph.Builder.Tensor<Bool>, BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotop%28_,_%29-6soc4.md)
  Adds an element-wise logical xor operation to the current graph.
- [static func .> (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotop%28_,_%29-9vd51.md)
  Adds an element-wise greater than comparison operation to the current graph.
- [static func .<= (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotopeq%28_,_%29-20vpj.md)
  Adds an element-wise less than or equal comparison operation to the current graph.
- [static func .>= (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](./tensor/dotopeq%28_,_%29-6gvvh.md)
  Adds an element-wise greater than or equal comparison operation to the current graph.
### Instance Properties
- [var dataType: BNNSDataType?](./tensor/datatype.md)
  The data type of the tensor.
- [var description: String](./tensor/description.md)
  A textual representation of this instance.
- [var rank: Int?](./tensor/rank.md)
  The rank of the tensor.
- [var shape: [Int]?](./tensor/shape.md)
  The shape of the tensor.
- [var stride: [Int]?](./tensor/stride.md)
  The stride of the tensor.
### Instance Methods
- [func abs() -> BNNSGraph.Builder.Tensor<T>](./tensor/abs%28%29.md)
  Adds an element-wise absolute operation to the current graph.
- [func acos() -> BNNSGraph.Builder.Tensor<T>](./tensor/acos%28%29.md)
  Adds an element-wise acos operation to the current graph.
- [func acosh() -> BNNSGraph.Builder.Tensor<T>](./tensor/acosh%28%29.md)
  Adds an element-wise atan operation to the current graph.
- [func argMax(axis: Int, keepDimension: Bool) -> BNNSGraph.Builder.Tensor<Int32>](./tensor/argmax%28axis,keepdimension%29.md)
  Adds an argmax operation to the current graph.
- [func argMin(axis: Int, keepDimension: Bool) -> BNNSGraph.Builder.Tensor<Int32>](./tensor/argmin%28axis,keepdimension%29.md)
  Adds an argmin operation to the current graph.
- [func argSort(axis: Int, sortOrder: BNNSGraph.Builder.SortOrder) -> BNNSGraph.Builder.Tensor<Int32>](./tensor/argsort%28axis,sortorder%29.md)
  Adds an argsort operation to the current graph.
- [func asin() -> BNNSGraph.Builder.Tensor<T>](./tensor/asin%28%29.md)
  Adds an element-wise asin operation to the current graph.
- [func asinh() -> BNNSGraph.Builder.Tensor<T>](./tensor/asinh%28%29.md)
  Adds an element-wise asinh operation to the current graph.
- [func atan() -> BNNSGraph.Builder.Tensor<T>](./tensor/atan%28%29.md)
  Adds an element-wise atan operation to the current graph.
- [func atanh() -> BNNSGraph.Builder.Tensor<T>](./tensor/atanh%28%29.md)
  Adds an element-wise atanh operation to the current graph.
- [func batchNorm(mean: some BNNSGraph.Builder.OperationParameter<T>, variance: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/batchnorm%28mean,variance,epsilon%29.md)
  Adds a batch normalization operation to the current graph.
- [func batchNorm(mean: some BNNSGraph.Builder.OperationParameter<T>, variance: some BNNSGraph.Builder.OperationParameter<T>, weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/batchnorm%28mean,variance,weight,bias,epsilon%29.md)
  Adds a batch normalization operation to the current graph.
- [func bidirectionalLSTM(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, initialCellStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, inputHiddenWeightBack: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeightBack: BNNSGraph.Builder.Tensor<T>, biasBack: BNNSGraph.Builder.Tensor<T>, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, cellActivation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>, memoryStates: BNNSGraph.Builder.Tensor<T>)](./tensor/bidirectionallstm%28initialhiddenstates,initialcellstates,inputhiddenweight,hiddenhiddenweight,bias,inputhiddenweightback,hiddenhiddenweightback,biasback,activation,recurrentactivation,cellactivation,outputsequence%29.md)
  Adds a bidirectional LSTM operation to the current graph.
- [func cast<U>(to: U.Type) -> BNNSGraph.Builder.Tensor<U>](./tensor/cast%28to%29.md)
  Adds a cast operation to the current graph.
- [func ceil() -> BNNSGraph.Builder.Tensor<T>](./tensor/ceil%28%29.md)
  Adds an element-wise ceiling operation to the current graph.
- [func channelNorm(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/channelnorm%28epsilon%29.md)
  Adds a channel normalization operation to the current graph.
- [func channelNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/channelnorm%28weight,bias,epsilon%29.md)
  Adds a channel normalization operation to the current graph.
- [func clampedReLU(alpha: Float, beta: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/clampedrelu%28alpha,beta%29.md)
  Adds a Clamped Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func clip(to: ClosedRange<Float>) -> BNNSGraph.Builder.Tensor<T>](./tensor/clip%28to%29.md)
  Adds an element-wise clip operation to the current graph.
- [func conv(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], bias: some BNNSGraph.Builder.OperationParameter<T>, padding: BNNSGraph.Builder.ConvolutionPadding, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/conv%28weight,strides,bias,padding,dilations,groupcount%29.md)
  Adds a convolution operation to the current graph.
- [func conv(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], padding: BNNSGraph.Builder.ConvolutionPadding, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/conv%28weight,strides,padding,dilations,groupcount%29.md)
  Adds a convolution operation to the current graph.
- [func convTranspose(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], bias: some BNNSGraph.Builder.OperationParameter<T>, padding: BNNSGraph.Builder.ConvolutionPadding, outputPaddingValues: [Int]?, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/convtranspose%28weight,strides,bias,padding,outputpaddingvalues,dilations,groupcount%29.md)
  Adds a transposed convolution operation to the current graph.
- [func convTranspose(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], padding: BNNSGraph.Builder.ConvolutionPadding, outputPaddingValues: [Int]?, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/convtranspose%28weight,strides,padding,outputpaddingvalues,dilations,groupcount%29.md)
  Adds a transposed convolution operation to the current graph.
- [func cos() -> BNNSGraph.Builder.Tensor<T>](./tensor/cos%28%29.md)
  Adds an element-wise cos operation to the current graph.
- [func cosh() -> BNNSGraph.Builder.Tensor<T>](./tensor/cosh%28%29.md)
  Adds an element-wise cosh operation to the current graph.
- [func cumulativeSum(axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/cumulativesum%28axis%29.md)
  Adds a cumulative sum operation to the the graph.
- [func elu(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/elu%28alpha%29.md)
  Adds an Exponential Linear Unit (ELU) activation operation to the current graph.
- [func erf() -> BNNSGraph.Builder.Tensor<T>](./tensor/erf%28%29.md)
  Adds an Error Function (erf) activation operation to the current graph.
- [func exp() -> BNNSGraph.Builder.Tensor<T>](./tensor/exp%28%29.md)
  Adds an element-wise exp operation to the current graph.
- [func exp2() -> BNNSGraph.Builder.Tensor<T>](./tensor/exp2%28%29.md)
  Adds an element-wise exp operation to the current graph.
- [func floor() -> BNNSGraph.Builder.Tensor<T>](./tensor/floor%28%29.md)
  Adds an element-wise floor operation to the current graph.
- [func fma(y: some BNNSGraph.Builder.OperationParameter<T>, z: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](./tensor/fma%28y,z%29.md)
  Adds an element-wise fused multiply-add operation to the current graph.
- [func gather(indices: some BNNSGraph.Builder.OperationParameter<Int32>, axis: Int, batchDimensionCount: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/gather%28indices,axis,batchdimensioncount%29.md)
  Adds a gather operation to the current graph.
- [func gatherAlongAxis(indices: some BNNSGraph.Builder.OperationParameter<Int32>, axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/gatheralongaxis%28indices,axis%29.md)
  Adds a gather-along-axis operation to the current graph.
- [func gatherND(indices: some BNNSGraph.Builder.OperationParameter<Int32>, batchDimensionCount: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/gathernd%28indices,batchdimensioncount%29.md)
  Adds a gather-nd operation to the current graph.
- [func gelu() -> BNNSGraph.Builder.Tensor<T>](./tensor/gelu%28%29.md)
  Adds a Gaussian Error Linear Unit (GELU) activation operation to the current graph.
- [func geluSigmoidApproximation() -> BNNSGraph.Builder.Tensor<T>](./tensor/gelusigmoidapproximation%28%29.md)
  Adds a Gaussian Error Linear Unit (GELU) sigmoid approximation activation operation to the current graph.
- [func geluTanhApproximation() -> BNNSGraph.Builder.Tensor<T>](./tensor/gelutanhapproximation%28%29.md)
  Adds a Gaussian Error Linear Unit (GELU) tanh approximation activation operation to the current graph.
- [func gru(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, inputBias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, applyResetGateAfterMatMul: Bool, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>)](./tensor/gru%28initialhiddenstates,inputhiddenweight,hiddenhiddenweight,bias,inputbias,direction,activation,recurrentactivation,applyresetgateaftermatmul,outputsequence%29.md)
  Adds a GRU operation to the current graph.
- [func hardSigmoid(alpha: Float, beta: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/hardsigmoid%28alpha,beta%29.md)
  Adds a hard sigmoid activation operation to the current graph.
- [func hardSwish() -> BNNSGraph.Builder.Tensor<T>](./tensor/hardswish%28%29.md)
  Adds a hard swish activation operation to the current graph.
- [func instanceNorm(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/instancenorm%28epsilon%29.md)
  Adds a instance normalization operation to the current graph.
- [func instanceNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/instancenorm%28weight,bias,epsilon%29.md)
  Adds a instance normalization operation to the current graph.
- [func l1Norm(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/l1norm%28axes,keepdimensions%29.md)
  Adds a sum-of-absolutes reduction operation along the given axis operation to the current graph.
- [func l2Norm(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/l2norm%28axes,keepdimensions%29.md)
  Adds a Euclidean-norm reduction operation along the given axis operation to the current graph.
- [func l2Norm(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/l2norm%28epsilon%29.md)
  Adds an L2 spatial normalization operation to the current graph.
- [func layerNorm(axes: [Int], epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/layernorm%28axes,epsilon%29.md)
  Adds a layer normalization operation to the current graph.
- [func layerNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, axes: [Int], epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/layernorm%28weight,bias,axes,epsilon%29.md)
  Adds a layer normalization operation to the current graph.
- [func leakyReLU(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/leakyrelu%28alpha%29.md)
  Adds a Leaky Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func linear(weight: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](./tensor/linear%28weight%29.md)
  Adds a linear transformation operation to the current graph.
- [func linear(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](./tensor/linear%28weight,bias%29.md)
  Adds a linear transformation operation to the current graph.
- [func log(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/log%28epsilon%29.md)
  Adds an element-wise log operation to the current graph.
- [func logSoftmax(axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/logsoftmax%28axis%29.md)
  Adds a log-softmax along the given axis operation to the current graph.
- [func logSum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/logsum%28axes,keepdimensions%29.md)
  Adds a log-sum reduction operation along the given axis operation to the current graph.
- [func logSumExp(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/logsumexp%28axes,keepdimensions%29.md)
  Adds a log-sum-exp reduction operation along the given axis operation to the current graph.
- [func lstm(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, initialCellStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, cellActivation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>, memoryStates: BNNSGraph.Builder.Tensor<T>)](./tensor/lstm%28initialhiddenstates,initialcellstates,inputhiddenweight,hiddenhiddenweight,bias,direction,activation,recurrentactivation,cellactivation,outputsequence%29.md)
  Adds an LSTM operation to the current graph.
- [func matmul(transpose: Bool, other: some BNNSGraph.Builder.OperationParameter<T>, transposeOther: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/matmul%28transpose,other,transposeother%29.md)
  Adds a matrix-matrix multiplication operation to the current graph.
- [func matmul(transpose: Bool, other: some BNNSGraph.Builder.OperationParameter<T>, transposeOther: Bool, bias: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](./tensor/matmul%28transpose,other,transposeother,bias%29.md)
  Adds a matrix-matrix multiplication operation to the current graph.
- [func max(y: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](./tensor/max%28y%29.md)
  Adds an element-wise maximum operation to the current graph.
- [func maximum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/maximum%28axes,keepdimensions%29.md)
  Adds a maximum reduction operation along the given axis operation to the current graph.
- [func mean(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/mean%28axes,keepdimensions%29.md)
  Adds a mean reduction operation along the given axis operation to the current graph.
- [func min(y: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](./tensor/min%28y%29.md)
  Adds an element-wise minimum operation to the current graph.
- [func minimum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/minimum%28axes,keepdimensions%29.md)
  Adds a minimum reduction operation along the given axis operation to the current graph.
- [func pad(BNNSGraph.Builder.Padding, padding: [Int]) -> BNNSGraph.Builder.Tensor<T>](./tensor/pad%28_,padding%29.md)
  Adds a padding operation to the graph
- [func pooling(BNNSGraph.Builder.PoolingFunction, kernelSize: [Int], strides: [Int], padding: BNNSGraph.Builder.PoolingPadding, ceilingMode: BNNSGraph.Builder.CeilingMode) -> BNNSGraph.Builder.Tensor<T>](./tensor/pooling%28_,kernelsize,strides,padding,ceilingmode%29.md)
  Adds a pooling operation to the current graph.
- [func pow(y: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](./tensor/pow%28y%29.md)
  Adds an element-wise power operation to the current graph.
- [func prelu(alpha: [Float]) -> BNNSGraph.Builder.Tensor<T>](./tensor/prelu%28alpha%29.md)
  Adds a Parametric ReLU (PReLU) activation operation to the current graph.
- [func product(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/product%28axes,keepdimensions%29.md)
  Adds a product reduction operation along the given axis operation to the current graph.
- [func reciprocal(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/reciprocal%28epsilon%29.md)
  Adds an element-wise reciprocal operation to the current graph.
- [func relu() -> BNNSGraph.Builder.Tensor<T>](./tensor/relu%28%29.md)
  Adds a Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func relu6() -> BNNSGraph.Builder.Tensor<T>](./tensor/relu6%28%29.md)
  Adds a Rectified Linear Unit 6 (ReLU6)  activation operation to the current graph.
- [func reshape(to: some BNNSGraph.Builder.OperationParameter<Int32>) -> BNNSGraph.Builder.Tensor<T>](./tensor/reshape%28to%29-5oniw.md)
  Adds a dynamic reshape operation to the current graph.
- [func reshape(to: [Int]) -> BNNSGraph.Builder.Tensor<T>](./tensor/reshape%28to%29-9stle.md)
  Adds a reshape operation to the current graph.
- [func rmsNorm(scale: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/rmsnorm%28scale,epsilon%29.md)
  Adds an RMS spatial normalization operation to the current graph.
- [func rnn(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>)](./tensor/rnn%28initialhiddenstates,inputhiddenweight,hiddenhiddenweight,bias,direction,activation,outputsequence%29.md)
  Adds an RNN operation to the current graph.
- [func round() -> BNNSGraph.Builder.Tensor<T>](./tensor/round%28%29.md)
  Adds an element-wise round operation to the current graph.
- [func rsqrt(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/rsqrt%28epsilon%29.md)
  Adds an element-wise rsqrt operation to the current graph.
- [func scaledTanh(alpha: Float, beta: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/scaledtanh%28alpha,beta%29.md)
  Adds a scaled tanh activation operation to the current graph.
- [func scatter(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode, axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/scatter%28updates,indices,mode,axis%29.md)
  Adds a scatter operation to the current graph.
- [func scatterAlongAxis(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode, axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/scatteralongaxis%28updates,indices,mode,axis%29.md)
  Adds a scatter-along-axis operation to the current graph
- [func scatterND(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode) -> BNNSGraph.Builder.Tensor<T>](./tensor/scatternd%28updates,indices,mode%29.md)
  Adds a scatter-nd operation to the current graph.
- [func select<U>(BNNSGraph.Builder.Tensor<U>, BNNSGraph.Builder.Tensor<U>) -> BNNSGraph.Builder.Tensor<U>](./tensor/select%28_,_%29-1fiqe.md)
  Adds a tensor-tensor select operation to the current graph.
- [func select<U>(BNNSGraph.Builder.Tensor<U>, any BNNSGraph.Builder.OperationParameter<U>) -> BNNSGraph.Builder.Tensor<U>](./tensor/select%28_,_%29-3ha1f.md)
  Adds a tensor-scalar select operation to the current graph.
- [func select<U>(any BNNSGraph.Builder.OperationParameter<U>, BNNSGraph.Builder.Tensor<U>) -> BNNSGraph.Builder.Tensor<U>](./tensor/select%28_,_%29-77itm.md)
  Adds a scalar-tensor select operation to the current graph.
- [func sigmoid() -> BNNSGraph.Builder.Tensor<T>](./tensor/sigmoid%28%29.md)
  Adds a sigmoid activation operation to the current graph.
- [func silu() -> BNNSGraph.Builder.Tensor<T>](./tensor/silu%28%29.md)
  Adds a Sigmoid Linear Unit (SiLU) activation operation to the current graph.
- [func sin() -> BNNSGraph.Builder.Tensor<T>](./tensor/sin%28%29.md)
  Adds an element-wise sin operation to the current graph.
- [func sinh() -> BNNSGraph.Builder.Tensor<T>](./tensor/sinh%28%29.md)
  Adds an element-wise sinh operation to the current graph.
- [func softmax(axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/softmax%28axis%29.md)
  Adds a softmax along the given axis operation to the current graph.
- [func softplus(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/softplus%28alpha%29.md)
  Adds a softplus activation operation to the current graph.
- [func softsign() -> BNNSGraph.Builder.Tensor<T>](./tensor/softsign%28%29.md)
  Adds a softsign activation operation to the current graph.
- [func sqrt() -> BNNSGraph.Builder.Tensor<T>](./tensor/sqrt%28%29.md)
  Adds an element-wise sqrt operation to the current graph.
- [func squeeze(axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/squeeze%28axis%29.md)
  Adds a squeeze operation in the graph.
- [func sum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/sum%28axes,keepdimensions%29.md)
  Adds a sum reduction operation along the given axis operation to the current graph.
- [func sumOfSquares(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](./tensor/sumofsquares%28axes,keepdimensions%29.md)
  Adds a sum-of-squares reduction operation along the given axis operation to the current graph.
- [func tan() -> BNNSGraph.Builder.Tensor<T>](./tensor/tan%28%29.md)
  Adds an element-wise tan operation to the current graph.
- [func tanh() -> BNNSGraph.Builder.Tensor<T>](./tensor/tanh%28%29.md)
  Adds an element-wise hyperbolic tangent operation to the current graph.
- [func tensorShape() -> BNNSGraph.Builder.Tensor<Int32>](./tensor/tensorshape%28%29.md)
  Adds a shape operation to the current graph.
- [func threshold(to: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/threshold%28to%29.md)
  Adds an element-wise round operation to the current graph.
- [func thresholdedReLU(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](./tensor/thresholdedrelu%28alpha%29.md)
  Adds a Thresholded Leaky Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func topK(Int, axis: Int, findLargest: Bool) -> (values: BNNSGraph.Builder.Tensor<T>, indices: BNNSGraph.Builder.Tensor<Int32>)](./tensor/topk%28_,axis,findlargest%29.md)
  Adds a top-k operation to the current graph.
- [func transpose(axes: [Int]) -> BNNSGraph.Builder.Tensor<T>](./tensor/transpose%28axes%29.md)
  Adds a transpose operation to the current graph.
- [func unsqueeze(axis: Int) -> BNNSGraph.Builder.Tensor<T>](./tensor/unsqueeze%28axis%29.md)
  Adds an unsqueeze operation in the graph.
### Subscripts
- [subscript(any BNNSGraph.Builder.SliceIndex...) -> BNNSGraph.Builder.Tensor<T>](./tensor/subscript%28_%29.md)
  Adds a slice operation to the current graph.
### Default Implementations
- [OperationParameter Implementations](./tensor/operationparameter-implementations.md)

## Relationships

### Conforms To
- [BNNSGraph.Builder.OperationParameter](./operationparameter.md)
- [BNNSGraph.TensorDescriptor](../tensordescriptor.md)
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Escapable](../../../Swift/escapable.md)

## See Also

### Building graphs in Swift
- [static func makeContext(options: BNNSGraph.CompileOptions, (inout BNNSGraph.Builder) -> [any BNNSGraph.TensorDescriptor]) throws -> BNNSGraph.Context](../makecontext%28options,_%29.md)
  Returns a new context that wraps a graph object that the given closure defines.
- [BNNSGraph.Builder](../builder.md)
  A structure thats provides a closure you can use to define the arguments and operations of a BNNS Graph.
- [Supporting real-time ML inference on the CPU](../../supporting-real-time-ml-inference-on-the-cpu.md)
  Add real-time digital signal processing to apps like Logic Pro X and GarageBand with the BNNS Graph API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor)*