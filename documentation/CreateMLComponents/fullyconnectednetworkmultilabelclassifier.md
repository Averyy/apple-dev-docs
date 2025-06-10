# FullyConnectedNetworkMultiLabelClassifier

**Framework**: Create ML Components  
**Kind**: struct

A classifier that uses a multi-label fully-connected network.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct FullyConnectedNetworkMultiLabelClassifier<Scalar, Label> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint, Scalar : Decodable, Scalar : Encodable, Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Mentions

- [Creating a multi-label image classifier](creating-a-multi-label-image-classifier.md)

## Topics

### Creating a classifier
- [init(labels: Set<Label>, configuration: FullyConnectedNetworkConfiguration)](fullyconnectednetworkmultilabelclassifier/init(labels:configuration:).md)
  Creates a full-connected network multi-label classifier.
### Getting the properties
- [var configuration: FullyConnectedNetworkConfiguration](fullyconnectednetworkmultilabelclassifier/configuration.md)
  The fully-connected network configuration.
- [static var defaultConfiguration: FullyConnectedNetworkConfiguration](fullyconnectednetworkmultilabelclassifier/defaultconfiguration.md)
  The default fully-connected network configration.
- [var labels: Set<Label>](fullyconnectednetworkmultilabelclassifier/labels.md)
  The set of possible labels.
### Fitting a classifier
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](fullyconnectednetworkmultilabelclassifier/fitted(to:eventhandler:).md)
  Fits a fully-connected network multi-label classifier model to a sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](fullyconnectednetworkmultilabelclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a fully-connected network multi-label classifier model to a sequence of examples.
- [FullyConnectedNetworkMultiLabelClassifier.Annotation](fullyconnectednetworkmultilabelclassifier/annotation.md)
  The annotation type.
- [FullyConnectedNetworkMultiLabelClassifier.Transformer](fullyconnectednetworkmultilabelclassifier/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedEstimator Implementations](fullyconnectednetworkmultilabelclassifier/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](fullyconnectednetworkmultilabelclassifier/updatablesupervisedestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedEstimator](supervisedestimator.md)
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)

## See Also

- [protocol Classifier](classifier.md)
  An estimator that predicts classification probabilities.
- [struct LogisticRegressionClassifier](logisticregressionclassifier.md)
  A logistic regression classifier.
- [struct LogisticRegressionClassifierModel](logisticregressionclassifiermodel.md)
  A trained logistic regression classifier model.
- [struct BoostedTreeClassifier](boostedtreeclassifier.md)
  A gradient boosted decision tree classifier.
- [struct BoostedTreeConfiguration](boostedtreeconfiguration.md)
  A boosted tree configuration.
- [struct FullyConnectedNetworkClassifier](fullyconnectednetworkclassifier.md)
  A classifier that uses a fully connected network.
- [struct FullyConnectedNetworkClassifierModel](fullyconnectednetworkclassifiermodel.md)
  A classifier model that uses a fully connected network.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier)*