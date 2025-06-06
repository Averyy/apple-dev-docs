# write(_:to:overwrite:)

**Framework**: Create ML Components  
**Kind**: method

Writes the encoded transformer to a file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func write(_ transformer: Self.Transformer, to url: URL, overwrite: Bool = true) throws
```

## Parameters

- `transformer`: A transformer created by this estimator.
- `url`: A file URL.
- `overwrite`: A Boolean value indicating whether to overwrite existing files.

## See Also

- [func read(from: URL) throws -> Self.Transformer](supervisedtemporalestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [associatedtype Annotation : Equatable, Sendable](supervisedtemporalestimator/annotation.md)
  The annotation type.
- [associatedtype Transformer : TemporalTransformer](supervisedtemporalestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator/write(_:to:overwrite:))*