# modelParameters

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The model configuration parameters the activity classifier used during its training session.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
(unsafe) let modelParameters: MLActivityClassifier.ModelParameters
```

## See Also

### Inspecting an activity classifier model
- [var model: MLModel](./model.md)
  The underlying Core ML model of the activity classifier stored in memory.
- [var featureColumns: [String]](./featurecolumns.md)
  The names of the feature columns the activity classifier used during its training session.
- [var labelColumn: String](./labelcolumn.md)
  The name of the label column the activity classifier used during its training session.
- [var recordingFileColumn: String](./recordingfilecolumn.md)
  The name of the column that contains the data files the activity classifier used during its training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/modelparameters-swift.property)*