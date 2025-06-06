# spellCheckingResult(range:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result with the range of a misspelled word.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func spellCheckingResult(range: NSRange) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`spelling`](nstextcheckingresult/checkingtype/spelling.md).

## Parameters

- `range`: The range of the detected result.

## See Also

- [class func correctionCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult](nstextcheckingresult/correctioncheckingresult(range:replacementstring:).md)
  Creates and returns a text checking result after detecting a possible correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/spellcheckingresult(range:))*