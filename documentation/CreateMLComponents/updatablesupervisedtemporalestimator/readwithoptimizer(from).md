# readWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Reads the encoded transformer and optimizer from a file.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func readWithOptimizer(from url: URL) throws -> Self.Transformer
```

## Return Value

The decoded transformer.

## Parameters

- `url`: A file URL.

## See Also

### Reading and writing
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](./writewithoptimizer%28_,to,overwrite%29.md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtemporalestimator/readwithoptimizer(from:))*