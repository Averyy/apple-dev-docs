# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method

Exports the text classifier as a Core ML model file at the specified URL.

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

## Mentions

- [Creating a Text Classifier Model](creating-a-classification-model-for-natural-language.md)
- [Creating a text classifier model](creating-a-text-classifier-model.md)

## Parameters

- `fileURL`: The location in the file system to which the file should be written.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

- [func write(toFile: String, metadata: MLModelMetadata?) throws](mltextclassifier/write(tofile:metadata:).md)
  Exports the text classifier as a Core ML model file at the specified file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/write(to:metadata:))*