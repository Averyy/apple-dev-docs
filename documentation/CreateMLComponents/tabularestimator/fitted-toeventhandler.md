# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

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
func fitted(to input: DataFrame, eventHandler: EventHandler?) async throws -> Self.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A data frame containing examples.
- `eventHandler`: An event handler.

## See Also

- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](tabularestimator/adaptedassupervised(annotationcolumnid:).md)
  Exposes this tabular estimator as a supervised tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator/fitted(to:eventhandler:))*