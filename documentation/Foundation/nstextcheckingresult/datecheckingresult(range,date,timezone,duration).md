# dateCheckingResult(range:date:timeZone:duration:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSTextCheckingResult *) dateCheckingResultWithRange:(NSRange) range date:(NSDate *) date timeZone:(NSTimeZone *) timeZone duration:(NSTimeInterval) duration;
```

## Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](./range.md) and a [`resultType`](./resulttype.md) of [`date`](./checkingtype/date.md).

## Parameters

- `range`: The range of the detected result.
- `date`: The detected date.
- `timeZone`: The detected time zone.
- `duration`: The detected duration.

## See Also

### Text Checking Results for Dates and Times
- [class func dateCheckingResult(range: NSRange, date: Date) -> NSTextCheckingResult](./datecheckingresult%28range,date%29.md)
  Creates and returns a text checking result with the specified date.
- [var date: Date?](./date.md)
  The date component of a type checking result.
- [var duration: TimeInterval](./duration.md)
  The duration component of a type checking result.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone component of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/datecheckingresult(range:date:timezone:duration:))*