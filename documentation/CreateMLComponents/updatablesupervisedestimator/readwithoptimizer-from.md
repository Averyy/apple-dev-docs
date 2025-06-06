# readWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method

Reads the encoded transformer and optimizer from a file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func readWithOptimizer(from url: URL) throws -> Self.Transformer
```

#### Return Value

The decoded transformer.

## Parameters

- `url`: A file URL.

## See Also

- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](updatablesupervisedestimator/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimator/readwithoptimizer(from:))*