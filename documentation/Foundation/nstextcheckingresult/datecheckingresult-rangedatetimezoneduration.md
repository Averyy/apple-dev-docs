# dateCheckingResult(range:date:timeZone:duration:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result with the specified date, time zone, and duration.

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
class func dateCheckingResult(range: NSRange, date: Date, timeZone: TimeZone, duration: TimeInterval) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`date`](nstextcheckingresult/checkingtype/date.md).

## Parameters

- `range`: The range of the detected result.
- `date`: The detected date.
- `timeZone`: The detected time zone.
- `duration`: The detected duration.

## See Also

- [class func dateCheckingResult(range: NSRange, date: Date) -> NSTextCheckingResult](nstextcheckingresult/datecheckingresult(range:date:).md)
  Creates and returns a text checking result with the specified date.
- [var date: Date?](nstextcheckingresult/date.md)
  The date component of a type checking result.
- [var duration: TimeInterval](nstextcheckingresult/duration.md)
  The duration component of a type checking result.
- [var timeZone: TimeZone?](nstextcheckingresult/timezone.md)
  The time zone component of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/datecheckingresult(range:date:timezone:duration:))*