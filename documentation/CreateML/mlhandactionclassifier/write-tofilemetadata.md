# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method

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

- [func write(to: URL, metadata: MLModelMetadata?) throws](mlhandactionclassifier/write(to:metadata:).md)
  Exports the hand action classifier as a CoreML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/write(tofile:metadata:))*