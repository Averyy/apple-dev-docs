# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the object detector as a Core ML model file.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func write(to fileURL: URL, metadata: MLModelMetadata? = MLModelMetadata()) throws
```

## Parameters

- `fileURL`: A file-system URL.
- `metadata`: The model’s description, author, version, and license information.

## See Also

### Saving an object detector
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./write%28tofile,metadata%29.md)
  Exports the object detector as a Core ML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/write(to:metadata:))*