# pmSymbol

**Framework**: Foundation  
**Kind**: property

The symbol used to represent “PM”, localized to the Calendar’s `locale`.

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
var pmSymbol: String { get }
```

#### Discussion

For example, for English in the Gregorian calendar, returns `"PM"`.

> **Note**:  By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

- [var amSymbol: String](calendar/amsymbol.md)
  The symbol used to represent “AM”, localized to the Calendar’s `locale`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/pmsymbol)*