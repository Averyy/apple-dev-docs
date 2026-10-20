# write(_:to:overwrite:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Writes the encoded transformer to a file.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func write(_ transformer: Self.Transformer, to url: URL, overwrite: Bool = true) throws
```

## Parameters

- `transformer`: A transformer created by this estimator.
- `url`: A file URL.
- `overwrite`: A Boolean value indicating whether to overwrite existing files.

## See Also

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](./read%28from%29.md)
  Reads the encoded transformer from a file.
- [associatedtype Annotation : Equatable, Sendable](./annotation.md)
  The annotation type.
- [associatedtype Transformer : TemporalTransformer](./transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator/write(_:to:overwrite:))*