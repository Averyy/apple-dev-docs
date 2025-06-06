# correctionCheckingResult(range:replacementString:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result after detecting a possible correction.

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
class func correctionCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`spelling`](nstextcheckingresult/checkingtype/spelling.md).

## Parameters

- `range`: The range of the detected result.
- `replacementString`: The suggested replacement string.

## See Also

- [var replacementString: String?](nstextcheckingresult/replacementstring.md)
  A replacement string from one of a number of replacement checking results.
- [class func spellCheckingResult(range: NSRange) -> NSTextCheckingResult](nstextcheckingresult/spellcheckingresult(range:).md)
  Creates and returns a text checking result with the range of a misspelled word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/correctioncheckingresult(range:replacementstring:))*