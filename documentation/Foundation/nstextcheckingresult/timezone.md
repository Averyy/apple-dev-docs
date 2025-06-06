# timeZone

**Framework**: Foundation  
**Kind**: property

The time zone component of a type checking result.

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
var timeZone: TimeZone? { get }
```

## See Also

- [class func dateCheckingResult(range: NSRange, date: Date) -> NSTextCheckingResult](nstextcheckingresult/datecheckingresult(range:date:).md)
  Creates and returns a text checking result with the specified date.
- [class func dateCheckingResult(range: NSRange, date: Date, timeZone: TimeZone, duration: TimeInterval) -> NSTextCheckingResult](nstextcheckingresult/datecheckingresult(range:date:timezone:duration:).md)
  Creates and returns a text checking result with the specified date, time zone, and duration.
- [var date: Date?](nstextcheckingresult/date.md)
  The date component of a type checking result.
- [var duration: TimeInterval](nstextcheckingresult/duration.md)
  The duration component of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/timezone)*