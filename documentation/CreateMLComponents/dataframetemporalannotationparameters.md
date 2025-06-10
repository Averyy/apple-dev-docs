# DataFrameTemporalAnnotationParameters

**Framework**: Create ML Components  
**Kind**: struct

Annotation parameters for the dataframe containing temporal annotations.

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
struct DataFrameTemporalAnnotationParameters<Annotation> where Annotation : Equatable, Annotation : Sendable
```

## Topics

### Creating the parameters
- [init()](dataframetemporalannotationparameters/init.md)
  Creates a DataFrameTemporalAnnotationParameters by using default options.
### Getting the properties
- [var annotationColumnID: ColumnID<Annotation>](dataframetemporalannotationparameters/annotationcolumnid.md)
  The column id that contains the annotation. The default value is “annotation” with `Annotation` type.
- [var endTimeColumnID: ColumnID<Double>?](dataframetemporalannotationparameters/endtimecolumnid.md)
  The column id that contains the end time. The default value is `nil`.
- [var filePathColumnID: ColumnID<String>](dataframetemporalannotationparameters/filepathcolumnid.md)
  The column id that contains the file path. The default value is “filePath” with String type.
- [var filePathType: DataFrameTemporalAnnotationParameters<Annotation>.FilePathType](dataframetemporalannotationparameters/filepathtype-swift.property.md)
  The file path type in the annotation file. The default value is `.absolute`.
- [var startTimeColumnID: ColumnID<Double>?](dataframetemporalannotationparameters/starttimecolumnid.md)
  The column id that contains the start time. The default value is `nil`.
### Specifying the path type
- [DataFrameTemporalAnnotationParameters.FilePathType](dataframetemporalannotationparameters/filepathtype-swift.enum.md)
  The file path type to be used.

## Relationships

### Conforms To
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
- [struct AnnotatedPrediction](annotatedprediction.md)
  An annotated prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/dataframetemporalannotationparameters)*