# quarterSymbols

**Framework**: Foundation  
**Kind**: property

A list of quarter names in this calendar, localized to the Calendar’s `locale`.

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
var quarterSymbols: [String] { get }
```

#### Discussion

For example, for English in the Gregorian calendar, returns `["1st quarter", "2nd quarter", "3rd quarter", "4th quarter"]`.

> **Note**:  By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

- [var shortQuarterSymbols: [String]](calendar/shortquartersymbols.md)
  A list of shorter-named quarters in this calendar, localized to the Calendar’s `locale`.
- [var standaloneQuarterSymbols: [String]](calendar/standalonequartersymbols.md)
  A list of standalone quarter names in this calendar, localized to the Calendar’s `locale`.
- [var shortStandaloneQuarterSymbols: [String]](calendar/shortstandalonequartersymbols.md)
  A list of shorter-named standalone quarters in this calendar, localized to the Calendar’s `locale`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/quartersymbols)*