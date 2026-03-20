# eligibilityRegion

**Framework**: MarketplaceKit  
**Kind**: property

A country code for the device’s current region.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
static var eligibilityRegion: String? { get async }
```

## Mentions

- [Distributing your app on an alternative app marketplace](distributing-your-app-on-an-alternative-marketplace.md)
- [Participating in alternative distribution for specific regions](participating-in-alternative-distribution-for-specific-regions.md)

#### Discussion

This property returns the device’s current country code based on its region setting, for example, `ie` for Ireland, and `jp` for Japan.

An app that installs from an alternative app marketplace can use the country code to determine whether the app meets criteria for transaction reporting. For more information, see [`Reporting transactions for the Core Technology Commission`](reporting-transactions-for-core-technology-commission.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/appdistributor/eligibilityregion)*