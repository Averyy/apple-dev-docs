# reservedLocales

**Framework**: Speech  
**Kind**: property  
**Role**: Type Property

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

## Discussion

Before you can subscribe to assets supporting a module, you must reserve those assets’ locales. Please note, the locales returned by this method may be variants of the locales provided to [`reserve(locale:)`](./reserve%28locale%29.md).

## See Also

### Managing allocations
- [static func reserve(locale: Locale) async throws -> Bool](./reserve%28locale%29.md)
  Add an asset locale to the app’s current reservations.
- [static func release(reservedLocale: Locale) async -> Bool](./release%28reservedlocale%29.md)
  Removes an asset locale reservation.
- [static var maximumReservedLocales: Int](./maximumreservedlocales.md)
  The number of locale reservations permitted to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/reservedlocales)*