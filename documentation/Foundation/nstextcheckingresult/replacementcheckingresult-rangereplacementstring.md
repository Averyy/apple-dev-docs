# replacementCheckingResult(range:replacementString:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result with the specified replacement string.

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
class func replacementCheckingResult(range: NSRange, replacementString: String) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`replacement`](nstextcheckingresult/checkingtype/replacement.md).

## Parameters

- `range`: The range of the detected result.
- `replacementString`: The replacement string.

## See Also

- [var replacementString: String?](nstextcheckingresult/replacementstring.md)
  A replacement string from one of a number of replacement checking results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/replacementcheckingresult(range:replacementstring:))*