# AnnotatedFiles

**Framework**: Create ML Components  
**Kind**: struct

An annotated files collection.

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
struct AnnotatedFiles
```

## Topics

### Creating the feature
- [init(labeledBySubdirectoryNamesAt: URL, type: UTType, continueOnFailure: Bool) throws](annotatedfiles/init(labeledbysubdirectorynamesat:type:continueonfailure:).md)
  Reads training examples from a directory containing files in labeled sub-directories.
- [init(labeledByNamesAt: URL, separator: Character, index: Int, type: UTType, continueOnFailure: Bool) throws](annotatedfiles/init(labeledbynamesat:separator:index:type:continueonfailure:).md)
  Reads training examples from a directory containing files having their labels in the name. The name can contain multiple words separated by a `separator`. So the `index` tells the position of the label in the file name. Files with incorrect name format are ignored.

## Relationships

### Conforms To
- [Collection](../swift/collection.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [struct AnnotatedBatch](annotatedbatch.md)
  A batch of annotated examples for fitting a supervised estimator.
- [struct AnnotatedFeature](annotatedfeature.md)
  An annotated example for fitting a supervised estimator.
- [struct AnnotatedFeatureProvider](annotatedfeatureprovider.md)
  An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- [struct AnnotatedPrediction](annotatedprediction.md)
  An annotated prediction.
- [struct DataFrameTemporalAnnotationParameters](dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles)*