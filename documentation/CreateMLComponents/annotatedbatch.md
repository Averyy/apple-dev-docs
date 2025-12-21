# AnnotatedBatch

**Framework**: Create ML Components  
**Kind**: struct

A batch of annotated examples for fitting a supervised estimator.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct AnnotatedBatch<Scalar> where Scalar : MLShapedArrayScalar
```

## Topics

### Creating an annotated batch
- [init(features: MLShapedArray<Scalar>, annotations: MLShapedArray<Scalar>)](annotatedbatch/init(features:annotations:).md)
  Creates an annotated batch.
### Inspecting an annotated batch
- [var annotations: MLShapedArray<Scalar>](annotatedbatch/annotations.md)
  The shaped array of annotations.
- [var count: Int](annotatedbatch/count.md)
  The number of examples in the batch.
- [var features: MLShapedArray<Scalar>](annotatedbatch/features.md)
  The shaped array of features.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnnotatedFiles](annotatedfiles.md)
  An annotated files collection.
- [struct AnnotatedFeature](annotatedfeature.md)
  An annotated example for fitting a supervised estimator.
- [struct AnnotatedFeatureProvider](annotatedfeatureprovider.md)
  An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- [struct AnnotatedPrediction](annotatedprediction.md)
  An annotated prediction.
- [struct DataFrameTemporalAnnotationParameters](dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedbatch)*