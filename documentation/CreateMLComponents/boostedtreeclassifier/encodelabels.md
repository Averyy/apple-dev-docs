# encodeLabels(_:)

**Framework**: Create ML Components  
**Kind**: method

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
func encodeLabels(_ annotations: some Collection<Optional<Label>>) throws -> (labels: [String?], encoded: [Int])
```

## See Also

- [func encode(TreeClassifierModel<Label>, to: inout any EstimatorEncoder) throws](boostedtreeclassifier/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> TreeClassifierModel<Label>](boostedtreeclassifier/decode(from:).md)
  Decodes a previously fitted transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier/encodelabels(_:))*