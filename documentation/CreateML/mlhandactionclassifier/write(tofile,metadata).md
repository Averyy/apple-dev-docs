# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the hand action classifier as a Core ML model file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func write(toFile path: String, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `path`: A file-system path.
- `metadata`: The model’s description, author, version, and license information.

## See Also

### Saving a hand action classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](./write%28to,metadata%29.md)
  Exports the hand action classifier as a CoreML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/write(tofile:metadata:))*