# init(trainingData:featureColumns:labelColumn:recordingFileColumn:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates an activity classifier with a training dataset represented by a data table.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(trainingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String, parameters: MLActivityClassifier.ModelParameters = ModelParameters(validationData: nil)) throws
```

#### Discussion

Use this initializer to create an activity classifier with an [`MLDataTable`](mldatatable.md). To configure the training process, initialize the activity classifier with an [`MLActivityClassifier.ModelParameters`](mlactivityclassifier/modelparameters-swift.struct.md) instance. For example, you can explicitly define the validation dataset instead of allowing the model to choose a random selection of your training data. Alternatively, set [`validationData`](mlactivityclassifier/modelparameters-swift.struct/validationdata.md) to `nil` to allow the activity classifier to choose the validation data for you from among your training data. This lets you set other parameters — like [`maximumIterations`](mlactivityclassifier/modelparameters-swift.struct/maximumiterations.md) and [`batchSize`](mlactivityclassifier/modelparameters-swift.struct/batchsize.md) — to nondefault values.

## Parameters

- `trainingData`: An   that contains a collection of sensor data that groups data entries by   activity label.
- `featureColumns`: The names of the columns in the data table that contain sensor data.
- `labelColumn`: The name of the column in the data table that contains activity labels.
- `recordingFileColumn`: The name of the column in the data table that contains data filenames.
- `parameters`: An   instance you use to configure the   model for the training session.

## See Also

- [init(trainingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String?, recordingFileColumn: String?, parameters: MLActivityClassifier.ModelParameters) throws](mlactivityclassifier/init(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:)-6ltei.md)
  Creates an activity classifier with a training dataset represented by a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/init(trainingdata:featurecolumns:labelcolumn:recordingfilecolumn:parameters:)-1z9ai)*