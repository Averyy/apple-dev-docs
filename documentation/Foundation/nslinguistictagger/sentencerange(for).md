# sentenceRange(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the range of a sentence containing the specified range.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.7+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
func sentenceRange(for range: NSRange) -> NSRange
```

```objc
- (NSRange) sentenceRangeForRange:(NSRange) range;
```

#### Return Value

Returns the range of the sentence.

#### Discussion

This is a convenience method for calling [`tokenRange(at:unit:)`](./tokenrange%28at,unit%29.md), passing the [`NSLinguisticTaggerUnit.sentence`](../nslinguistictaggerunit/sentence.md) unit and the first position of the provided range.

## Parameters

- `range`: The character range.

## See Also

### Determining the Range of a Unit Token
- [func tokenRange(at: Int, unit: NSLinguisticTaggerUnit) -> NSRange](./tokenrange%28at,unit%29.md)
  Returns the range of the linguistic unit containing the specified character index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/sentencerange(for:))*