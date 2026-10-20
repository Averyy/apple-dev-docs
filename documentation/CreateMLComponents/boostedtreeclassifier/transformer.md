# BoostedTreeClassifier.Transformer

**Framework**: Create ML Components  
**Kind**: typealias  
**Role**: Type Alias

The transformer type created by this estimator.

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
typealias Transformer = TreeClassifierModel<Label>
```

## See Also

### Fitting the classifier
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> TreeClassifierModel<Label>](./fitted%28to,validateon,eventhandler%29.md)
  Fits a boosted tree classifier model to a collection of examples.
- [BoostedTreeClassifier.Annotation](./annotation.md)
  The annotation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier/transformer)*