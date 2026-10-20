# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

### Saving an activity classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](./write%28to,metadata%29.md)
  Exports the activity classifier as a Core ML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/write(tofile:metadata:))*