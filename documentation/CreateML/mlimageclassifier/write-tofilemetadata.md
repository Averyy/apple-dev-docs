# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method

Exports the image classifier as a Core ML model file to the file path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func write(toFile path: String, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `path`: The location path in the file system where you want to save the model.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

- [func write(to: URL, metadata: MLModelMetadata?) throws](mlimageclassifier/write(to:metadata:).md)
  Exports the image classifier as a Core ML model file to a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/write(tofile:metadata:))*