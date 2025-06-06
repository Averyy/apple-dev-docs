# FullyConnectedNetworkClassifierModel

**Framework**: Create ML Components  
**Kind**: struct

A classifier model that uses a fully connected network.

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
struct FullyConnectedNetworkClassifierModel<Scalar, Label> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint, Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Topics

### Creating a classifier model
- [init(from: any Decoder) throws](fullyconnectednetworkclassifiermodel/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Applying a classification
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> ClassificationDistribution<Label>](fullyconnectednetworkclassifiermodel/applied(to:eventhandler:).md)
  Performs a classification on a shaped array.
### Type Aliases
- [FullyConnectedNetworkClassifierModel.Input](fullyconnectednetworkclassifiermodel/input.md)
  The input type.
- [FullyConnectedNetworkClassifierModel.Output](fullyconnectednetworkclassifiermodel/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](fullyconnectednetworkclassifiermodel/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](fullyconnectednetworkclassifiermodel/decodable-implementations.md)
- [Encodable Implementations](fullyconnectednetworkclassifiermodel/encodable-implementations.md)
- [Transformer Implementations](fullyconnectednetworkclassifiermodel/transformer-implementations.md)

## Relationships

### Conforms To
- [Classifier](classifier.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifiermodel)*