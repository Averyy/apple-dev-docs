# write(toFile:metadata:)

**Framework**: Create ML  
**Kind**: method

Exports the recommender as a Core ML model file at the given file path.

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

- [func write(to: URL, metadata: MLModelMetadata?) throws](mlrecommender/write(to:metadata:).md)
  Exports the recommender as a Core ML model file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/write(tofile:metadata:))*