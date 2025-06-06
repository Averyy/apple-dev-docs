# BNNS

**Framework**: Accelerate  
**Kind**: enum

An enumeration that acts as a namespace for Swift overlays to BNNS.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
enum BNNS
```

## Topics

### Base Classes
- [class Layer](bnns/layer.md)
  The base class for layer objects that wrap filters and manage deinitialization.
- [class UnaryLayer](bnns/unarylayer.md)
  The base class for layers that accept a single input.
- [class BinaryLayer](bnns/binarylayer.md)
  The base class for layers that accept two inputs.
### Classes
- [class ActivationLayer](bnns/activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [class BinaryArithmeticLayer](bnns/binaryarithmeticlayer.md)
  A layer object that wraps a binary arithmetic filter and manages its deinitialization.
- [class BroadcastMatrixMultiplyLayer](bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
- [class ConvolutionLayer](bnns/convolutionlayer.md)
  A layer object that wraps a convolution filter and manages its deinitialization.
- [class CropResizeLayer](bnns/cropresizelayer.md)
  A layer object that wraps a crop-resize filter and manages its deinitialization.
- [class DropoutLayer](bnns/dropoutlayer.md)
  A layer object that wraps a dropout filter and manages its deinitialization.
- [class EmbeddingLayer](bnns/embeddinglayer.md)
  A layer object that wraps an embedding filter and manages its deinitialization.
- [class FullyConnectedLayer](bnns/fullyconnectedlayer.md)
  A layer object that wraps a fully connected filter and manages its deinitialization.
- [class FusedConvolutionNormalizationLayer](bnns/fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [class FusedFullyConnectedNormalizationLayer](bnns/fusedfullyconnectednormalizationlayer.md)
  A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.
- [class FusedLayer](bnns/fusedlayer.md)
  The base class for fused convolution-normalization and fully connected-normalization layers.
- [class FusedParametersLayer](bnns/fusedparameterslayer.md)
  A layer object that wraps a fused layer and manages its deinitialization.
- [class GramLayer](bnns/gramlayer.md)
  A layer object that wraps a Gram matrix filter and manages its deinitialization.
- [class LossLayer](bnns/losslayer.md)
  A layer object that wraps a loss filter and manages its deinitialization.
- [class NormalizationLayer](bnns/normalizationlayer.md)
  A layer object that wraps a normalization filter and manages its deinitialization.
- [class PaddingLayer](bnns/paddinglayer.md)
  A layer object that wraps a padding filter and manages its deinitialization.
- [class PermuteLayer](bnns/permutelayer.md)
  A layer object that wraps a permute filter and manages its deinitialization.
- [class PoolingLayer](bnns/poolinglayer.md)
  A layer object that wraps a pooling filter and manages its deinitialization.
- [class RandomGenerator](bnns/randomgenerator.md)
  A random number generator.
- [class RandomGeneratorState](bnns/randomgeneratorstate.md)
  An opaque object that contains the state of a random number generator.
- [class ReductionLayer](bnns/reductionlayer.md)
  A layer object that wraps a reduction filter and manages its deinitialization.
- [class ResizeLayer](bnns/resizelayer.md)
  A layer object that wraps a resize filter and manages its deinitialization.
- [class TernaryArithmeticLayer](bnns/ternaryarithmeticlayer.md)
  A layer object that wraps a ternary arithmetic filter and manages its deinitialization.
- [class UnaryArithmeticLayer](bnns/unaryarithmeticlayer.md)
  A layer object that wraps a unary arithmetic filter and manages its deinitialization.
### Structures
- [struct AdamOptimizer](bnns/adamoptimizer.md)
  An optimizer that uses the Adam optimization algorithm.
- [struct AdamWOptimizer](bnns/adamwoptimizer.md)
  An optimizer that uses the AdamW optimization algorithm.
- [struct FusedBinaryArithmeticParameters](bnns/fusedbinaryarithmeticparameters.md)
  A structure that contains the parameters for a fused binary arithmetic layer.
- [struct FusedConvolutionParameters](bnns/fusedconvolutionparameters.md)
  A structure that contains the parameters for a fused convolution layer.
- [struct FusedDequantizationParameters](bnns/fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](bnns/fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.
- [struct FusedQuantizationParameters](bnns/fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedTernaryArithmeticParameters](bnns/fusedternaryarithmeticparameters.md)
  A structure that contains the parameters for a fused ternary arithmetic layer.
- [struct FusedUnaryArithmeticParameters](bnns/fusedunaryarithmeticparameters.md)
  A structure that contains the parameters for a fused unary arithmetic layer.
- [struct NearestNeighbors](bnns/nearestneighbors.md)
  A structure that calculates k-nearest neighbors.
- [struct Norm](bnns/norm.md)
  Constants that describe norm types.
- [struct RMSPropOptimizer](bnns/rmspropoptimizer.md)
  An optimizer that uses the root mean square propagation (RMSProp) optimization method.
- [struct RelationalOperator](bnns/relationaloperator.md)
  Constants that describe relational operations.
- [struct SGDMomentumOptimizer](bnns/sgdmomentumoptimizer.md)
  An optimizer that uses the stochastic gradient descent (SGD) with the momentum optimization method.
- [struct SparseParameters](bnns/sparseparameters.md)
  A data structure that provides a hint to the sparsity function.
### Type Methods
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:).md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:input:output:batchsize:filterparameters:).md)
  Applies the specified activation function.
- [static func applyInTopK(k: Int, input: BNNSNDArrayDescriptor, testIndices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyintopk(k:input:testindices:output:axis:batchsize:filterparameters:).md)
  Applies an in-top-k filter directly to an input.
- [static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](bnns/applymatrixmultiplication(inputa:transposed:inputb:transposed:output:alpha:workspace:filterparameters:).md)
  Performs a matrix multiplication operation directly on two input matrices.
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/applyreduction(_:input:output:weights:filterparameters:).md)
  Applies the specified reduction function.
- [static func applyTopK(k: Int, input: BNNSNDArrayDescriptor, bestValues: BNNSNDArrayDescriptor, bestIndices: BNNSNDArrayDescriptor, axis: Int, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applytopk(k:input:bestvalues:bestindices:axis:batchsize:filterparameters:).md)
  Applies a top-k filter directly to an input.
- [static func clip(to: ClosedRange<Float>, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/clip(to:input:output:).md)
  Clips the input tensor to a closed range and writes the result to the output tensor.
- [static func clipByGlobalNorm(threshold: Float, inputs: [BNNSNDArrayDescriptor], outputs: [BNNSNDArrayDescriptor], globalNorm: Float) throws](bnns/clipbyglobalnorm(threshold:inputs:outputs:globalnorm:).md)
  Clips the input tensors to a global Euclidean norm and writes the result to the output tensors.
- [static func clipByNorm(threshold: Float, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](bnns/clipbynorm(threshold:input:output:axes:).md)
  Clips the input tensor to a Euclidean norm and writes the result to the output tensor.
- [static func compare(BNNSNDArrayDescriptor, BNNSNDArrayDescriptor, using: BNNS.RelationalOperator, output: BNNSNDArrayDescriptor) throws](bnns/compare(_:_:using:output:).md)
  Performs an elementwise comparison of two array descriptors using the specified relational operator.
- [static func computeNorm(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?) throws](bnns/computenorm(input:output:axes:).md)
  Computes the Euclidean norm and writes the result to the output tensor.
- [static func computeNormBackward(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axes: [Int]?, outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor) throws](bnns/computenormbackward(input:output:axes:outputgradient:generatinginputgradient:).md)
  Backpropogates gradients for the compute norm function.
- [static func copy(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/copy(_:to:filterparameters:).md)
  Copies the contents of an n-dimensional array descriptor to another descriptor of the same shape.
- [static func copyBandPart(BNNSNDArrayDescriptor, to: BNNSNDArrayDescriptor, lowerBandCount: Int?, upperBandCount: Int?, filterParameters: BNNSFilterParameters?) throws](bnns/copybandpart(_:to:lowerbandcount:upperbandcount:filterparameters:).md)
  Copies the specified subdiagonals and superdiagonals of a matrix, and sets other elements to zero.
- [static func dequantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/dequantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Dequantizes the input tensor and writes the result to the output tensor.
- [static func gather(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, filterParameters: BNNSFilterParameters?) throws](bnns/gather(input:indices:output:axis:filterparameters:).md)
  Gathers the elements of a tensor along a single axis.
- [static func gatherND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/gathernd(input:indices:output:filterparameters:).md)
  Gathers the slices of a tensor.
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](bnns/matrixmultiplicationworkspacesize(inputa:transposed:inputb:transposed:output:alpha:filterparameters:).md)
  Returns the workspace size that a matrix multiply operation requires.
- [static func quantize(batchSize: Int, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int?, scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/quantize(batchsize:input:output:axis:scale:bias:filterparameters:).md)
  Quantizes the input tensor and writes the result to the output tensor.
- [static func scatter(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, filterParameters: BNNSFilterParameters?) throws](bnns/scatter(input:indices:output:axis:filterparameters:).md)
- [static func scatter(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters?) throws](bnns/scatter(input:indices:output:axis:reductionfunction:filterparameters:).md)
  Scatters the elements of a tensor along a single axis.
- [static func scatterND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/scatternd(input:indices:output:filterparameters:).md)
- [static func scatterND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters?) throws](bnns/scatternd(input:indices:output:reductionfunction:filterparameters:).md)
  Scatters the slices of a tensor.
- [static func shuffle(BNNS.ShuffleType, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/shuffle(_:input:output:filterparameters:).md)
  Rearranges elements in a tensor according to shuffle type.
- [static func tile(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/tile(input:output:filterparameters:).md)
  Generates an output tensor by tiling an input tensor multiple times.
- [static func tileBackward(outputGradient: BNNSNDArrayDescriptor, generatingInputGradient: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/tilebackward(outputgradient:generatinginputgradient:filterparameters:).md)
  Applies a tile filter backward to generate an input gradient.
- [static func transpose(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, firstTransposeAxis: Int, secondTransposeAxis: Int, filterParameters: BNNSFilterParameters?) throws](bnns/transpose(input:output:firsttransposeaxis:secondtransposeaxis:filterparameters:).md)
  Transposes a tensor by swapping two of its dimensions.
### Enumerations
- [BNNS.ActivationFunction](bnns/activationfunction.md)
  Constants that describe activation functions.
- [BNNS.ArithmeticBinaryFunction](bnns/arithmeticbinaryfunction.md)
  Constants that describe binary arithmetic functions.
- [BNNS.ArithmeticTernaryFunction](bnns/arithmeticternaryfunction.md)
  Constants that describe ternary arithmetic functions.
- [BNNS.ArithmeticUnaryFunction](bnns/arithmeticunaryfunction.md)
  Constants that describe unary arithmetic functions.
- [BNNS.ConvolutionPadding](bnns/convolutionpadding.md)
  Constants that describe convolution padding modes.
- [BNNS.ConvolutionType](bnns/convolutiontype.md)
  Constants that describe convolution types.
- [BNNS.DataLayout](bnns/datalayout.md)
  Constants that describe the data layout of an n-dimensional array descriptor shape.
- [BNNS.DescriptorType](bnns/descriptortype.md)
  Constants that describe the input and output types of an arithmetic operation.
- [BNNS.Error](bnns/error.md)
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.
- [BNNS.InterpolationMethod](bnns/interpolationmethod.md)
  Constants that specify interpolation methods for resize operations.
- [BNNS.LearningPhase](bnns/learningphase.md)
  Constants that describe the learning phase of a normalization operation.
- [BNNS.LossFunction](bnns/lossfunction.md)
  Constants that describe loss functions.
- [BNNS.LossReduction](bnns/lossreduction.md)
  An enumeration that describes loss reduction functions.
- [BNNS.NormalizationType](bnns/normalizationtype.md)
  Constants that describe normalization types.
- [BNNS.PaddingMode](bnns/paddingmode.md)
  Constants that define padding modes.
- [BNNS.PoolingType](bnns/poolingtype.md)
  Constants that describe pooling types.
- [BNNS.RandomGeneratorMethod](bnns/randomgeneratormethod.md)
  Constants that describe random number generation methods.
- [BNNS.ReductionFunction](bnns/reductionfunction.md)
  Constants that describe reduction functions.
- [BNNS.Shape](bnns/shape.md)
  Constants that describe the size and data layout of an n-dimensional array descriptor.
- [BNNS.ShuffleType](bnns/shuffletype.md)
  Constants that specify a shuffle type.
- [BNNS.SparseLayout](bnns/sparselayout.md)
  Constants that specify standardized sparse layouts that BNNS can convert to opaque.
- [BNNS.SparsityType](bnns/sparsitytype.md)
  Constants that specify patterns in the sparsity.

## See Also

- [enum BNNSGraph](bnnsgraph.md)
  An enumeration that acts as a namespace for the Swift overlays to BNNS Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns)*