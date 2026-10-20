# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a boosted tree regressor model to a collection of examples.

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
func fitted(to input: DataFrame, validateOn validation: DataFrame? = nil, eventHandler: EventHandler? = nil) async throws -> TreeRegressorModel
```

#### Return Value

The fitted boosted tree regressor model.

## Parameters

- `input`: A data frame containing examples used for fitting the transformer.
- `validation`: A data frame containing examples used for validating the fitted transformer.
- `eventHandler`: An event handler. This method reports maximum error and root-mean-square error metrics.

## See Also

- [BoostedTreeRegressor.Transformer](boostedtreeregressor/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor/fitted(to:validateon:eventhandler:))*