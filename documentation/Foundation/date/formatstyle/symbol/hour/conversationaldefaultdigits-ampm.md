# conversationalDefaultDigits(amPM:)

**Framework**: Foundation  
**Kind**: method

Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.

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
static func conversationalDefaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour
```

#### Return Value

An hour format style customized according to the specified day period format style and the given locale.

#### Discussion

This format may include the day period symbol (a.m. or p.m.), depending on locale, and can include conversational period formats. For example, `7a` (`narrow`), `7AM` (`abbreviated`), `7A.M.` (`wide`).

## Parameters

- `amPM`: Specifies the format of the day period representation.

## See Also

- [static var defaultDigitsNoAMPM: Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/defaultdigitsnoampm.md)
  Custom format style portraying the minimum number of digits that represents the numeric hour.
- [static var twoDigitsNoAMPM: Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/twodigitsnoampm.md)
  Custom format style portraying the numeric hour using two digits.
- [static func conversationalTwoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/conversationaltwodigits(ampm:).md)
  Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.
- [static func defaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/defaultdigits(ampm:).md)
  Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.
- [static func twoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour/twodigits(ampm:).md)
  Custom format style portraying two digits that represent the hour and locale-dependent day period formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/conversationaldefaultdigits(ampm:))*