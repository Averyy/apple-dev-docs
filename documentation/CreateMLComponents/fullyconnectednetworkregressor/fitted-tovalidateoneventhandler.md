# fitted(to:validateOn:eventHandler:)

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
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> FullyConnectedNetworkRegressorModel<Scalar> where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Float>, Validation.Element == AnnotatedFeature<MLShapedArray<Scalar>, Float>
```

#### Return Value

The fitted fully connected network regressor model.

#### Discussion

The training process partitions the input into random batches according to the batch size configuration parameter. Training stops when the validation loss stops improving or when the maximum number of iterations is reached.

## Parameters

- `input`: A sequence of examples used for fitting the regressor.
- `validation`: A sequence of examples used for validating the fitted regressor.
- `eventHandler`: An event handler.

## See Also

- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkRegressor<Scalar>.Transformer](fullyconnectednetworkregressor/fitted(to:eventhandler:).md)
  Fits a fully connected network regressor model to a sequence of examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor/fitted(to:validateon:eventhandler:))*