# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method

Exports the text classifier as a Core ML model file at the specified file path.

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

- `path`: A file system path where the model file should be written.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

- [func write(to: URL, metadata: MLModelMetadata?) throws](mltextclassifier/write(to:metadata:).md)
  Exports the text classifier as a Core ML model file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/write(tofile:metadata:))*