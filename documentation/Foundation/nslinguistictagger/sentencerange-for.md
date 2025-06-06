# sentenceRange(for:)

**Framework**: Foundation  
**Kind**: method

Returns the range of a sentence containing the specified range.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sentenceRange(for range: NSRange) -> NSRange
```

#### Return Value

Returns the range of the sentence.

#### Discussion

This is a convenience method for calling [`tokenRange(at:unit:)`](nslinguistictagger/tokenrange(at:unit:).md), passing the [`NSLinguisticTaggerUnit.sentence`](nslinguistictaggerunit/sentence.md) unit and the first position of the provided range.

## Parameters

- `range`: The character range.

## See Also

- [func tokenRange(at: Int, unit: NSLinguisticTaggerUnit) -> NSRange](nslinguistictagger/tokenrange(at:unit:).md)
  Returns the range of the linguistic unit containing the specified character index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/sentencerange(for:))*