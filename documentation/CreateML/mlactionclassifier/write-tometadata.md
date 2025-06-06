# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method

Exports the action classifier as a Core ML model file to a location in the file system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func write(to fileURL: URL, metadata: MLModelMetadata? = nil) throws
```

#### Discussion

- fileURL: The location URL in the file system where you want to save the model.
- metadata: Descriptive information to include with the exported model file.

## See Also

- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlactionclassifier/write(tofile:metadata:).md)
  Exports the action classifier as a Core ML model file to the file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/write(to:metadata:))*