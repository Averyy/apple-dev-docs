# labelColumn

**Framework**: Createml  
**Kind**: property

The name of the label column the activity classifier used during its training session.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var labelColumn: String
```

#### Discussion

This property reflects the name of the data table column or annotation file column the training session used to label each activity.

> **Note**: The [`MLActivityClassifier`](mlactivityclassifier.md) instance provides a default name if you trained it with a data source that’s set to [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](mlactivityclassifier/datasource/labeleddirectories(at:).md).

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

- [var model: MLModel](mlactivityclassifier/model.md)
  The underlying Core ML model of the activity classifier stored in memory.
- [let modelParameters: MLActivityClassifier.ModelParameters](mlactivityclassifier/modelparameters-swift.property.md)
  The model configuration parameters the activity classifier used during its training session.
- [var featureColumns: [String]](mlactivityclassifier/featurecolumns.md)
  The names of the feature columns the activity classifier used during its training session.
- [var recordingFileColumn: String](mlactivityclassifier/recordingfilecolumn.md)
  The name of the column that contains the data files the activity classifier used during its training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/labelcolumn)*