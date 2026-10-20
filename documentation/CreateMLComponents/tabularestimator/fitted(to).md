# fitted(to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func fitted(to input: DataFrame) async throws -> Self.Transformer
```

**Other overloads**:

```swift
func fitted(to input: DataFrame) async throws -> Self.Transformer
```

## See Also

### Adapting and fitting
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](./adaptedassupervised%28annotationcolumnid%29.md)
  Exposes this tabular estimator as a supervised tabular estimator.
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a data frame


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator/fitted(to:))*