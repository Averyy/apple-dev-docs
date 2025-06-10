# AnnotatedPrediction

**Framework**: Create ML Components  
**Kind**: struct

An annotated prediction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct AnnotatedPrediction<Prediction, Annotation>
```

## Topics

### Creating an annotated prediction
- [init(prediction: Prediction, annotation: Annotation)](annotatedprediction/init(prediction:annotation:).md)
  Creates an annotated preditction.
### Getting the properties
- [var annotation: Annotation](annotatedprediction/annotation.md)
  The ground truth annotation.
- [var prediction: Prediction](annotatedprediction/prediction.md)
  The predicted value.
### Default Implementations
- [Decodable Implementations](annotatedprediction/decodable-implementations.md)
- [Encodable Implementations](annotatedprediction/encodable-implementations.md)
- [Equatable Implementations](annotatedprediction/equatable-implementations.md)
- [Hashable Implementations](annotatedprediction/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnnotatedFiles](annotatedfiles.md)
  An annotated files collection.
- [struct AnnotatedBatch](annotatedbatch.md)
  A batch of annotated examples for fitting a supervised estimator.
- [struct AnnotatedFeature](annotatedfeature.md)
  An annotated example for fitting a supervised estimator.
- [struct AnnotatedFeatureProvider](annotatedfeatureprovider.md)
  An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- [struct DataFrameTemporalAnnotationParameters](dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedprediction)*