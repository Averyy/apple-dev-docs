# Objects that Simplify the Creation of Neural Networks

**Framework**: Metal Performance Shaders

Simplify the creation of neural networks using networks of filter, image, and state nodes.

#### Overview

Graphs in Metal Performance Shaders offer a higher level graph API, intended to simplify the creation of neural networks. The graph is a network of [`MPSNNFilterNode`](mpsnnfilternode.md), [`MPSNNImageNode`](mpsnnimagenode.md) and [`MPSNNStateNode`](mpsnnstatenode.md) objects.

- [`MPSNNImageNode`](mpsnnimagenode.md) represents [`MPSImage`](mpsimage.md) or [`MPSTemporaryImage`](mpstemporaryimage.md) objects
- [`MPSNNFilterNode`](mpsnnfilternode.md) represents [`MPSCNNKernel`](mpscnnkernel.md) objects—each of the lower level [`MPSCNNKernel`](mpscnnkernel.md) subclasses has an associated object that is a subclass of the [`MPSNNFilterNode`](mpsnnfilternode.md)
- [`MPSNNStateNode`](mpsnnstatenode.md) represents [`MPSState`](mpsstate.md) objects

## Topics

### Neural Network Graphs
- [class MPSNNGraph](mpsnngraph.md)
  An optimized representation of a graph of neural network image and filter nodes.
- [class MPSNNImageNode](mpsnnimagenode.md)
  A placeholder node denoting the position of a neural network image in a graph.
- [protocol MPSHandle](mpshandle.md)
  The protocol that provides resource identification.
### Arithmetic Layer Nodes
- [class MPSNNAdditionNode](mpsnnadditionnode.md)
  A representation of an addition operator.
- [class MPSNNAdditionGradientNode](mpsnnadditiongradientnode.md)
  A representation of a gradient addition operator.
- [class MPSNNSubtractionNode](mpsnnsubtractionnode.md)
  A representation of an subtraction operator.
- [class MPSNNSubtractionGradientNode](mpsnnsubtractiongradientnode.md)
  A representation of a gradient subtraction operator.
- [class MPSNNMultiplicationNode](mpsnnmultiplicationnode.md)
  A representation of a multiplication operator.
- [class MPSNNMultiplicationGradientNode](mpsnnmultiplicationgradientnode.md)
  A representation of a gradient multiplication operator.
- [class MPSNNDivisionNode](mpsnndivisionnode.md)
  A representation of a division operator.
- [class MPSNNBinaryArithmeticNode](mpsnnbinaryarithmeticnode.md)
  Virtual base class for basic arithmetic nodes.
- [class MPSNNArithmeticGradientNode](mpsnnarithmeticgradientnode.md)
  A representation of the base class for gradient arithmetic operators.
- [class MPSNNArithmeticGradientStateNode](mpsnnarithmeticgradientstatenode.md)
  A representation of the clamp mask used by gradient arithmetic operators.
### Convolution Layer Nodes
- [class MPSCNNBinaryConvolutionNode](mpscnnbinaryconvolutionnode.md)
  A representation of a convolution kernel with binary weights and an input image using binary approximations.
- [class MPSCNNConvolutionNode](mpscnnconvolutionnode.md)
  A representation of a convolution kernel.
- [class MPSCNNConvolutionTransposeNode](mpscnnconvolutiontransposenode.md)
  A representation of a transposed convolution.
- [class MPSCNNConvolutionGradientNode](mpscnnconvolutiongradientnode.md)
  A representation of a gradient convolution kernel.
- [class MPSCNNConvolutionGradientStateNode](mpscnnconvolutiongradientstatenode.md)
  A representation of a gradient convolution state.
- [class MPSCNNCrossChannelNormalizationGradientNode](mpscnncrosschannelnormalizationgradientnode.md)
  A representation of a gradient normalization kernel applied across feature channels.
### Pooling Layer Nodes
- [class MPSCNNPoolingAverageNode](mpscnnpoolingaveragenode.md)
  A representation of an average pooling filter.
- [class MPSCNNDilatedPoolingMaxNode](mpscnndilatedpoolingmaxnode.md)
  A representation of a dilated max pooling filter.
- [class MPSCNNPoolingL2NormNode](mpscnnpoolingl2normnode.md)
  A representation of a L2-norm pooling filter.
- [class MPSCNNPoolingMaxNode](mpscnnpoolingmaxnode.md)
  A representation of a max pooling filter.
