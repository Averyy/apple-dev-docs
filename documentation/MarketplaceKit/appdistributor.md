# AppDistributor

**Framework**: MarketplaceKit  
**Kind**: enum

Options that describe the marketplace from which the app installs.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
enum AppDistributor
```

## Mentions

- [Distributing your app on an alternative app marketplace](distributing-your-app-on-an-alternative-marketplace.md)

#### Overview

Apps on alternative app marketplaces need to use APIs that vary from apps on the App Store. Specifically, use:

- [`AdAttributionKit`](https://developer.apple.com/documentation/AdAttributionKit) for ads.
- An e-commerce solution other than the App Store’s [`In-App Purchase`](https://developer.apple.com/documentation/StoreKit/in-app-purchase) system.
- A social gaming network other than [`Game Center`](https://developer.apple.com/documentation/AppStoreConnectAPI/game-center) unless your app is also on the App Store.
- [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets) to download large files in the background rather than [`On Demand Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/).

Only use [`StoreKit`](https://developer.apple.com/documentation/StoreKit) on the App Store.

To observe API differences, check the value of the app distributor’s static ([`current`](appdistributor/current.md)) property to determine the installation source:

| App distributor case | Installation source |
| --- | --- |
| [`AppDistributor.appStore`](appdistributor/appstore.md) | The App Store |
| [`AppDistributor.testFlight`](appdistributor/testflight.md) | TestFlight |
| [`AppDistributor.marketplace(_:)`](appdistributor/marketplace(_:).md) | Alternative app marketplace; the argument `String` identifies the marketplace bundle ID |
| [`AppDistributor.web`](appdistributor/web.md) | The developer’s website |
| [`AppDistributor.other`](appdistributor/other.md) | Enterprise or education developer programs |

For more information, see [`Distributing your app on an alternative app marketplace`](distributing-your-app-on-an-alternative-marketplace.md).

## Topics

### Enumeration Cases
- [AppDistributor.appStore](appdistributor/appstore.md)
- [AppDistributor.marketplace(_:)](appdistributor/marketplace(_:).md)
- [AppDistributor.other](appdistributor/other.md)
- [AppDistributor.testFlight](appdistributor/testflight.md)
- [AppDistributor.web](appdistributor/web.md)
### Type Properties
- [static var current: AppDistributor](appdistributor/current.md)
  The source from which the app installs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/appdistributor)*