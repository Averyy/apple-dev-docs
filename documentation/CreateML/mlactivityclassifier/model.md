# model

**Framework**: Create ML  
**Kind**: property

The underlying Core ML model of the activity classifier stored in memory.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var model: MLModel { get set }
```

## See Also

- [let modelParameters: MLActivityClassifier.ModelParameters](mlactivityclassifier/modelparameters-swift.property.md)
  The model configuration parameters the activity classifier used during its training session.
- [var featureColumns: [String]](mlactivityclassifier/featurecolumns.md)
  The names of the feature columns the activity classifier used during its training session.
- [var labelColumn: String](mlactivityclassifier/labelcolumn.md)
  The name of the label column the activity classifier used during its training session.
- [var recordingFileColumn: String](mlactivityclassifier/recordingfilecolumn.md)
  The name of the column that contains the data files the activity classifier used during its training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/model)*