- [class MPSCNNPoolingNode](mpscnnpoolingnode.md)
  A representation of a MPS CNN pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradientNode](mpscnndilatedpoolingmaxgradientnode.md)
  A representation of a gradient dilated max pooling filter.
- [class MPSCNNPoolingAverageGradientNode](mpscnnpoolingaveragegradientnode.md)
  A representation of a gradient average pooling filter.
- [class MPSCNNPoolingGradientNode](mpscnnpoolinggradientnode.md)
  A representation of a gradient pooling kernel.
- [class MPSCNNPoolingL2NormGradientNode](mpscnnpoolingl2normgradientnode.md)
  A representation of a gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradientNode](mpscnnpoolingmaxgradientnode.md)
  A representation of a gradient max pooling filter.
### Fully Connected Layer Nodes
- [class MPSCNNBinaryFullyConnectedNode](mpscnnbinaryfullyconnectednode.md)
  A representation of a fully connected convolution layer with binary weights and optionally binarized input image.
- [class MPSCNNFullyConnectedNode](mpscnnfullyconnectednode.md)
  A representation of a fully connected convolution layer, also known as an inner product layer.
### Neuron Layer Nodes
- [class MPSCNNNeuronAbsoluteNode](mpscnnneuronabsolutenode.md)
  A representation of an absolute neuron filter.
- [class MPSCNNNeuronELUNode](mpscnnneuronelunode.md)
  A representation of a parametric ELU neuron filter.
- [class MPSCNNNeuronHardSigmoidNode](mpscnnneuronhardsigmoidnode.md)
  A representation of a hard sigmoid neuron filter.
- [class MPSCNNNeuronLinearNode](mpscnnneuronlinearnode.md)
  A representation of a linear neuron filter.
- [class MPSCNNNeuronPReLUNode](mpscnnneuronprelunode.md)
  A representation a PReLU neuron filter.
- [class MPSCNNNeuronReLUNNode](mpscnnneuronrelunnode.md)
  A representation a ReLUN neuron filter.
- [class MPSCNNNeuronReLUNode](mpscnnneuronrelunode.md)
  A representation a ReLU neuron filter.
- [class MPSCNNNeuronSigmoidNode](mpscnnneuronsigmoidnode.md)
  A representation of a sigmoid neuron filter.
- [class MPSCNNNeuronSoftPlusNode](mpscnnneuronsoftplusnode.md)
  A representation of a parametric softplus neuron filter.
- [class MPSCNNNeuronSoftSignNode](mpscnnneuronsoftsignnode.md)
  A representation of a softsign neuron filter.
- [class MPSCNNNeuronTanHNode](mpscnnneurontanhnode.md)
  A representation of a hyperbolic tangent neuron filter.
- [class MPSCNNNeuronExponentialNode](mpscnnneuronexponentialnode.md)
  A representation of an exponential neuron filter.
- [class MPSCNNNeuronGradientNode](mpscnnneurongradientnode.md)
  A representation of a gradient exponential neuron filter.
- [class MPSCNNNeuronLogarithmNode](mpscnnneuronlogarithmnode.md)
  A representation of a logarithm neuron filter.
- [class MPSCNNNeuronPowerNode](mpscnnneuronpowernode.md)
  A representation of a power neuron filter.
- [class MPSCNNNeuronNode](mpscnnneuronnode.md)
  The virtual base class for MPS CNN neuron nodes.
### Softmax Layer Nodes
- [class MPSCNNSoftMaxNode](mpscnnsoftmaxnode.md)
  A representation of a softmax filter.
- [class MPSCNNLogSoftMaxNode](mpscnnlogsoftmaxnode.md)
  A representation of a logarithmic softmax filter kernel.
- [class MPSCNNLogSoftMaxGradientNode](mpscnnlogsoftmaxgradientnode.md)
  A representation of a gradient logarithmic softmax filter kernel.
- [class MPSCNNSoftMaxGradientNode](mpscnnsoftmaxgradientnode.md)
  A representation of a gradient softmax filter.
### Normalization Layer Nodes
- [class MPSCNNCrossChannelNormalizationNode](mpscnncrosschannelnormalizationnode.md)
  A representation of a normalization kernel across feature channels.
- [class MPSCNNLocalContrastNormalizationNode](mpscnnlocalcontrastnormalizationnode.md)
  A representation of a local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationNode](mpscnnspatialnormalizationnode.md)
  A representation of a spatial normalization kernel.
