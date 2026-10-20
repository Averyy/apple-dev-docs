# init(learningRate:momentum:gradientScale:regularizationScale:clipsGradientsTo:usesNestrovMomentum:regularizationFunction:sgdMomentumVariant:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new stochastic gradient descent (SGD) with momentum optimizer object.

**Availability**:
- iOS 14.0+ - Deprecated in 15.0 (renamed: init(learningRate:momentum:gradientScale:regularizationScale:clipsGradientsTo:usesNesterovMomentum:regularizationFunction:sgdMomentumVariant:))
- iPadOS 14.0+ - Deprecated in 15.0 (renamed: init(learningRate:momentum:gradientScale:regularizationScale:clipsGradientsTo:usesNesterovMomentum:regularizationFunction:sgdMomentumVariant:))
- Mac Catalyst 14.0+ - Deprecated in 15.0 (renamed: init(learningRate:momentum:gradientScale:regularizationScale:clipsGradientsTo:usesNesterovMomentum:regularizationFunction:sgdMomentumVariant:))
- macOS 11.0+ - Deprecated in 12.0 (renamed: init(learningRate:momentum:gradientScale:regularizationScale:clipsGradientsTo:usesNesterovMomentum:regularizationFunction:sgdMomentumVariant:))
- tvOS 14.0+ - Deprecated in 15.0 (renamed: init(learningRate:momentum:gradientScale:regularizationScale:clipsGradientsTo:usesNesterovMomentum:regularizationFunction:sgdMomentumVariant:))
- visionOS
- watchOS 7.0+ - Deprecated in 8.0 (renamed: init(learningRate:momentum:gradientScale:regularizationScale:clipsGradientsTo:usesNesterovMomentum:regularizationFunction:sgdMomentumVariant:))

## Declaration

```swift
init(learningRate: Float, momentum: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo gradientBounds: ClosedRange<Float>? = nil, usesNestrovMomentum: Bool, regularizationFunction: BNNSOptimizerRegularizationFunction, sgdMomentumVariant: BNNSOptimizerSGDMomentumVariant)
```

## Parameters

- `learningRate`: A value that specifies the learning rate.
- `momentum`: The rate of momentum decay.
- `gradientScale`: A value that specifies the gradient scaling factor.
- `regularizationScale`: A value that specifies the regularization scaling factor.
- `gradientBounds`: The values for the minimum and maximum gradients.
- `usesNestrovMomentum`: A Boolean value that specifies whether to use Nesterov momentum update.
- `regularizationFunction`: The variable that specifies the regularization function.
- `sgdMomentumVariant`: The variable that specifies the momentum variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sgdmomentumoptimizer/init(learningrate:momentum:gradientscale:regularizationscale:clipsgradientsto:usesnestrovmomentum:regularizationfunction:sgdmomentumvariant:))*