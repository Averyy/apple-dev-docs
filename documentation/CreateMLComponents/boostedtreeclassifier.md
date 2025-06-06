# BoostedTreeClassifier

**Framework**: Create ML Components  
**Kind**: struct

A gradient boosted decision tree classifier.

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
struct BoostedTreeClassifier<Label> where Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Topics

### Creating a classifier
- [init(labels: Set<Label?>, annotationColumnName: String, featureColumnNames: [String], configuration: BoostedTreeConfiguration)](boostedtreeclassifier/init(labels:annotationcolumnname:featurecolumnnames:configuration:).md)
  Creates a boosted tree classifier.
### Getting the properties
- [var annotationColumnID: ColumnID<Label>](boostedtreeclassifier/annotationcolumnid.md)
  The annotation column identifier.
- [var featureColumnNames: [String]](boostedtreeclassifier/featurecolumnnames.md)
  The names of the columns containing feature values.
- [var configuration: BoostedTreeConfiguration](boostedtreeclassifier/configuration.md)
  Boosted tree configuration.
- [var labels: Set<Label?>](boostedtreeclassifier/labels.md)
  The set of possible labels.
### Fitting the classifier
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> TreeClassifierModel<Label>](boostedtreeclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a boosted tree classifier model to a collection of examples.
- [BoostedTreeClassifier.Annotation](boostedtreeclassifier/annotation.md)
  The annotation type.
- [BoostedTreeClassifier.Transformer](boostedtreeclassifier/transformer.md)
  The transformer type created by this estimator.
### Encoding and decoding the classifier
- [func encode(TreeClassifierModel<Label>, to: inout any EstimatorEncoder) throws](boostedtreeclassifier/encode(_:to:).md)
  Encodes a fitted transformer.
- [func encodeLabels(some Collection<Optional<Label>>) throws -> (labels: [String?], encoded: [Int])](boostedtreeclassifier/encodelabels(_:).md)
- [func decode(from: inout any EstimatorDecoder) throws -> TreeClassifierModel<Label>](boostedtreeclassifier/decode(from:).md)
  Decodes a previously fitted transformer.
### Default Implementations
- [SupervisedTabularEstimator Implementations](boostedtreeclassifier/supervisedtabularestimator-implementations.md)
- [UpdatableSupervisedTabularEstimator Implementations](boostedtreeclassifier/updatablesupervisedtabularestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SupervisedTabularEstimator](supervisedtabularestimator.md)
- [UpdatableSupervisedTabularEstimator](updatablesupervisedtabularestimator.md)

## See Also

- [protocol Classifier](classifier.md)
  An estimator that predicts classification probabilities.
- [struct LogisticRegressionClassifier](logisticregressionclassifier.md)
  A logistic regression classifier.
- [struct LogisticRegressionClassifierModel](logisticregressionclassifiermodel.md)
  A trained logistic regression classifier model.
- [struct BoostedTreeConfiguration](boostedtreeconfiguration.md)
  A boosted tree configuration.
- [struct FullyConnectedNetworkClassifier](fullyconnectednetworkclassifier.md)
  A classifier that uses a fully connected network.
- [struct FullyConnectedNetworkClassifierModel](fullyconnectednetworkclassifiermodel.md)
  A classifier model that uses a fully connected network.
- [struct FullyConnectedNetworkMultiLabelClassifier](fullyconnectednetworkmultilabelclassifier.md)
  A classifier that uses a multi-label fully-connected network.
- [struct FullyConnectedNetworkMultiLabelClassifierModel](fullyconnectednetworkmultilabelclassifiermodel.md)
  A multi-label classifier model that uses a fully-connected network.
- [struct FullyConnectedNetworkConfiguration](fullyconnectednetworkconfiguration.md)
  A fully connected network configuration.
- [struct TreeClassifierModel](treeclassifiermodel.md)
  A trained tree classifier model.
- [struct TimeSeriesClassifier](timeseriesclassifier.md)
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier)*