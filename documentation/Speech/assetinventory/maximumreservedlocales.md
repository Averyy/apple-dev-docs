# maximumReservedLocales

**Framework**: Speech  
**Kind**: property

The number of locale reservations permitted to an app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var maximumReservedLocales: Int { get }
```

#### Discussion

This value is the largest allowed count of [`reservedLocales`](assetinventory/reservedlocales.md). The value may vary between devices according to storage space.

## See Also

- [static func reserve(locale: Locale) async throws -> Bool](assetinventory/reserve(locale:).md)
  Add an asset locale to the app’s current reservations.
- [static func release(reservedLocale: Locale) async -> Bool](assetinventory/release(reservedlocale:).md)
  Removes an asset locale reservation.
- [static var reservedLocales: [Locale]](assetinventory/reservedlocales.md)
  The app’s current asset locale reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/maximumreservedlocales)*