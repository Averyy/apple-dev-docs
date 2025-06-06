# veryShortMonthSymbols

**Framework**: Foundation  
**Kind**: property

A list of very-shortly-named months in this calendar, localized to the Calendar’s `locale`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var veryShortMonthSymbols: [String] { get }
```

#### Discussion

For example, for English in the Gregorian calendar, returns `["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]`.

> **Note**:  By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

 By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

- [var monthSymbols: [String]](calendar/monthsymbols.md)
  A list of months in this calendar, localized to the Calendar’s `locale`.
- [var shortMonthSymbols: [String]](calendar/shortmonthsymbols.md)
  A list of shorter-named months in this calendar, localized to the Calendar’s `locale`.
- [var standaloneMonthSymbols: [String]](calendar/standalonemonthsymbols.md)
  A list of standalone months in this calendar, localized to the Calendar’s `locale`.
- [var shortStandaloneMonthSymbols: [String]](calendar/shortstandalonemonthsymbols.md)
  A list of shorter-named standalone months in this calendar, localized to the Calendar’s `locale`.
- [var veryShortStandaloneMonthSymbols: [String]](calendar/veryshortstandalonemonthsymbols.md)
  A list of very-shortly-named standalone months in this calendar, localized to the Calendar’s `locale`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/veryshortmonthsymbols)*