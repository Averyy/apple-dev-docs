# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the image classifier as a Core ML model file to a location in the file system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func write(to fileURL: URL, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `fileURL`: The location URL in the file system where you want to save the model.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

### Saving an image classifier
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./write%28tofile,metadata%29.md)
  Exports the image classifier as a Core ML model file to the file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/write(to:metadata:))*