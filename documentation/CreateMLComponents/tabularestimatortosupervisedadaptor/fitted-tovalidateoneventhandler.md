# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Returns the tabular transformer fitted using the provided tabular estimator.

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
func fitted(to input: DataFrame, validateOn validation: DataFrame? = nil, eventHandler: EventHandler? = nil) async throws -> Estimator.Transformer
```

#### Return Value

The a fitted tabular transformer.

## Parameters

- `input`: A data frame containing examples.
- `validation`: A data frame containing examples.
- `eventHandler`: An event handler.

## See Also

- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:))*