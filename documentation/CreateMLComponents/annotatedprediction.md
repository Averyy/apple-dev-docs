# AnnotatedPrediction

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [init(prediction: Prediction, annotation: Annotation)](./annotatedprediction/init%28prediction,annotation%29.md)
  Creates an annotated preditction.
### Getting the properties
- [var annotation: Annotation](./annotatedprediction/annotation.md)
  The ground truth annotation.
- [var prediction: Prediction](./annotatedprediction/prediction.md)
  The predicted value.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Annotations
- [struct AnnotatedFiles](./annotatedfiles.md)
  An annotated files collection.
- [struct AnnotatedBatch](./annotatedbatch.md)
  A batch of annotated examples for fitting a supervised estimator.
- [struct AnnotatedFeature](./annotatedfeature.md)
  An annotated example for fitting a supervised estimator.
- [struct AnnotatedFeatureProvider](./annotatedfeatureprovider.md)
  An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- [struct DataFrameTemporalAnnotationParameters](./dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedprediction)*