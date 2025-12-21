# catalogRegion

**Framework**: MarketplaceKit  
**Kind**: property

A country code for the device’s current region.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
nonisolated
final var catalogRegion: String? { get async }
```

## Mentions

- [Participating in alternative distribution for specific regions](participating-in-alternative-distribution-for-specific-regions.md)

#### Discussion

This property returns the device’s current country code based on its region setting, for example, `ie` for Ireland, and `jp` for Japan.

Apps that reside on an alternative app marketplace can have varying availability based on region, so the marketplace can use the country code to decide which set of apps, or catalog, to offer a person for installation.

This property is `nil` if the app isn’t an alternative app marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/catalogregion)*