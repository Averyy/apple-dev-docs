# epochs

**Framework**: Core ML  
**Kind**: property

The key you use to access the optimizer’s epochs parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class var epochs: MLParameterKey { get }
```

#### Discussion

The value type for the [`epochs`](mlparameterkey/epochs.md) key is an [`Int64`](https://developer.apple.com/documentation/Swift/Int64).

## See Also

- [class var learningRate: MLParameterKey](mlparameterkey/learningrate.md)
  The key you use to access the optimizer’s learning rate parameter.
- [class var momentum: MLParameterKey](mlparameterkey/momentum.md)
  The key you use to access the stochastic gradient descent (SGD) optimizer’s momentum parameter.
- [class var miniBatchSize: MLParameterKey](mlparameterkey/minibatchsize.md)
  The key you use to access the optimizer’s mini batch-size parameter.
- [class var beta1: MLParameterKey](mlparameterkey/beta1.md)
  The key you use to access the Adam optimizer’s first beta parameter.
- [class var beta2: MLParameterKey](mlparameterkey/beta2.md)
  The key you use to access the Adam optimizer’s second beta parameter.
- [class var eps: MLParameterKey](mlparameterkey/eps.md)
  The key you use to access the Adam optimizer’s epsilon parameter.
- [class var shuffle: MLParameterKey](mlparameterkey/shuffle.md)
  The key you use to access the shuffle parameter, a Boolean value that determines whether the model randomizes the data between epochs.
- [class var seed: MLParameterKey](mlparameterkey/seed.md)
  The key you use to access the seed parameter that initializes the random number generator for the shuffle option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterkey/epochs)*