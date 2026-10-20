# Transformer

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The transformer type created by this estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
associatedtype Transformer : TemporalTransformer
```

## See Also

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](./read%28from%29.md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](./write%28_,to,overwrite%29.md)
  Writes the encoded transformer to a file.
- [associatedtype Annotation : Equatable, Sendable](./annotation.md)
  The annotation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator/transformer)*