# targetColumn

**Framework**: Create ML  
**Kind**: property

The name of the column you selected at initialization to define which categories the classifier predicts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var targetColumn: String
```

#### Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

- [init(checkpoint: MLCheckpoint) throws](mlboostedtreeclassifier/init(checkpoint:).md)
  Creates a boosted tree classifier from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters) throws](mlboostedtreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-11dpb.md)
  Creates a boosted tree classifier.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeClassifier>](mlboostedtreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-334sj.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeClassifier>](mlboostedtreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7et81.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeClassifier>](mlboostedtreeclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLBoostedTreeClassifier>) throws -> MLJob<MLBoostedTreeClassifier>](mlboostedtreeclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeClassifier>](mlboostedtreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-79pib.md)
  Trains a boosted tree classifier.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeClassifier>](mlboostedtreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-9sfj7.md)
  Trains a boosted tree classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters) throws](mlboostedtreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-8w2dm.md)
  Creates a Boosted Tree Classifier from the feature columns in the training data to predict the categories in the target column.
- [MLBoostedTreeClassifier.ModelParameters](mlboostedtreeclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLBoostedTreeClassifier.ModelParameters](mlboostedtreeclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var featureColumns: [String]](mlboostedtreeclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/targetcolumn)*