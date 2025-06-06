# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method

Exports the object detector as a Core ML model file.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func write(toFile path: String, metadata: MLModelMetadata? = MLModelMetadata()) throws
```

## Parameters

- `path`: A file-system path.
- `metadata`: The model’s description, author, version, and license information.

## See Also

- [func write(to: URL, metadata: MLModelMetadata?) throws](mlobjectdetector/write(to:metadata:).md)
  Exports the object detector as a Core ML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/write(tofile:metadata:))*