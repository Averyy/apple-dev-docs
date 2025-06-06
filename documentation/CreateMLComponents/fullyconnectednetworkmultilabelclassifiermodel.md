# FullyConnectedNetworkMultiLabelClassifierModel

**Framework**: Create ML Components  
**Kind**: struct

A multi-label classifier model that uses a fully-connected network.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint, Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Topics

### Performing a classification
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) throws -> ClassificationDistribution<Label>](fullyconnectednetworkmultilabelclassifiermodel/applied(to:eventhandler:).md)
  Performs a classification on a shaped array.
### Computing evaluation metrics
- [func evaluation(on: some Collection<AnnotatedFeature<MLShapedArray<Scalar>, Set<Label>>>, confidenceThresholds: [Label : Float]) throws -> MultiLabelClassificationMetrics<Label>](fullyconnectednetworkmultilabelclassifiermodel/evaluation(on:confidencethresholds:).md)
  Computes evaluation metrics on annotated examples.
### Performing a prediction
- [func prediction<S>(from: S, confidenceThresholds: [Label : Scalar]) throws -> [ClassificationDistribution<Label>]](fullyconnectednetworkmultilabelclassifiermodel/prediction(from:confidencethresholds:)-3kiaw.md)
  Performs a sequence of predictions and keeps label-confidence pairs that are greater than or equal to the provided confidence thresholds.
- [func prediction(from: FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>.Input, confidenceThresholds: [Label : Scalar]) throws -> ClassificationDistribution<Label>](fullyconnectednetworkmultilabelclassifiermodel/prediction(from:confidencethresholds:)-57mka.md)
  Performs a prediction and keeps label-confidence pairs that are greater than or equal to the provided confidence thresholds.
### Updating the precision recall curve
- [func updatePrecisionRecallCurves(some Collection<AnnotatedFeature<MLShapedArray<Scalar>, Set<Label>>>) async throws](fullyconnectednetworkmultilabelclassifiermodel/updateprecisionrecallcurves(_:).md)
  Updates the per-label precision-recall curve using the input data.
### Type Aliases
- [FullyConnectedNetworkMultiLabelClassifierModel.Input](fullyconnectednetworkmultilabelclassifiermodel/input.md)
  The input type.
- [FullyConnectedNetworkMultiLabelClassifierModel.Output](fullyconnectednetworkmultilabelclassifiermodel/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](fullyconnectednetworkmultilabelclassifiermodel/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](fullyconnectednetworkmultilabelclassifiermodel/decodable-implementations.md)
- [Encodable Implementations](fullyconnectednetworkmultilabelclassifiermodel/encodable-implementations.md)
- [Transformer Implementations](fullyconnectednetworkmultilabelclassifiermodel/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [Transformer](transformer.md)

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
- [struct FullyConnectedNetworkConfiguration](fullyconnectednetworkconfiguration.md)
  A fully connected network configuration.
- [struct TreeClassifierModel](treeclassifiermodel.md)
  A trained tree classifier model.
- [struct TimeSeriesClassifier](timeseriesclassifier.md)
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifiermodel)*