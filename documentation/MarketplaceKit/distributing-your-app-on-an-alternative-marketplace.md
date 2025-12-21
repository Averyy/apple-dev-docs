# Distributing your app on an alternative app marketplace

**Framework**: MarketplaceKit

Design your app for alternative distribution from an alternative app marketplace.

#### Overview

To distribute your app from an alternative app marketplace, review and sign the necessary agreements. For your app to reside on an alternative app marketplace, it needs to run on one or more of the platforms that the target region supports. For information on the region-based agreements and platorms, see [`Participating in alternative distribution for specific regions`](participating-in-alternative-distribution-for-specific-regions.md).

App Store Connect ignores apps for platforms that the region doesn’t support. For example, when App Store Connect sends an alternative distribution package for your app to an alternative marketplace, it excludes any watchOS extensions or watch apps.

Apps on an alternative marketplace aren’t required to use MarketplaceKit, but you need to build your app with Xcode 14.1 or later and set the deployment target to greater than or equal to the earliest version of the OS that Xcode 14.1 supports. If your app does call MarketplaceKit methods, build your app with Xcode 15.3 or later.

#### Add the Required Target Property

If your app offers the purchase of digital goods or services, add the [`MKSellsDigitalGoods`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information-property-list/mksellsdigitalgoods) property to your app’s target configuration in Xcode with a value of `YES`. Also, report each offered purchase to Apple using the [`TransactionReporting`](transactionreporting.md) API. For more information, see [`Reporting transactions for the Core Technology Commission`](reporting-transactions-for-core-technology-commission.md).

If your app doesn’t sell digital goods or services, you still need to add the [`MKSellsDigitalGoods`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information-property-list/mksellsdigitalgoods) property to your app’s target configuration with a value of `NO`.

#### Customize Your App Depending on the Installation Source

If your app installs from more than one source, you can implement conditional code to do something different, such as displaying a different graphic, depending on the source from which a person installs your app. Use MarketplaceKit’s app distributor’s static [`current`](appdistributor/current.md) property to determine the installation source:

| App distributor | Installation source |
| --- | --- |
| [`AppDistributor.appStore`](appdistributor/appstore.md) | The App Store |
| [`AppDistributor.testFlight`](appdistributor/testflight.md) | TestFlight |
| [`AppDistributor.marketplace(_:)`](appdistributor/marketplace(_:).md) | Alternative app marketplace; the argument `String` identifies the marketplace bundle ID |
| [`AppDistributor.web`](appdistributor/web.md) | The developer’s website |
| [`AppDistributor.other`](appdistributor/other.md) | Enterprise or education developer programs |

In apps that people install from alternative marketplaces, use APIs that vary from apps on the App Store. Specifically, use:

