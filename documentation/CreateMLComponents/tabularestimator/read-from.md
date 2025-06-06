# read(from:)

**Framework**: Create ML Components  
**Kind**: method

Reads the encoded transformer from a file.

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
func read(from url: URL) throws -> Self.Transformer
```

#### Return Value

The decoded transformer.

## Parameters

- `url`: A file URL.

## See Also

- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](tabularestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
- [associatedtype Transformer : TabularTransformer](tabularestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimator/read(from:))*