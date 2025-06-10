# AnnotatedFeature

**Framework**: Create ML Components  
**Kind**: struct

An annotated example for fitting a supervised estimator.

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
struct AnnotatedFeature<Feature, Annotation>
```

## Mentions

- [Creating a multi-label image classifier](creating-a-multi-label-image-classifier.md)

## Topics

### Creating the feature
- [init(feature: Feature, annotation: Annotation)](annotatedfeature/init(feature:annotation:).md)
  Creates an example with a feature and an annotation.
### Getting the properties
- [var annotation: Annotation](annotatedfeature/annotation.md)
  The annotation.
- [var feature: Feature](annotatedfeature/feature.md)
  The feature value.
### Default Implementations
- [Decodable Implementations](annotatedfeature/decodable-implementations.md)
- [Encodable Implementations](annotatedfeature/encodable-implementations.md)
- [Equatable Implementations](annotatedfeature/equatable-implementations.md)
- [Hashable Implementations](annotatedfeature/hashable-implementations.md)

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
- [struct AnnotatedFeatureProvider](annotatedfeatureprovider.md)
  An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- [struct AnnotatedPrediction](annotatedprediction.md)
  An annotated prediction.
- [struct DataFrameTemporalAnnotationParameters](dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfeature)*