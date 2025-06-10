# BNNSGraph.Builder.Tensor

**Framework**: Accelerate  
**Kind**: struct

A structure that represents an abstract handle to a tensor that you use within a `BNNSGraph.makeContext` closure.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Tensor<T> where T : BNNSScalar
```

## Topics

### Operators
- [static func .! (BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'.!(_:).md)
  Adds an element-wise logical not operation to the current graph.
- [static func .!= (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'.!=(_:_:).md)
  Adds an element-wise inequality operation to the current graph.
- [static func .& (BNNSGraph.Builder.Tensor<Bool>, BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'.&(_:_:).md)
  Adds an element-wise logical and operation to the current graph.
- [static func .== (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'.==(_:_:).md)
  Adds an element-wise equality operation to the current graph.
- [static func .| (BNNSGraph.Builder.Tensor<Bool>, BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'._(_:_:)-171l2.md)
  Adds an element-wise logical or operation to the current graph.
- [static func .< (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'._(_:_:)-6sgl6.md)
  Adds an element-wise less than comparison operation to the current graph.
- [static func .^ (BNNSGraph.Builder.Tensor<Bool>, BNNSGraph.Builder.Tensor<Bool>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'._(_:_:)-6soc4.md)
  Adds an element-wise logical xor operation to the current graph.
- [static func .> (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'._(_:_:)-9vd51.md)
  Adds an element-wise greater than comparison operation to the current graph.
- [static func .<= (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'._=(_:_:)-20vpj.md)
  Adds an element-wise less than or equal comparison operation to the current graph.
- [static func .>= (BNNSGraph.Builder.Tensor<T>, BNNSGraph.Builder.Tensor<T>) -> BNNSGraph.Builder.Tensor<Bool>](bnnsgraph/builder/tensor/'._=(_:_:)-6gvvh.md)
  Adds an element-wise greater than or equal comparison operation to the current graph.
### Instance Properties
- [var dataType: BNNSDataType?](bnnsgraph/builder/tensor/datatype.md)
  The data type of the tensor.
- [var description: String](bnnsgraph/builder/tensor/description.md)
  A textual representation of this instance.
- [var rank: Int?](bnnsgraph/builder/tensor/rank.md)
  The rank of the tensor.
- [var shape: [Int]?](bnnsgraph/builder/tensor/shape.md)
  The shape of the tensor.
- [var stride: [Int]?](bnnsgraph/builder/tensor/stride.md)
  The stride of the tensor.
### Instance Methods
- [func abs() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/abs.md)
  Adds an element-wise absolute operation to the current graph.
- [func acos() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/acos.md)
  Adds an element-wise acos operation to the current graph.
- [func acosh() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/acosh.md)
  Adds an element-wise atan operation to the current graph.
- [func argMax(axis: Int, keepDimension: Bool) -> BNNSGraph.Builder.Tensor<Int32>](bnnsgraph/builder/tensor/argmax(axis:keepdimension:).md)
  Adds an argmax operation to the current graph.
- [func argMin(axis: Int, keepDimension: Bool) -> BNNSGraph.Builder.Tensor<Int32>](bnnsgraph/builder/tensor/argmin(axis:keepdimension:).md)
  Adds an argmin operation to the current graph.
- [func argSort(axis: Int, sortOrder: BNNSGraph.Builder.SortOrder) -> BNNSGraph.Builder.Tensor<Int32>](bnnsgraph/builder/tensor/argsort(axis:sortorder:).md)
  Adds an argsort operation to the current graph.
- [func asin() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/asin.md)
  Adds an element-wise asin operation to the current graph.
- [func asinh() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/asinh.md)
  Adds an element-wise asinh operation to the current graph.
- [func atan() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/atan.md)
  Adds an element-wise atan operation to the current graph.
- [func atanh() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/atanh.md)
  Adds an element-wise atanh operation to the current graph.
- [func batchNorm(mean: some BNNSGraph.Builder.OperationParameter<T>, variance: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/batchnorm(mean:variance:epsilon:).md)
  Adds a batch normalization operation to the current graph.
- [func batchNorm(mean: some BNNSGraph.Builder.OperationParameter<T>, variance: some BNNSGraph.Builder.OperationParameter<T>, weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/batchnorm(mean:variance:weight:bias:epsilon:).md)
  Adds a batch normalization operation to the current graph.
- [func bidirectionalLSTM(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, initialCellStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, inputHiddenWeightBack: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeightBack: BNNSGraph.Builder.Tensor<T>, biasBack: BNNSGraph.Builder.Tensor<T>, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, cellActivation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>, memoryStates: BNNSGraph.Builder.Tensor<T>)](bnnsgraph/builder/tensor/bidirectionallstm(initialhiddenstates:initialcellstates:inputhiddenweight:hiddenhiddenweight:bias:inputhiddenweightback:hiddenhiddenweightback:biasback:activation:recurrentactivation:cellactivation:outputsequence:).md)
  Adds a bidirectional LSTM operation to the current graph.
- [func cast<U>(to: U.Type) -> BNNSGraph.Builder.Tensor<U>](bnnsgraph/builder/tensor/cast(to:).md)
  Adds a cast operation to the current graph.
- [func ceil() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/ceil.md)
  Adds an element-wise ceiling operation to the current graph.
- [func channelNorm(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/channelnorm(epsilon:).md)
  Adds a channel normalization operation to the current graph.
- [func channelNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/channelnorm(weight:bias:epsilon:).md)
  Adds a channel normalization operation to the current graph.
- [func clampedReLU(alpha: Float, beta: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/clampedrelu(alpha:beta:).md)
  Adds a Clamped Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func clip(to: ClosedRange<Float>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/clip(to:).md)
  Adds an element-wise clip operation to the current graph.
- [func conv(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], bias: some BNNSGraph.Builder.OperationParameter<T>, padding: BNNSGraph.Builder.ConvolutionPadding, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/conv(weight:strides:bias:padding:dilations:groupcount:).md)
  Adds a convolution operation to the current graph.
- [func conv(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], padding: BNNSGraph.Builder.ConvolutionPadding, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/conv(weight:strides:padding:dilations:groupcount:).md)
  Adds a convolution operation to the current graph.
- [func convTranspose(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], bias: some BNNSGraph.Builder.OperationParameter<T>, padding: BNNSGraph.Builder.ConvolutionPadding, outputPaddingValues: [Int]?, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/convtranspose(weight:strides:bias:padding:outputpaddingvalues:dilations:groupcount:).md)
  Adds a transposed convolution operation to the current graph.
- [func convTranspose(weight: some BNNSGraph.Builder.OperationParameter<T>, strides: [Int], padding: BNNSGraph.Builder.ConvolutionPadding, outputPaddingValues: [Int]?, dilations: [Int]?, groupCount: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/convtranspose(weight:strides:padding:outputpaddingvalues:dilations:groupcount:).md)
  Adds a transposed convolution operation to the current graph.
- [func cos() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/cos.md)
  Adds an element-wise cos operation to the current graph.
- [func cosh() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/cosh.md)
  Adds an element-wise cosh operation to the current graph.
- [func cumulativeSum(axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/cumulativesum(axis:).md)
  Adds a cumulative sum operation to the the graph.
- [func elu(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/elu(alpha:).md)
  Adds an Exponential Linear Unit (ELU) activation operation to the current graph.
- [func erf() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/erf.md)
  Adds an Error Function (erf) activation operation to the current graph.
- [func exp() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/exp.md)
  Adds an element-wise exp operation to the current graph.
- [func exp2() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/exp2.md)
  Adds an element-wise exp operation to the current graph.
- [func floor() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/floor.md)
  Adds an element-wise floor operation to the current graph.
- [func fma(y: some BNNSGraph.Builder.OperationParameter<T>, z: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/fma(y:z:).md)
  Adds an element-wise fused multiply-add operation to the current graph.
- [func gather(indices: some BNNSGraph.Builder.OperationParameter<Int32>, axis: Int, batchDimensionCount: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/gather(indices:axis:batchdimensioncount:).md)
  Adds a gather operation to the current graph.
- [func gatherAlongAxis(indices: some BNNSGraph.Builder.OperationParameter<Int32>, axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/gatheralongaxis(indices:axis:).md)
  Adds a gather-along-axis operation to the current graph.
- [func gatherND(indices: some BNNSGraph.Builder.OperationParameter<Int32>, batchDimensionCount: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/gathernd(indices:batchdimensioncount:).md)
  Adds a gather-nd operation to the current graph.
- [func gelu() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/gelu.md)
  Adds a Gaussian Error Linear Unit (GELU) activation operation to the current graph.
- [func geluSigmoidApproximation() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/gelusigmoidapproximation.md)
  Adds a Gaussian Error Linear Unit (GELU) sigmoid approximation activation operation to the current graph.
- [func geluTanhApproximation() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/gelutanhapproximation.md)
  Adds a Gaussian Error Linear Unit (GELU) tanh approximation activation operation to the current graph.
- [func gru(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, inputBias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, applyResetGateAfterMatMul: Bool, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>)](bnnsgraph/builder/tensor/gru(initialhiddenstates:inputhiddenweight:hiddenhiddenweight:bias:inputbias:direction:activation:recurrentactivation:applyresetgateaftermatmul:outputsequence:).md)
  Adds a GRU operation to the current graph.
- [func hardSigmoid(alpha: Float, beta: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/hardsigmoid(alpha:beta:).md)
  Adds a hard sigmoid activation operation to the current graph.
- [func hardSwish() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/hardswish.md)
  Adds a hard swish activation operation to the current graph.
- [func instanceNorm(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/instancenorm(epsilon:).md)
  Adds a instance normalization operation to the current graph.
- [func instanceNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/instancenorm(weight:bias:epsilon:).md)
  Adds a instance normalization operation to the current graph.
- [func l1Norm(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/l1norm(axes:keepdimensions:).md)
  Adds a sum-of-absolutes reduction operation along the given axis operation to the current graph.
- [func l2Norm(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/l2norm(axes:keepdimensions:).md)
  Adds a Euclidean-norm reduction operation along the given axis operation to the current graph.
- [func l2Norm(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/l2norm(epsilon:).md)
  Adds an L2 spatial normalization operation to the current graph.
- [func layerNorm(axes: [Int], epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/layernorm(axes:epsilon:).md)
  Adds a layer normalization operation to the current graph.
- [func layerNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, axes: [Int], epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/layernorm(weight:bias:axes:epsilon:).md)
  Adds a layer normalization operation to the current graph.
- [func leakyReLU(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/leakyrelu(alpha:).md)
  Adds a Leaky Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func linear(weight: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/linear(weight:).md)
  Adds a linear transformation operation to the current graph.
- [func linear(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/linear(weight:bias:).md)
  Adds a linear transformation operation to the current graph.
- [func log(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/log(epsilon:).md)
  Adds an element-wise log operation to the current graph.
- [func logSoftmax(axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/logsoftmax(axis:).md)
  Adds a log-softmax along the given axis operation to the current graph.
- [func logSum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/logsum(axes:keepdimensions:).md)
  Adds a log-sum reduction operation along the given axis operation to the current graph.
- [func logSumExp(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/logsumexp(axes:keepdimensions:).md)
  Adds a log-sum-exp reduction operation along the given axis operation to the current graph.
- [func lstm(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, initialCellStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, cellActivation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>, memoryStates: BNNSGraph.Builder.Tensor<T>)](bnnsgraph/builder/tensor/lstm(initialhiddenstates:initialcellstates:inputhiddenweight:hiddenhiddenweight:bias:direction:activation:recurrentactivation:cellactivation:outputsequence:).md)
  Adds an LSTM operation to the current graph.
- [func matmul(transpose: Bool, other: some BNNSGraph.Builder.OperationParameter<T>, transposeOther: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/matmul(transpose:other:transposeother:).md)
  Adds a matrix-matrix multiplication operation to the current graph.
- [func matmul(transpose: Bool, other: some BNNSGraph.Builder.OperationParameter<T>, transposeOther: Bool, bias: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/matmul(transpose:other:transposeother:bias:).md)
  Adds a matrix-matrix multiplication operation to the current graph.
- [func max(y: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/max(y:).md)
  Adds an element-wise maximum operation to the current graph.
- [func maximum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/maximum(axes:keepdimensions:).md)
  Adds a maximum reduction operation along the given axis operation to the current graph.
- [func mean(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/mean(axes:keepdimensions:).md)
  Adds a mean reduction operation along the given axis operation to the current graph.
- [func min(y: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/min(y:).md)
  Adds an element-wise minimum operation to the current graph.
- [func minimum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/minimum(axes:keepdimensions:).md)
  Adds a minimum reduction operation along the given axis operation to the current graph.
- [func pad(BNNSGraph.Builder.Padding, padding: [Int]) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/pad(_:padding:).md)
  Adds a padding operation to the graph
- [func pooling(BNNSGraph.Builder.PoolingFunction, kernelSize: [Int], strides: [Int], padding: BNNSGraph.Builder.PoolingPadding, ceilingMode: BNNSGraph.Builder.CeilingMode) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/pooling(_:kernelsize:strides:padding:ceilingmode:).md)
  Adds a pooling operation to the current graph.
- [func pow(y: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/pow(y:).md)
  Adds an element-wise power operation to the current graph.
- [func prelu(alpha: [Float]) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/prelu(alpha:).md)
  Adds a Parametric ReLU (PReLU) activation operation to the current graph.
- [func product(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/product(axes:keepdimensions:).md)
  Adds a product reduction operation along the given axis operation to the current graph.
- [func reciprocal(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/reciprocal(epsilon:).md)
  Adds an element-wise reciprocal operation to the current graph.
- [func relu() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/relu.md)
  Adds a Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func relu6() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/relu6.md)
  Adds a Rectified Linear Unit 6 (ReLU6)  activation operation to the current graph.
- [func reshape(to: some BNNSGraph.Builder.OperationParameter<Int32>) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/reshape(to:)-5oniw.md)
  Adds a dynamic reshape operation to the current graph.
- [func reshape(to: [Int]) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/reshape(to:)-9stle.md)
  Adds a reshape operation to the current graph.
- [func rmsNorm(scale: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/rmsnorm(scale:epsilon:).md)
  Adds an RMS spatial normalization operation to the current graph.
- [func rnn(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>)](bnnsgraph/builder/tensor/rnn(initialhiddenstates:inputhiddenweight:hiddenhiddenweight:bias:direction:activation:outputsequence:).md)
  Adds an RNN operation to the current graph.
- [func round() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/round.md)
  Adds an element-wise round operation to the current graph.
- [func rsqrt(epsilon: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/rsqrt(epsilon:).md)
  Adds an element-wise rsqrt operation to the current graph.
- [func scaledTanh(alpha: Float, beta: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/scaledtanh(alpha:beta:).md)
  Adds a scaled tanh activation operation to the current graph.
- [func scatter(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode, axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/scatter(updates:indices:mode:axis:).md)
  Adds a scatter operation to the current graph.
- [func scatterAlongAxis(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode, axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/scatteralongaxis(updates:indices:mode:axis:).md)
  Adds a scatter-along-axis operation to the current graph
- [func scatterND(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/scatternd(updates:indices:mode:).md)
  Adds a scatter-nd operation to the current graph.
- [func sigmoid() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/sigmoid.md)
  Adds a sigmoid activation operation to the current graph.
- [func silu() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/silu.md)
  Adds a Sigmoid Linear Unit (SiLU) activation operation to the current graph.
- [func sin() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/sin.md)
  Adds an element-wise sin operation to the current graph.
- [func sinh() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/sinh.md)
  Adds an element-wise sinh operation to the current graph.
- [func softmax(axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/softmax(axis:).md)
  Adds a softmax along the given axis operation to the current graph.
- [func softplus(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/softplus(alpha:).md)
  Adds a softplus activation operation to the current graph.
- [func softsign() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/softsign.md)
  Adds a softsign activation operation to the current graph.
- [func sqrt() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/sqrt.md)
  Adds an element-wise sqrt operation to the current graph.
- [func squeeze(axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/squeeze(axis:).md)
  Adds a squeeze operation in the graph.
- [func sum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/sum(axes:keepdimensions:).md)
  Adds a sum reduction operation along the given axis operation to the current graph.
- [func sumOfSquares(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/sumofsquares(axes:keepdimensions:).md)
  Adds a sum-of-squares reduction operation along the given axis operation to the current graph.
- [func tan() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/tan.md)
  Adds an element-wise tan operation to the current graph.
- [func tanh() -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/tanh.md)
  Adds an element-wise hyperbolic tangent operation to the current graph.
- [func tensorShape() -> BNNSGraph.Builder.Tensor<Int32>](bnnsgraph/builder/tensor/tensorshape.md)
  Adds a shape operation to the current graph.
- [func threshold(to: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/threshold(to:).md)
  Adds an element-wise round operation to the current graph.
- [func thresholdedReLU(alpha: Float) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/thresholdedrelu(alpha:).md)
  Adds a Thresholded Leaky Rectified Linear Unit (ReLU) activation operation to the current graph.
- [func topK(Int, axis: Int, findLargest: Bool) -> (values: BNNSGraph.Builder.Tensor<T>, indices: BNNSGraph.Builder.Tensor<Int32>)](bnnsgraph/builder/tensor/topk(_:axis:findlargest:).md)
  Adds a top-k operation to the current graph.
- [func transpose(axes: [Int]) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/transpose(axes:).md)
  Adds a transpose operation to the current graph.
- [func unsqueeze(axis: Int) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/unsqueeze(axis:).md)
  Adds an unsqueeze operation in the graph.
### Subscripts
- [subscript(any BNNSGraph.Builder.SliceIndex...) -> BNNSGraph.Builder.Tensor<T>](bnnsgraph/builder/tensor/subscript(_:).md)
  Adds a slice operation to the current graph.
### Default Implementations
- [OperationParameter Implementations](bnnsgraph/builder/tensor/operationparameter-implementations.md)

## Relationships

### Conforms To
- [BNNSGraph.Builder.OperationParameter](bnnsgraph/builder/operationparameter.md)
- [BNNSGraph.TensorDescriptor](bnnsgraph/tensordescriptor.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [static func makeContext(options: BNNSGraph.CompileOptions, (inout BNNSGraph.Builder) -> [any BNNSGraph.TensorDescriptor]) throws -> BNNSGraph.Context](bnnsgraph/makecontext(options:_:).md)
  Returns a new context that wraps a graph object that the given closure defines.
- [BNNSGraph.Builder](bnnsgraph/builder.md)
  A structure thats provides a closure you can use to define the arguments and operations of a BNNS Graph.
- [Supporting real-time ML inference on the CPU](supporting-real-time-ml-inference-on-the-cpu.md)
  Add real-time digital signal processing to apps like Logic Pro X and GarageBand with the BNNS Graph API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor)*