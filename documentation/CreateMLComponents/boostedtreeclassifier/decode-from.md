# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes a previously fitted transformer.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> TreeClassifierModel<Label>
```

## See Also

- [func encode(TreeClassifierModel<Label>, to: inout any EstimatorEncoder) throws](boostedtreeclassifier/encode(_:to:).md)
  Encodes a fitted transformer.
- [func encodeLabels(some Collection<Optional<Label>>) throws -> (labels: [String?], encoded: [Int])](boostedtreeclassifier/encodelabels(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier/decode(from:))*