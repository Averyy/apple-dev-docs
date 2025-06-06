# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a linear regressor model to a sequence of examples.

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
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> LinearRegressorModel<Scalar> where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Scalar>, Validation.Element == AnnotatedFeature<MLShapedArray<Scalar>, Scalar>
```

#### Return Value

The fitted linear regressor model.

## Parameters

- `input`: A sequence of examples used for fitting the regressor.
- `validation`: A sequence of examples used for validating the fitted regressor.
- `eventHandler`: An event handler. This method reports maximum error and root-mean-square error metrics.

## See Also

- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> LinearRegressorModel<Scalar>](linearregressor/fitted(to:eventhandler:).md)
  Fits a linear regressor model to a sequence of examples.
- [LinearRegressor.Annotation](linearregressor/annotation.md)
  The annotation type.
- [LinearRegressor.Transformer](linearregressor/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/fitted(to:validateon:eventhandler:))*