# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the action classifier as a Core ML model file to the file path.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func write(toFile path: String, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `path`: The location path in the file system where you want to save the model.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

### Saving an action classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](./write%28to,metadata%29.md)
  Exports the action classifier as a Core ML model file to a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/write(tofile:metadata:))*