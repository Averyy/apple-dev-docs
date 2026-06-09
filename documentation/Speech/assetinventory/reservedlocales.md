# reservedLocales

**Framework**: Speech  
**Kind**: property

The app’s current asset locale reservations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var reservedLocales: [Locale] { get async }
```

#### Discussion

Before you can subscribe to assets supporting a module, you must reserve those assets’ locales. Please note, the locales returned by this method may be variants of the locales provided to [`reserve(locale:)`](assetinventory/reserve(locale:).md).

## See Also

- [static func reserve(locale: Locale) async throws -> Bool](assetinventory/reserve(locale:).md)
  Add an asset locale to the app’s current reservations.
- [static func release(reservedLocale: Locale) async -> Bool](assetinventory/release(reservedlocale:).md)
  Removes an asset locale reservation.
- [static var maximumReservedLocales: Int](assetinventory/maximumreservedlocales.md)
  The number of locale reservations permitted to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/reservedlocales)*