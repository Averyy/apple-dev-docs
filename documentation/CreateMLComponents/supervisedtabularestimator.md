# SupervisedTabularEstimator

**Framework**: Create ML Components  
**Kind**: protocol

A tabular estimator that creates a transformer by fitting to a data set in a data frame.

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
protocol SupervisedTabularEstimator<Transformer, Annotation>
```

## Topics

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](supervisedtabularestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](supervisedtabularestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
- [associatedtype Annotation](supervisedtabularestimator/annotation.md)
  The annotation type.
- [var annotationColumnID: ColumnID<Self.Annotation>](supervisedtabularestimator/annotationcolumnid.md)
  The annotation column identifier.
- [associatedtype Transformer : TabularTransformer](supervisedtabularestimator/transformer.md)
  The transformer type created by this estimator.
### Appending
- [func appending(_:)](supervisedtabularestimator/appending(_:).md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
### Fitting
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a data frame
- [func fitted(to: DataFrame, validateOn: DataFrame?) async throws -> Self.Transformer](supervisedtabularestimator/fitted(to:validateon:).md)
### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](supervisedtabularestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](supervisedtabularestimator/decode(from:).md)
  Decodes a previously fitted transformer.

## Relationships

### Inherited By
- [UpdatableSupervisedTabularEstimator](updatablesupervisedtabularestimator.md)
### Conforming Types
- [AnnotatedFeatureProvider](annotatedfeatureprovider.md)
- [BoostedTreeClassifier](boostedtreeclassifier.md)
- [BoostedTreeRegressor](boostedtreeregressor.md)
- [PreprocessingSupervisedTabularEstimator](preprocessingsupervisedtabularestimator.md)
- [PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
- [TabularEstimatorToSupervisedAdaptor](tabularestimatortosupervisedadaptor.md)
- [UpdatableTabularEstimatorToSupervisedAdaptor](updatabletabularestimatortosupervisedadaptor.md)

## See Also

- [protocol TabularTransformer](tabulartransformer.md)
  A tabular transformer that transforms a data frame.
- [protocol TabularEstimator](tabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [struct ColumnSelector](columnselector.md)
  An operation that applies an estimator to a selection of columns.
- [struct ColumnSelectorTransformer](columnselectortransformer.md)
  A transformer that applies a base transformer to specific columns in a data frame.
- [enum ColumnSelection](columnselection.md)
  A selection of columns from a data frame.
- [struct ColumnConcatenator](columnconcatenator.md)
  A transformer that concatenates every numerical column in a dataframe into to a shaped array for each row.
- [struct PreprocessingSupervisedTabularEstimator](preprocessingsupervisedtabularestimator.md)
  A supervised tabular estimator that composes a preprocessing transformer and a supervised tabular estimator.
- [struct PreprocessingTabularEstimator](preprocessingtabularestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator)*