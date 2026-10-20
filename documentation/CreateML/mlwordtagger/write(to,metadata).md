# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the word tagger as a Core ML model file at the specified URL.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func write(to fileURL: URL, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `fileURL`: The location in the file system to which the file should be written.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

### Saving a word tagger
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./write%28tofile,metadata%29.md)
  Exports the word tagger as a Core ML model file at the specified file path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/write(to:metadata:))*