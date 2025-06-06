# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a data frame

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
func fitted(to input: DataFrame, eventHandler: EventHandler? = nil) async throws -> ColumnSelector<Estimator, UnwrappedInput>.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A data frame.
- `eventHandler`: An event handler.

## See Also

- [ColumnSelector.Input](columnselector/input.md)
- [ColumnSelector.Output](columnselector/output.md)
- [ColumnSelector.Transformer](columnselector/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselector/fitted(to:eventhandler:))*