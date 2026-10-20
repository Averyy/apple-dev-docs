# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

- [Creating a text classifier model](../creating-a-text-classifier-model.md)
- [Creating a word tagger model](../creating-a-word-tagger-model.md)

## Parameters

- `fileURL`: The location in the file system to which the file should be written.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

### Saving a text classifier
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./write%28tofile,metadata%29.md)
  Exports the text classifier as a Core ML model file at the specified file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/write(to:metadata:))*