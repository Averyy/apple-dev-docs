# dashCheckingResult(range:replacementString:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result with the specified dash corrected replacement string.

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
class func dashCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`dash`](nstextcheckingresult/checkingtype/dash.md).

## Parameters

- `range`: The range of the detected result.
- `replacementString`: The replacement string.

## See Also

- [class func quoteCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult](nstextcheckingresult/quotecheckingresult(range:replacementstring:).md)
  Creates and returns a text checking result with the specified quote-balanced replacement string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/dashcheckingresult(range:replacementstring:))*