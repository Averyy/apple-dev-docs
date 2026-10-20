# MLActivityClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

A data source for an activity classifier.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum DataSource
```

## Topics

### Creating a data source
- [MLActivityClassifier.DataSource.labeledDirectories(at:)](./datasource/labeleddirectories%28at%29.md)
  An activity classifier data source that uses a directory of directories that contain sensor data files.
- [case directoryWithDataAndAnnotation(at: URL, annotationFileName: String, timeStampColumn: String, labelStartTimeColumn: String, labelEndTimeColumn: String)](./datasource/directorywithdataandannotation%28at,annotationfilename,timestampcolumn,labelstarttimecolumn,labelendtimecolumn%29.md)
  An activity classifier data source that uses a directory that contains sensor data files and one annotation file.
### Generating data tables from a data source
- [func labeledSensorData(featureColumns: [String], labelColumn: String?, recordingFileColumn: String?) throws -> MLDataTable](./datasource/labeledsensordata%28featurecolumns,labelcolumn,recordingfilecolumn%29.md)
  Generates a data table from the contents of the data source.
- [func stratifiedSplit(proportions: [Double], seed: Int, featureColumns: [String], labelColumn: String, recordingFileColumn: String) throws -> MLDataTable](./datasource/stratifiedsplit%28proportions,seed,featurecolumns,labelcolumn,recordingfilecolumn%29.md)
  Generates a data table by splitting the data source into strata.
### Gathering annotated features
- [func gatherAnnotatedFeatures(featureColumns: [String], labelColumn: String, recordingFileColumn: String?) throws -> DataFrame](./datasource/gatherannotatedfeatures%28featurecolumns,labelcolumn,recordingfilecolumn%29.md)
  Processes the data source and returns a data frame that contains features, labels and file names.
### Getting the data frame
- [MLActivityClassifier.DataSource.dataFrame(_:)](./datasource/dataframe%28_%29.md)
  An activity classifier data source that uses a data frame containing sensor features and labels.

## See Also

### Supporting types
- [MLActivityClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Model training parameters that direct the training process for an activity classifier model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource)*