# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a boosted tree classifier model to a collection of examples.

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
func fitted(to input: DataFrame, validateOn validation: DataFrame? = nil, eventHandler: EventHandler? = nil) async throws -> TreeClassifierModel<Label>
```

#### Return Value

The fitted boosted tree classifier model.

## Parameters

- `input`: A data frame of examples.
- `validation`: A data frame of validation examples.
- `eventHandler`: An event handler. This method reports accuracy and loss metrics.

## See Also

- [BoostedTreeClassifier.Annotation](boostedtreeclassifier/annotation.md)
  The annotation type.
- [BoostedTreeClassifier.Transformer](boostedtreeclassifier/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier/fitted(to:validateon:eventhandler:))*