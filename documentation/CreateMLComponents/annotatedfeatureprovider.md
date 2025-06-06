# AnnotatedFeatureProvider

**Framework**: Create ML Components  
**Kind**: struct

An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.

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
struct AnnotatedFeatureProvider<Base, UnwrappedInput> where Base : SupervisedEstimator, Base.Transformer.Input == UnwrappedInput?
```

#### Overview

Tabular estimators use multiple features columns as input. When there is a single column of features, you may use a non-tabular estimator. Do this by combining multiple columns with a `ColumnConcatenator` transformer. Once there is a single column of features, use `AnnotatedFeatureProvider` to specify which column contains the features, which column contains the annotations, and which column should hold the results.

When using `AnnotatedFeatureProvider`, make sure to handle missing values before using a non-tabular estimator that takes non-optional values. This example includes an `OptionalUnwrapper` transformer.

```None
let concatenation = ColumnConcatenator<Float>(
    columnSelection: .include(columnNames: ["type", "region"]),
    concatenatedColumnName: "features"
)
let regression = AnnotatedFeatureProvider(
    OptionalUnwrapper<MLShapedArray<Float>>().appending(LinearRegressor<Float>()),
    annotationsColumnName: "price",
    featuresColumnName: "features",
    resultsColumnName: "result"
)
let task = concatenation.appending(regression)
```

## Topics

### Creating the provider
- [init(Base, annotationsColumnName: String, featuresColumnName: String, resultsColumnName: String)](annotatedfeatureprovider/init(_:annotationscolumnname:featurescolumnname:resultscolumnname:).md)
  Creates an adaptor that converts a regular estimator to a tabular estimator.
### Getting the properties
- [var annotationColumnID: ColumnID<AnnotatedFeatureProvider<Base, UnwrappedInput>.Annotation>](annotatedfeatureprovider/annotationcolumnid.md)
  The annotation column identifier.
- [AnnotatedFeatureProvider.Annotation](annotatedfeatureprovider/annotation.md)
  The annotation type.
- [var base: Base](annotatedfeatureprovider/base.md)
  The base estimator.
- [var featuresColumnName: String](annotatedfeatureprovider/featurescolumnname.md)
  The features column name.
- [var resultsColumnName: String](annotatedfeatureprovider/resultscolumnname.md)
  The results column name.
### Encoding and decoding
- [func encode(AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer, to: inout any EstimatorEncoder) throws](annotatedfeatureprovider/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer](annotatedfeatureprovider/decode(from:).md)
  Decodes a previously fitted transformer.
### Fitting
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> ColumnSelectorTransformer<Base.Transformer, UnwrappedInput>](annotatedfeatureprovider/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a data frame
- [AnnotatedFeatureProvider.Transformer](annotatedfeatureprovider/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedTabularEstimator Implementations](annotatedfeatureprovider/supervisedtabularestimator-implementations.md)
- [UpdatableSupervisedTabularEstimator Implementations](annotatedfeatureprovider/updatablesupervisedtabularestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SupervisedTabularEstimator](supervisedtabularestimator.md)
- [UpdatableSupervisedTabularEstimator](updatablesupervisedtabularestimator.md)

## See Also

- [struct AnnotatedFiles](annotatedfiles.md)
  An annotated files collection.
- [struct AnnotatedBatch](annotatedbatch.md)
  A batch of annotated examples for fitting a supervised estimator.
- [struct AnnotatedFeature](annotatedfeature.md)
  An annotated example for fitting a supervised estimator.
- [struct AnnotatedPrediction](annotatedprediction.md)
  An annotated prediction.
- [struct DataFrameTemporalAnnotationParameters](dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfeatureprovider)*