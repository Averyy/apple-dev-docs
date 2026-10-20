# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the gazetteer as a Core ML model file at the specified file path.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func write(toFile path: String, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `path`: A file system path where the model file should be written.
- `metadata`: Descriptive information to include with the exported model file.

## See Also

### Saving a gazetteer
- [func write(to: URL, metadata: MLModelMetadata?) throws](./write%28to,metadata%29.md)
  Exports the gazetteer as a Core ML model file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/write(tofile:metadata:))*