# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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
func fitted<Input>(to input: Input, eventHandler: EventHandler? = nil) async throws -> LinearRegressorModel<Scalar> where Input : Sequence, Input.Element == AnnotatedFeature<MLShapedArray<Scalar>, Scalar>
```

#### Return Value

The fitted linear regressor model.

## Parameters

- `input`: A sequence of examples used for fitting the regressor.
- `eventHandler`: An event handler. This method reports maximum error and root-mean-square error metrics.

## See Also

### Fitting
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> LinearRegressorModel<Scalar>](./fitted%28to,validateon,eventhandler%29.md)
  Fits a linear regressor model to a sequence of examples.
- [LinearRegressor.Annotation](./annotation.md)
  The annotation type.
- [LinearRegressor.Transformer](./transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/fitted(to:eventhandler:))*