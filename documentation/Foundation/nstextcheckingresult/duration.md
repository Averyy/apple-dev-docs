# duration

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The duration component of a type checking result.

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
var duration: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval duration;
```

## See Also

### Text Checking Results for Dates and Times
- [class func dateCheckingResult(range: NSRange, date: Date) -> NSTextCheckingResult](./datecheckingresult%28range,date%29.md)
  Creates and returns a text checking result with the specified date.
- [class func dateCheckingResult(range: NSRange, date: Date, timeZone: TimeZone, duration: TimeInterval) -> NSTextCheckingResult](./datecheckingresult%28range,date,timezone,duration%29.md)
  Creates and returns a text checking result with the specified date, time zone, and duration.
- [var date: Date?](./date.md)
  The date component of a type checking result.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone component of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/duration)*