- [class MPSCNNBatchNormalizationGradientNode](mpscnnbatchnormalizationgradientnode.md)
  A representation of a gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationNode](mpscnnbatchnormalizationnode.md)
  A representation of a batch normalization kernel.
- [protocol MPSCNNBatchNormalizationDataSource](mpscnnbatchnormalizationdatasource.md)
  A protocol that defines methods that a batch normalization state uses to initialize scale factors, bias terms, and batch statistics.
- [class MPSCNNInstanceNormalizationGradientNode](mpscnninstancenormalizationgradientnode.md)
  A representation of a gradient instance normalization kernel.
- [protocol MPSCNNInstanceNormalizationDataSource](mpscnninstancenormalizationdatasource.md)
  A protocol that defines methods that an instance normalization uses to initialize scale factors and bias terms.
- [class MPSCNNInstanceNormalizationNode](mpscnninstancenormalizationnode.md)
  A representation of an instance normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradientNode](mpscnnlocalcontrastnormalizationgradientnode.md)
  A representation of a gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationGradientNode](mpscnnspatialnormalizationgradientnode.md)
  A representation of a gradient spatial normalization kernel.
- [class MPSCNNNormalizationNode](mpscnnnormalizationnode.md)
  Virtual base class for CNN normalization nodes.
### Upsampling Layer Nodes
- [class MPSCNNUpsamplingBilinearNode](mpscnnupsamplingbilinearnode.md)
  A representation of a bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestNode](mpscnnupsamplingnearestnode.md)
  A representation of a nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradientNode](mpscnnupsamplingbilineargradientnode.md)
  A representation of a gradient bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearestGradientNode](mpscnnupsamplingnearestgradientnode.md)
  A representation of a gradient nearest spatial upsampling filter.
### Resampling Nodes
- [class MPSNNBilinearScaleNode](mpsnnbilinearscalenode.md)
  A representation of a bilinear resampling filter.
- [class MPSNNLanczosScaleNode](mpsnnlanczosscalenode.md)
  A representation of a Lanczos resampling filter.
- [class MPSNNScaleNode](mpsnnscalenode.md)
  Abstract node representing an image resampling filter.
- [protocol MPSImageTransformProvider](mpsimagetransformprovider.md)
  A general interface for objects that provide image resampling.
### Dropout Layer Nodes
- [class MPSCNNDropoutNode](mpscnndropoutnode.md)
  A representation of a dropout filter.
- [class MPSCNNDropoutGradientNode](mpscnndropoutgradientnode.md)
  A representation of a gradient dropout filter.
### Kernel Concatenation Nodes
- [class MPSNNConcatenationNode](mpsnnconcatenationnode.md)
  A representation of the results from one or more kernels.
- [class MPSNNConcatenationGradientNode](mpsnnconcatenationgradientnode.md)
  A representation of the results from one or more gradient kernels.
### Loss Layer Nodes
- [class MPSCNNLossNode](mpscnnlossnode.md)
  A representation of a loss kernel.
- [class MPSCNNYOLOLossNode](mpscnnyololossnode.md)
  A representation of a YOLO loss kernel.
- [class MPSNNLabelsNode](mpsnnlabelsnode.md)
  A placeholder node denoting the per-element weight buffer used by loss and gradient loss kernels.
### Filter Node Base Classes
- [class MPSNNFilterNode](mpsnnfilternode.md)
  A placeholder node denoting a neural network filter stage.
- [class MPSNNGradientFilterNode](mpsnngradientfilternode.md)
  A representation of a gradient filter.
### Protocols
- [protocol MPSNNTrainableNode](mpsnntrainablenode.md)
  A protocol that defines methods that determine whether and when neural network training parameters are updated.

## See Also

- [Training a Neural Network with Metal Performance Shaders](training-a-neural-network-with-metal-performance-shaders.md)
  Use an MPS neural network graph to train a simple neural network digit classifier.
- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSTemporaryImage](mpstemporaryimage.md)
  A texture for use in convolutional neural networks that stores transient data to be used and discarded promptly.
- [Convolutional Neural Network Kernels](convolutional-neural-network-kernels.md)
  Build neural networks with layers.
- [Recurrent Neural Networks](recurrent-neural-networks.md)
  Create recurrent neural networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/objects-that-simplify-the-creation-of-neural-networks)*