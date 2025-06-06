# init(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates an activity classifier with a training dataset represented by a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String? = nil, recordingFileColumn: String? = nil, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil)) throws
```

#### Discussion

Use this initializer to create an activity classifier with an [`MLActivityClassifier.DataSource`](mlactivityclassifier/datasource.md). To configure the training process, initialize the activity classifier with an [`MLActivityClassifier.ModelParameters`](mlactivityclassifier/modelparameters-swift.struct.md) instance. For example, you can explicitly define the validation dataset instead of allowing the model to choose a random selection of your training data. Alternatively, set [`validationData`](mlactivityclassifier/modelparameters-swift.struct/validationdata.md) to `nil` to allow the activity classifier to choose the validation data for you from among your training data. This lets you set other parameters — like [`maximumIterations`](mlactivityclassifier/modelparameters-swift.struct/maximumiterations.md) and [`batchSize`](mlactivityclassifier/modelparameters-swift.struct/batchsize.md) — to nondefault values.

## Parameters

- `trainingData`: An   instance.
- `featureColumns`: The names of the columns in an annotation file that contain sensor data.
- `labelColumn`: The initializer ignores this parameter if   uses   .
- `recordingFileColumn`: The initializer ignores this parameter if   uses   .
- `parameters`: An   instance you use to configure the   model for the training session.

## See Also

- [init(trainingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters) throws](mlactivityclassifier/init(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:)-1z9ai.md)
  Creates an activity classifier with a training dataset represented by a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/init(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:)-6ltei)*