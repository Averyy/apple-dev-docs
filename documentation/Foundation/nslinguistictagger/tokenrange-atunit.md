# tokenRange(at:unit:)

**Framework**: Foundation  
**Kind**: method

Returns the range of the linguistic unit containing the specified character index.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func tokenRange(at charIndex: Int, unit: NSLinguisticTaggerUnit) -> NSRange
```

#### Return Value

The range of the substring for the linguistic unit.

## Parameters

- `charIndex`: The character index to begin examination.
- `unit`: The linguistic unit. For possible values, see  .

## See Also

- [func sentenceRange(for: NSRange) -> NSRange](nslinguistictagger/sentencerange(for:).md)
  Returns the range of a sentence containing the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tokenrange(at:unit:))*