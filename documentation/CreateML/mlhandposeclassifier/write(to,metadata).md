# write(to:metadata:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports the hand pose classifier as a CoreML model file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func write(to fileURL: URL, metadata: MLModelMetadata? = nil) throws
```

## Parameters

- `fileURL`: A file-system URL.
- `metadata`: The model’s description, author, version, and license information.

## See Also

### Saving a hand pose classifier
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./write%28tofile,metadata%29.md)
  Exports the hand pose classifier as a Core ML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/write(to:metadata:))*