- [`AdAttributionKit`](https://developer.apple.com/documentation/AdAttributionKit) for ads
- A custom e-commerce solution; API that rely on Apple’s App Store, such as [`In-App Purchase`](https://developer.apple.com/documentation/StoreKit/in-app-purchase) and [`On Demand Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/), don’t support alternative app marketplaces.
- [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets) to download large files in the background
- A social gaming network other than [`Game Center`](https://developer.apple.com/documentation/AppStoreConnectAPI/game-center) unless your app is also on the App Store

API availability varies depending on the source, so your app needs to check the current source at each launch — not just at the first launch — and adjust the APIs it uses accordingly.

#### Enable Your App to Run on Other Platforms

Apps can run on platforms that MarketplaceKit doesn’t support, including macOS using Mac Catalyst or as-is on Apple silicon, and visionOS. To check the platform, use `#if canImport(MarketplaceKit)`, which returns `false` for Mac apps built with Mac Catalyst and visionOS. Avoid importing MarketplaceKit on unsupported platforms, as follows:

```swift
#if canImport(MarketplaceKit)
import MarketplaceKit
#endif
```

If your app uses [`AppDistributor`](appdistributor.md), check the platform first and avoid accessing MarketplaceKit on unsupported platforms. The following example uses `#if canImport(MarketplaceKit)` again to conditionalize access to [`AppDistributor`](appdistributor.md):

```swift
func getDistributorName() async -> String {
#if canImport(MarketplaceKit)
    do {
        let currentDistributor = try await AppDistributor.current
        switch currentDistributor {
        case .appStore:
            return "App Store"
        case .testFlight:
            return "TestFlight"
        case .marketplace(let bundleId):
            return "Alternative marketplace (\(bundleId))"
        case .web:
            return "Website"
        case .other:
            return "Other"
        @unknown default:
            return "Unknown"
        }
    } catch { return "Error" }
#else
    return "Unavailable"
#endif
}
```

To check for as-is apps that run on Apple silicon, use `ProcessInfo.processInfo.isiOSAppOnMac`:

```swift
if ProcessInfo.processInfo.isiOSAppOnMac {
    distributorName = "Unavailable"
} else {
    Task { currentDistributorName = await getCurrentDistributor() }
}
```

#### Establish a Marketplace Relationship and Enable Notifications

To distribute your app on a particular alternative app marketplace, contact the marketplace directly and it provides you with a unique ID that you upload to App Store Connect. Apple verifies the ID with the marketplace’s public key to confirm your agreement, or relationship. For more information, see [`Manage distribution on an alternative app marketplace`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/manage-distribution-on-an-alternative-app-marketplace).

When you’re ready to submit your app for review, choose the App Store review type if you also intend to ship your app from the App Store in addition to an alternative app marketplace. To ship your app just from an alternative app marketplace, choose the Notarization review type (see [`Submit for Notarization`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/submit-for-notarization)).

When your app completes App Review or Notarization, your app becomes available for the marketplace to distribute. For distribution on an alternative app marketplace, App Store Connect provides your app in the form of an alternative distribution package after you’ve set up your marketplace relationship. The package contains instructions that the alternative app marketplace follows to assemble an installable version of your app. You can download the alternative distribution package and provide it to the marketplace manually or enable notifications in App Store Connect, which sends the package to the marketplace automatically. When notifications are on, App Store Connect keeps the marketplace up-to-date on the alternative distribution packages for all your latest app versions.

#### Test Your App During Development

Your app can install from an alternative marketplace app only after passing [`Notarization`](https://developer.apple.comhttps://developer.apple.com/support/dma-and-apps-in-the-eu/#notarization-for-ios-apps). To test your app beforehand, set the installation source for development builds. Setting the installation source enables you to simulate an installation from a marketplace in production.

Set your target’s Alternative Distribution - Marketplaces build setting to a list of marketplace bundle IDs for the alternative marketplaces from which your app can install.

![A screenshot of Xcode with the project, AltDistTesting, selected in the project navigation sidebar, and the build settings tab open. Under targets, AltDistTesting is selected, under Deployment the setting Alternative Distribution - Marketplaces is set to com.megabytemart.megabytemart.](https://docs-assets.developer.apple.com/published/715e17e0c190e7540475997a1000d417/distributing-your-app-on-an-alternative-marketplace-2%402x.png)

> **Note**: The build setting by name is `MARKETPLACES`. Open your Xcode project in Xcode 15.3 or later and add the build setting manually if one by that title isn’t present.

This build setting overrides the [`current`](appdistributor/current.md) property for development builds, which enables you to test any custom code branching your app might do, such as displaying a different image or offering different menu items.

![A screenshot of Xcode Scheme settings window with Run selected in the sidebar and the options tab open. The Distribution pop-up menu shows the com.megabytemart.megabytemart option selected.](https://docs-assets.developer.apple.com/published/70e79d5d902f0366fe7fd4361d78a65f/distributing-your-app-on-an-alternative-marketplace-3%402x.png)

In your scheme’s Run task Options tab, Distribution selection menu, choose that marketplace’s bundle ID to simulate installation from that marketplace for runs on device through Xcode.

Similarly, to override the [`current`](appdistributor/current.md) distributor in a test plan, choose a marketplace bundle ID in the Distribution selection menu of your test plan’s configuration.

![A screenshot of Xcode with TestPlan selected in the project navigation sidebar and the Configurations tab open. The Distribution pop-up menu has com.megabytemart.megabytemart selected.](https://docs-assets.developer.apple.com/published/209510fc162d3ec1d862ab011027f876/distributing-your-app-on-an-alternative-marketplace-4%402x.png)

## See Also

- [Creating an alternative app marketplace](creating-an-alternative-app-marketplace.md)
  Enable the distribution of other third-party apps from within your marketplace app.
- [Distributing your app from your website](distributing-your-app-from-your-website.md)
  Configure your app and website to enable people to install your app on their devices from your website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-on-an-alternative-marketplace)*