# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the action classifier as a Core ML model file to a location in the file system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func write(to fileURL: URL, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `fileURL`: The location URL in the file system where you want to save the model.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

### Saving an action classifier
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./write%28tofile,metadata%29.md)
  Exports the action classifier as a Core ML model file to the file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/write(to:metadata:))*