# adaptedAsSupervised(annotationColumnID:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Exposes this tabular estimator as a supervised tabular estimator.

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
func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>
```

## See Also

### Adapting and fitting
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a data frame
- [func fitted(to:)](./fitted%28to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator/adaptedassupervised(annotationcolumnid:))*