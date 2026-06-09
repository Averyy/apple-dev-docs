# release(reservedLocale:)

**Framework**: Speech  
**Kind**: method

Removes an asset locale reservation.

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
static func release(reservedLocale: Locale) async -> Bool
```

#### Return Value

`false` if the locale was not reserved.

#### Discussion

Unsubscribes from any assets that depended on the locale.

## See Also

- [static func reserve(locale: Locale) async throws -> Bool](assetinventory/reserve(locale:).md)
  Add an asset locale to the app’s current reservations.
- [static var reservedLocales: [Locale]](assetinventory/reservedlocales.md)
  The app’s current asset locale reservations.
- [static var maximumReservedLocales: Int](assetinventory/maximumreservedlocales.md)
  The number of locale reservations permitted to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/release(reservedlocale:))*