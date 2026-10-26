# MPSAccelerationStructureCompletionHandler

**Framework**: Metal Performance Shaders  
**Kind**: typealias  
**Role**: Type Alias

A block of code that’s invoked when an operation on an acceleration structure has completed.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
typealias MPSAccelerationStructureCompletionHandler = (MPSAccelerationStructure?) -> Void
```

```c
typedef void (^)(MPSAccelerationStructure *) MPSAccelerationStructureCompletionHandler;
```

## See Also

### Data Types
- [typealias MPSAxisAlignedBoundingBox](./mpsaxisalignedboundingbox-swift.typealias.md)
  An axis-aligned bounding box.
- [typealias MPSDeviceCaps](./mpsdevicecaps.md)
- [typealias MPSFunctionConstant](./mpsfunctionconstant.md)
- [typealias MPSFunctionConstantInMetal](./mpsfunctionconstantinmetal.md)
- [typealias MPSGradientNodeBlock](./mpsgradientnodeblock.md)
- [MPSCNNArithmeticGradientStateBatch](./mpscnnarithmeticgradientstatebatch.md)
  A batch of arithmetic gradient state instances.
- [MPSCNNConvolutionGradientStateBatch](./mpscnnconvolutiongradientstatebatch.md)
  A batch of convolution gradient state instances.
- [MPSCNNConvolutionTransposeGradientStateBatch](./mpscnnconvolutiontransposegradientstatebatch.md)
- [MPSCNNDropoutGradientStateBatch](./mpscnndropoutgradientstatebatch.md)
  A batch of dropout gradient state instances.
- [MPSCNNGroupNormalizationGradientStateBatch](./mpscnngroupnormalizationgradientstatebatch.md)
- [MPSCNNInstanceNormalizationGradientStateBatch](./mpscnninstancenormalizationgradientstatebatch.md)
  A batch of instance normalization gradient state instances.
- [MPSCNNLossLabelsBatch](./mpscnnlosslabelsbatch.md)
  A batch of loss labels instances.
- [MPSImageBatch](./mpsimagebatch.md)
  A batch of Metal Performance Shader image instances.
- [MPSNNBinaryGradientStateBatch](./mpsnnbinarygradientstatebatch.md)
  A batch of binary gradient state instances.
- [MPSNNGradientStateBatch](./mpsnngradientstatebatch.md)
  A batch of gradient state instances.
- [MPSNNMultiaryGradientStateBatch](./mpsnnmultiarygradientstatebatch.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructurecompletionhandler)*