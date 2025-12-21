# TimeSeriesClassifier

**Framework**: Create ML Components  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct TimeSeriesClassifier<Scalar, Label> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint, Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Topics

### Creating a time series classifier
- [init(labels: Set<Label>, configuration: TimeSeriesClassifierConfiguration)](timeseriesclassifier/init(labels:configuration:).md)
  Creates a time series classifier.
### Inspecting a time series classifier
- [var configuration: TimeSeriesClassifierConfiguration](timeseriesclassifier/configuration-swift.property.md)
  The configuration.
- [var labels: Set<Label>](timeseriesclassifier/labels.md)
  The set of possible labels.
### Fitting a time series classifier
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler?) async throws -> TimeSeriesClassifier<Scalar, Label>.Model](timeseriesclassifier/fitted(to:eventhandler:).md)
  Fits a time series classifier model to a sequence of examples.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler?) async throws -> TimeSeriesClassifier<Scalar, Label>.Model](timeseriesclassifier/fitted(to:validateon:eventhandler:).md)
  Fits a time series classifier model to a sequence of examples.
### Supporting types
- [TimeSeriesClassifier.Configuration](timeseriesclassifier/configuration-swift.typealias.md)
- [TimeSeriesClassifier.Model](timeseriesclassifier/model.md)
  A time-series classifier model.
### Default Implementations
- [UpdatableSupervisedEstimator Implementations](timeseriesclassifier/updatablesupervisedestimator-implementations.md)

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
- [struct FullyConnectedNetworkMultiLabelClassifier](fullyconnectednetworkmultilabelclassifier.md)
  A classifier that uses a multi-label fully-connected network.
- [struct FullyConnectedNetworkMultiLabelClassifierModel](fullyconnectednetworkmultilabelclassifiermodel.md)
  A multi-label classifier model that uses a fully-connected network.
- [struct FullyConnectedNetworkConfiguration](fullyconnectednetworkconfiguration.md)
  A fully connected network configuration.
- [struct TreeClassifierModel](treeclassifiermodel.md)
  A trained tree classifier model.
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier)*