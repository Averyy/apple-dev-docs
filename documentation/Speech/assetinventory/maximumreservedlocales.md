# maximumReservedLocales

**Framework**: Speech  
**Kind**: property  
**Role**: Type Property

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

This value is the largest allowed count of [`reservedLocales`](./reservedlocales.md). The value may vary between devices according to storage space.

## See Also

### Managing allocations
- [static func reserve(locale: Locale) async throws -> Bool](./reserve%28locale%29.md)
  Add an asset locale to the app’s current reservations.
- [static func release(reservedLocale: Locale) async -> Bool](./release%28reservedlocale%29.md)
  Removes an asset locale reservation.
- [static var reservedLocales: [Locale]](./reservedlocales.md)
  The app’s current asset locale reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/maximumreservedlocales)*