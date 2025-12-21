# TreeClassifierModel

**Framework**: Create ML Components  
**Kind**: struct

A trained tree classifier model.

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
struct TreeClassifierModel<Label> where Label : Hashable
```

## Topics

### Getting the properties
- [var classCount: Int](treeclassifiermodel/classcount.md)
  The number of classes.
- [var featureColumnNames: [String]](treeclassifiermodel/featurecolumnnames.md)
  The names of the columns containing feature values.
- [var predictionColumnName: String](treeclassifiermodel/predictioncolumnname.md)
  The name of the column containing the predicted labels.
### Building a data frame
- [func buildDataFrame([ClassificationDistribution<Label>]) -> DataFrame](treeclassifiermodel/builddataframe(_:).md)
  Builds a data frame containing a labels column and a probability distribution column.
### Applying
- [func applied(to: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](treeclassifiermodel/applied(to:eventhandler:).md)
  Performs a classification on a data frame.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabularTransformer](tabulartransformer.md)
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
- [struct FullyConnectedNetworkMultiLabelClassifierModel](fullyconnectednetworkmultilabelclassifiermodel.md)
  A multi-label classifier model that uses a fully-connected network.
- [struct FullyConnectedNetworkConfiguration](fullyconnectednetworkconfiguration.md)
  A fully connected network configuration.
- [struct TimeSeriesClassifier](timeseriesclassifier.md)
- [struct TimeSeriesClassifierConfiguration](timeseriesclassifierconfiguration.md)
  The configuration for a time-series classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/treeclassifiermodel)*