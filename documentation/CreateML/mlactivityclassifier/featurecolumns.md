# featureColumns

**Framework**: Create ML  
**Kind**: property

The names of the feature columns the activity classifier used during its training session.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var featureColumns: [String]
```

#### Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

- [var model: MLModel](mlactivityclassifier/model.md)
  The underlying Core ML model of the activity classifier stored in memory.
- [let modelParameters: MLActivityClassifier.ModelParameters](mlactivityclassifier/modelparameters-swift.property.md)
  The model configuration parameters the activity classifier used during its training session.
- [var labelColumn: String](mlactivityclassifier/labelcolumn.md)
  The name of the label column the activity classifier used during its training session.
- [var recordingFileColumn: String](mlactivityclassifier/recordingfilecolumn.md)
  The name of the column that contains the data files the activity classifier used during its training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/featurecolumns)*