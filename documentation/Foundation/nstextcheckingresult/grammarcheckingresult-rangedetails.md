# grammarCheckingResult(range:details:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result with the specified array of grammatical errors.

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
class func grammarCheckingResult(range: NSRange, details: [[String : Any]]) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`grammar`](nstextcheckingresult/checkingtype/grammar.md).

## Parameters

- `range`: The range of the detected result.
- `details`: An array of details regarding the grammatical errors. This array of strings is suitable for presenting to the user.

## See Also

- [var grammarDetails: [[String : Any]]?](nstextcheckingresult/grammardetails.md)
  The details of a located grammatical type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/grammarcheckingresult(range:details:))*