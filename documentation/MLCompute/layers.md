# Layers

**Framework**: ML Compute

Create and inspect layers that encapsulate operations and configuration details to receive, process, and output tensors.

## Topics

### Activation Layers
- [class MLCActivationLayer](mlcactivationlayer.md)
  A layer that applies an activation function to the source tensor and produces an output.
- [class MLCMultiheadAttentionLayer](mlcmultiheadattentionlayer.md)
  A multihead, scaled dot-product attention layer that attends to one or more entries in the input key-value pairs.
- [class MLCSoftmaxLayer](mlcsoftmaxlayer.md)
  A layer that outputs a probability distribution as attention weights.
### Math Layers
- [class MLCArithmeticLayer](mlcarithmeticlayer.md)
  A layer that performs an arithmetic operation.
- [class MLCReductionLayer](mlcreductionlayer.md)
  A layer that reduces tensor values across a specific dimension to a scalar value.
- [class MLCMatMulLayer](mlcmatmullayer.md)
  A layer that multiplies matrices.
- [class MLCFullyConnectedLayer](mlcfullyconnectedlayer.md)
  A layer that connects each input to each output within its layer.
- [class MLCGramMatrixLayer](mlcgrammatrixlayer.md)
  A layer that computes the uncentered cross-correlation values between the spacial planes of each feature channel of a tensor.
- [class MLCComparisonLayer](mlccomparisonlayer.md)
  A layer that performs elementwise comparison of two tensors.
### Transformation Layers
- [class MLCTransposeLayer](mlctransposelayer.md)
  A layer that permutes the dimensions you specify.
- [class MLCConcatenationLayer](mlcconcatenationlayer.md)
  A layer that combines tensors into a single tensor.
- [class MLCReshapeLayer](mlcreshapelayer.md)
  A layer that reshapes a tensor with the shape you specify.
- [class MLCSliceLayer](mlcslicelayer.md)
  A layer that extracts a slice from a tensor.
- [class MLCSplitLayer](mlcsplitlayer.md)
  A layer that splits a tensor value into a list of subtensors.
- [class MLCPaddingLayer](mlcpaddinglayer.md)
  A layer that pads a tensor with the padding sizes you specify.
- [class MLCScatterLayer](mlcscatterlayer.md)
  A layer that updates the output at an index you specify.
- [class MLCSelectionLayer](mlcselectionlayer.md)
  A layer for selecting elements from two tensors.
- [class MLCGatherLayer](mlcgatherlayer.md)
  A layer that fetches data at the locations you specify.
### Normalization Layers
- [class MLCLayerNormalizationLayer](mlclayernormalizationlayer.md)
  A layer that applies layer normalization over inputs.
- [class MLCBatchNormalizationLayer](mlcbatchnormalizationlayer.md)
  A layer that normalizes a batch of inputs.
- [class MLCGroupNormalizationLayer](mlcgroupnormalizationlayer.md)
  A layer that divides the channels into groups for normalization.
- [class MLCInstanceNormalizationLayer](mlcinstancenormalizationlayer.md)
  A layer that normalizes all features of one channel.
- [class MLCDropoutLayer](mlcdropoutlayer.md)
  A layer that deactivates neurons randomly to avoid overfitting.
### Convolution and Recurrent Layers
- [class MLCConvolutionLayer](mlcconvolutionlayer.md)
  A layer that applies a convolution over a signal.
- [class MLCLSTMLayer](mlclstmlayer.md)
  A layer that represents long short-term memory (LSTM) networks.
- [class MLCPoolingLayer](mlcpoolinglayer.md)
  A layer that summarizes the average presence of a feature.
- [class MLCUpsampleLayer](mlcupsamplelayer.md)
  A layer that applies upsampling with the shape you specify.
- [class MLCEmbeddingLayer](mlcembeddinglayer.md)
  A layer that stores a word embedding.
### Loss Layers
- [class MLCLossLayer](mlclosslayer.md)
  A layer that estimates the inaccuracies of the model to reduce the loss on the next evaluation.
- [class MLCYOLOLossLayer](mlcyololosslayer.md)
  A layer that estimates loss for the YOLO algorithm.
### Base Layer
- [class MLCLayer](mlclayer.md)
  The base class for all framework layers.
### Supporting Types
- [enum MLCPaddingPolicy](mlcpaddingpolicy-3hic8.md)
  A padding policy that you specify for a convolution or pooling layer.
- [enum MLCPaddingType](mlcpaddingtype.md)
  A padding type that you specify for a padding layer.

## See Also

- [class MLCTensor](mlctensor.md)
  The data object you use throughout the framework.
- [class MLCPlatform](mlcplatform.md)
  A utility class for setting global properties in the framework.
- [Training and Validation](training-and-validation.md)
  Create, train, and validate a graph to produce acceptable prediction results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/layers)*