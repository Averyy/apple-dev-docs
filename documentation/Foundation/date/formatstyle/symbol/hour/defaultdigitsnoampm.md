# defaultDigitsNoAMPM

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Custom format style portraying the minimum number of digits that represents the numeric hour.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var defaultDigitsNoAMPM: Date.FormatStyle.Symbol.Hour { get }
```

## Discussion

This style doesn’t include the day period symbol (a.m. or p.m.). For example, `1`, `11`.

## See Also

### Modifying an Hour
- [static var twoDigitsNoAMPM: Date.FormatStyle.Symbol.Hour](./twodigitsnoampm.md)
  Custom format style portraying the numeric hour using two digits.
- [static func conversationalDefaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./conversationaldefaultdigits%28ampm%29.md)
  Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.
- [static func conversationalTwoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./conversationaltwodigits%28ampm%29.md)
  Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.
- [static func defaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./defaultdigits%28ampm%29.md)
  Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.
- [static func twoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./twodigits%28ampm%29.md)
  Custom format style portraying two digits that represent the hour and locale-dependent day period formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/defaultdigitsnoampm)*