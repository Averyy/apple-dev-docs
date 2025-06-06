# longEraSymbols

**Framework**: Foundation  
**Kind**: property

A list of longer-named eras in this calendar, localized to the Calendar’s `locale`.

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
var longEraSymbols: [String] { get }
```

#### Discussion

For example, for English in the Gregorian calendar, returns `["Before Christ", "Anno Domini"]`.

> **Note**:  By default, Calendars have no locale set. If you wish to receive a localized answer, be sure to set the `locale` property first - most likely to `Locale.autoupdatingCurrent`.

## See Also

- [var eraSymbols: [String]](calendar/erasymbols.md)
  A list of eras in this calendar, localized to the Calendar’s `locale`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/longerasymbols)*