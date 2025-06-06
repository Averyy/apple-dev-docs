# adaptedAsSupervised(annotationColumnID:)

**Framework**: Create ML Components  
**Kind**: method

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoestimatoradaptor/adaptedassupervised(annotationcolumnid:))*