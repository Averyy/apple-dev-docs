# Transformer

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Required**: Yes

The transformer type created by this estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
associatedtype Transformer : TemporalTransformer
```

## See Also

- [func read(from: URL) throws -> Self.Transformer](supervisedtemporalestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](supervisedtemporalestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
- [associatedtype Annotation : Equatable, Sendable](supervisedtemporalestimator/annotation.md)
  The annotation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator/transformer)*