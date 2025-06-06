# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method

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

- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlobjectdetector/write(tofile:metadata:).md)
  Exports the object detector as a Core ML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/write(to:metadata:))*