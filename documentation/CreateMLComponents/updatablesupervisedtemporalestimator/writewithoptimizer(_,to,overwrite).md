# writeWithOptimizer(_:to:overwrite:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Writes the encoded transformer and optimizer to a file.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func writeWithOptimizer(_ transformer: Self.Transformer, to url: URL, overwrite: Bool = true) throws
```

## Parameters

- `transformer`: A transformer created by this estimator.
- `url`: A file URL.
- `overwrite`: A Boolean value indicating whether to overwrite existing files.

## See Also

### Reading and writing
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](./readwithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtemporalestimator/writewithoptimizer(_:to:overwrite:))*