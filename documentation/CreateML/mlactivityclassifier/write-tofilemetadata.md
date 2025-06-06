# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method

Exports the activity classifier as a Core ML model file.

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

- [func write(to: URL, metadata: MLModelMetadata?) throws](mlactivityclassifier/write(to:metadata:).md)
  Exports the activity classifier as a Core ML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/write(tofile:metadata:))*