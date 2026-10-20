# TabularEstimator

**Framework**: Create ML Components  
**Kind**: protocol  
**Role**: Protocol

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
protocol TabularEstimator<Transformer>
```

## Topics

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](./tabularestimator/read%28from%29.md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](./tabularestimator/write%28_,to,overwrite%29.md)
  Writes the encoded transformer to a file.
- [associatedtype Transformer : TabularTransformer](./tabularestimator/transformer.md)
  The transformer type created by this estimator.
### Appending
- [func appending(_:)](./tabularestimator/appending%28_%29.md)
  Composes this tabular estimator with a supervised tabular estimator.
### Adapting and fitting
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](./tabularestimator/adaptedassupervised%28annotationcolumnid%29.md)
  Exposes this tabular estimator as a supervised tabular estimator.
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> Self.Transformer](./tabularestimator/fitted%28to,eventhandler%29.md)
  Fits a transformer to a data frame
- [func fitted(to:)](./tabularestimator/fitted%28to%29.md)
### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](./tabularestimator/encode%28_,to%29.md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](./tabularestimator/decode%28from%29.md)
  Decodes a previously fitted transformer.

## Relationships

### Inherited By
- [UpdatableTabularEstimator](./updatabletabularestimator.md)
### Conforming Types
- [ColumnSelector](./columnselector.md)
- [PreprocessingTabularEstimator](./preprocessingtabularestimator.md)
- [PreprocessingUpdatableTabularEstimator](./preprocessingupdatabletabularestimator.md)
- [TabularTransformerToEstimatorAdaptor](./tabulartransformertoestimatoradaptor.md)
- [TabularTransformerToUpdatableEstimatorAdaptor](./tabulartransformertoupdatableestimatoradaptor.md)

## See Also

### Tabular components
- [protocol TabularTransformer](./tabulartransformer.md)
  A tabular transformer that transforms a data frame.
- [protocol SupervisedTabularEstimator](./supervisedtabularestimator.md)
  A tabular estimator that creates a transformer by fitting to a data set in a data frame.
- [struct ColumnSelector](./columnselector.md)
  An operation that applies an estimator to a selection of columns.
- [struct ColumnSelectorTransformer](./columnselectortransformer.md)
  A transformer that applies a base transformer to specific columns in a data frame.
- [enum ColumnSelection](./columnselection.md)
  A selection of columns from a data frame.
- [struct ColumnConcatenator](./columnconcatenator.md)
  A transformer that concatenates every numerical column in a dataframe into to a shaped array for each row.
- [struct PreprocessingSupervisedTabularEstimator](./preprocessingsupervisedtabularestimator.md)
  A supervised tabular estimator that composes a preprocessing transformer and a supervised tabular estimator.
- [struct PreprocessingTabularEstimator](./preprocessingtabularestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingUpdatableSupervisedTabularEstimator](./preprocessingupdatablesupervisedtabularestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableTabularEstimator](./preprocessingupdatabletabularestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator)*