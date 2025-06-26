# twoDigitsNoAMPM

**Framework**: Foundation  
**Kind**: property

Custom format style portraying the numeric hour using two digits.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- visionOS 1.0+

## Declaration

```swift
static var twoDigitsNoAMPM: Date.FormatStyle.Symbol.Hour { get }
```

#### Discussion

This style pads the hour with a leading zero if necessary. It doesn’t include the day period symbol (a.m. or p.m.). For example, `01`, `11`.

## See Also

- [static var defaultDigitsNoAMPM: Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/defaultdigitsnoampm.md)
  Custom format style portraying the minimum number of digits that represents the numeric hour.
- [static func conversationalDefaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/conversationaldefaultdigits(ampm:).md)
  Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.
- [static func conversationalTwoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/conversationaltwodigits(ampm:).md)
  Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.
- [static func defaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/defaultdigits(ampm:).md)
  Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.
- [static func twoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/twodigits(ampm:).md)
  Custom format style portraying two digits that represent the hour and locale-dependent day period formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/twodigitsnoampm)*