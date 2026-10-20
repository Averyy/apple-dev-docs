# MLSupportVectorClassifier

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

A classifier that predicts a binary target value by maximizing the separation between categories.

**Availability**:
- macOS 10.14+ - Deprecated in 14.0

## Declaration

```swift
struct MLSupportVectorClassifier
```

## Topics

### Creating and training a support vector classifier
- [init(trainingData:targetColumn:featureColumns:parameters:)](./mlsupportvectorclassifier/init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a support vector classifier.
- [MLSupportVectorClassifier.ModelParameters](./mlsupportvectorclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLSupportVectorClassifier.ModelParameters](./mlsupportvectorclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](./mlsupportvectorclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](./mlsupportvectorclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Evaluating a support vector classifier
- [func evaluation(on:)](./mlsupportvectorclassifier/evaluation%28on%29.md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLClassifierMetrics](./mlsupportvectorclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](./mlsupportvectorclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Testing a support vector classifier
- [func predictions(from:)](./mlsupportvectorclassifier/predictions%28from%29.md)
  Predicts a column of labels for the given testing data.
### Saving a support vector classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](./mlsupportvectorclassifier/write%28to,metadata%29.md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./mlsupportvectorclassifier/write%28tofile,metadata%29.md)
  Exports a Core ML model file for use in your app.
### Describing a support vector classifier
- [var model: MLModel](./mlsupportvectorclassifier/model.md)
  The Core ML model.
- [var description: String](./mlsupportvectorclassifier/description.md)
  A text representation of the support vector classifier.
- [var debugDescription: String](./mlsupportvectorclassifier/debugdescription.md)
  A text representation of the support vector classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](./mlsupportvectorclassifier/playgrounddescription.md)
  A description of the support vector classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./mlsupportvectorclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./mlsupportvectorclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./mlsupportvectorclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting classifier types
- [struct MLDecisionTreeClassifier](./mldecisiontreeclassifier.md)
  A classifier that predicts the target by creating rules to split the data.
- [struct MLRandomForestClassifier](./mlrandomforestclassifier.md)
  A classifier based on a collection of decision trees trained on subsets of the data.
- [struct MLBoostedTreeClassifier](./mlboostedtreeclassifier.md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [struct MLLogisticRegressionClassifier](./mllogisticregressionclassifier.md)
  A classifier that predicts a discrete target value as a function of data features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier)*