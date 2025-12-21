# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a fully connected network regressor model to a sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func fitted<Input>(to input: Input, eventHandler: EventHandler? = nil) async throws -> FullyConnectedNetworkRegressor<Scalar>.Transformer where Input : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Float>
```

#### Return Value

The fitted transformer.

#### Discussion

The training process partitions the input into random batches according to the batch size configuration parameter. Training stops when the maximum number of iterations is reached.

> **Note**: This method does not do early-stopping, using a high value for `maximumIterations` may lead to over-fitting. Consider providing a validation set.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkRegressorModel<Scalar>](fullyconnectednetworkregressor/fitted(to:validateon:eventhandler:).md)
  Fits a fully connected network regressor model to a sequence of examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor/fitted(to:eventhandler:))*