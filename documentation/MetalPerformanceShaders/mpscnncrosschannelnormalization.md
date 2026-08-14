# MPSCNNCrossChannelNormalization

**Framework**: Metal Performance Shaders  
**Kind**: class

A normalization kernel applied across feature channels.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNCrossChannelNormalization
```

#### Overview

The normalization kernel applies the kernel to a local region across nearby feature channels, but with no spatial extent (i.e., they have the shape `kernel size x 1 x 1`). The normalized output is given by the function:

![Y(i,j,k) = X(i,j,k) / L(i,j,k)^beta](/images/com.apple.metalperformanceshaders/media-2903526@2x.png)

Where the normalizing factor is:

![L(i,j,k) = delta + alpha/N * (sum_{q in Q(k)} X(i,j,q)^2](/images/com.apple.metalperformanceshaders/media-2903524@2x.png)

Where `N` is the kernel size. The window `Q(k)` itself is defined as:

![Q(k) = [max(0, k-floor(N/2)), min(D-1, k+floor((N-1)/2)]](/images/com.apple.metalperformanceshaders/media-2903527@2x.png)

Where `k` is the feature channel index (running from 0 to `D-1`) and `D` is the number of feature channels, and the values of [`alpha`](mpscnncrosschannelnormalization/alpha.md), [`beta`](mpscnncrosschannelnormalization/beta.md), and [`delta`](mpscnncrosschannelnormalization/delta.md) are set via properties.

It is your responsibility to ensure that the combination of the values of the [`delta`](mpscnncrosschannelnormalization/delta.md) and [`alpha`](mpscnncrosschannelnormalization/alpha.md) properties does not result in a situation where the denominator becomes zero - in such situations the resulting pixel-value is undefined.

> **Note**:  The encoding methods in the [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) class can be used to encode an [`MPSCNNCrossChannelNormalization`](mpscnncrosschannelnormalization.md) object to a [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnncrosschannelnormalization/init(coder:device:).md)
  Initializes a normalization kernel in a channel.
- [init(device: any MTLDevice, kernelSize: Int)](mpscnncrosschannelnormalization/init(device:kernelsize:).md)
  Initializes a normalization kernel in a channel.
### Instance Properties
- [var alpha: Float](mpscnncrosschannelnormalization/alpha.md)
  The “alpha” variable of the kernel function.
- [var beta: Float](mpscnncrosschannelnormalization/beta.md)
  The “beta” variable of the kernel function.
- [var delta: Float](mpscnncrosschannelnormalization/delta.md)
  The “delta” variable of the kernel function.
- [var kernelSize: Int](mpscnncrosschannelnormalization/kernelsize.md)
  The size of the square kernel window.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSCNNCrossChannelNormalizationGradient](mpscnncrosschannelnormalizationgradient.md)
  A gradient normalization kernel applied across feature channels.
- [class MPSCNNLocalContrastNormalization](mpscnnlocalcontrastnormalization.md)
  A local-contrast normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradient](mpscnnlocalcontrastnormalizationgradient.md)
  A gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalization](mpscnnspatialnormalization.md)
  A spatial normalization kernel.
- [class MPSCNNSpatialNormalizationGradient](mpscnnspatialnormalizationgradient.md)
  A gradient spatial normalization kernel.
- [class MPSCNNBatchNormalization](mpscnnbatchnormalization.md)
  A batch normalization kernel.
- [class MPSCNNBatchNormalizationGradient](mpscnnbatchnormalizationgradient.md)
  A gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationState](mpscnnbatchnormalizationstate.md)
  An object that stores data required to execute batch normalization.
- [class MPSCNNNormalizationMeanAndVarianceState](mpscnnnormalizationmeanandvariancestate.md)
  An object that stores mean and variance terms used to execute batch normalization.
- [class MPSCNNBatchNormalizationStatistics](mpscnnbatchnormalizationstatistics.md)
  An object that stores statistics required to execute batch normalization.
- [class MPSCNNBatchNormalizationStatisticsGradient](mpscnnbatchnormalizationstatisticsgradient.md)
  An object that stores the gradient of the loss function with respect to the batch statistics and batch normalization weights.
- [class MPSCNNInstanceNormalization](mpscnninstancenormalization.md)
  An instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradient](mpscnninstancenormalizationgradient.md)
  A gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationGradientState](mpscnninstancenormalizationgradientstate.md)
  An object that stores information required to execute a gradient pass for instance normalization.
- [class MPSCNNNormalizationGammaAndBetaState](mpscnnnormalizationgammaandbetastate.md)
  An object that stores gamma and beta terms used to apply a scale and bias in instance- or batch-normalization operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization)*