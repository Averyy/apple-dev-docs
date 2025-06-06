# LogisticRegressionClassifierModel

**Framework**: Create ML Components  
**Kind**: struct

A trained logistic regression classifier model.

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
struct LogisticRegressionClassifierModel<Scalar, Label> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint, Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Topics

### Creating a regression model
- [init(coefficients: some Sequence<Scalar>, labels: Set<Label>)](logisticregressionclassifiermodel/init(coefficients:labels:).md)
  Creates a logistic regression model.
### Getting the properties
- [var coefficients: [Scalar]](logisticregressionclassifiermodel/coefficients.md)
  The linear coefficients.
- [var featureCount: Int](logisticregressionclassifiermodel/featurecount.md)
  The number of features expected in the input.
### Performing the classification
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> ClassificationDistribution<Label>](logisticregressionclassifiermodel/applied(to:eventhandler:).md)
  Performs a classification on a single input.
- [LogisticRegressionClassifierModel.Input](logisticregressionclassifiermodel/input.md)
  The input type.
### Type Aliases
- [LogisticRegressionClassifierModel.Output](logisticregressionclassifiermodel/output.md)
  The output type.
### Default Implementations
- [Transformer Implementations](logisticregressionclassifiermodel/transformer-implementations.md)

## Relationships

### Conforms To
- [Classifier](classifier.md)
- [Sendable](../Swift/Sendable.md)
- [Transformer](transformer.md)

## See Also

- [protocol Classifier](classifier.md)
  An estimator that predicts classification probabilities.
- [struct LogisticRegressionClassifier](logisticregressionclassifier.md)
  A logistic regression classifier.
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
- [struct TimeSeriesClassifier](timeseriesclassifier.md)
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifiermodel)*