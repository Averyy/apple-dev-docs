# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a data frame.

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
func fitted(to input: DataFrame, validateOn validation: DataFrame?, eventHandler: EventHandler? = nil) async throws -> UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A data frame containing examples used for fitting the transformer.
- `validation`: A data frame containing examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

- [func makeTransformer() -> Estimator.Transformer](updatabletabularestimatortosupervisedadaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout UpdatableTabularEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](updatabletabularestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame containing examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:))*