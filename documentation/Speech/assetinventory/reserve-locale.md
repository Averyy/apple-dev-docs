# reserve(locale:)

**Framework**: Speech  
**Kind**: method

Add an asset locale to the app’s current reservations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@discardableResult
static func reserve(locale: Locale) async throws -> Bool
```

#### Return Value

`false` if the locale was already reserved.

#### Discussion

If an asset that supports the input locale exists, adds that asset’s locale to [`reservedLocales`](assetinventory/reservedlocales.md).

> **Note**: An error if the number of locales would exceed [`maximumReservedLocales`](assetinventory/maximumreservedlocales.md) or if there is no asset that can support the locale.

## See Also

- [static func release(reservedLocale: Locale) async -> Bool](assetinventory/release(reservedlocale:).md)
  Removes an asset locale reservation.
- [static var reservedLocales: [Locale]](assetinventory/reservedlocales.md)
  The app’s current asset locale reservations.
- [static var maximumReservedLocales: Int](assetinventory/maximumreservedlocales.md)
  The number of locale reservations permitted to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/reserve(locale:))*