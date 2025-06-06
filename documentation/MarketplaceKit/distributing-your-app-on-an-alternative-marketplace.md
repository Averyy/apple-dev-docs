# Distributing your app on an alternative app marketplace

**Framework**: Marketplacekit

Design your app for alternative distribution from an alternative app marketplace.

#### Overview

To distribute your app from an alternative app marketplace, review and sign the [`Alternative EU Terms Addendum`](https://developer.apple.comhttps://developer.apple.com/contact/request/alternative-eu-terms-addendum/) to the [`Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/programs/apple-developer-program-license-agreement).

![Three screenshots of iPhone that show the stages of installing an app, Backyard Birds, from a fictional alternative app marketplace called Megabyte Mart. The left screenshot has the caption Alternative app marketplace and shows a representation of the Megabyte Mart app that show the app icon for Backyard Birds with an Install button in a list. The center screenshot has the caption Install sheet and shows a confirmation, the title of the sheet is Megabyte Mart Would Like to Install an App, followed by lines that represent descriptive text, followed by the Backyard Birds app info, which includes the developer name Tapland, Inc. as well as screenshots, below the app info is the Install App button, followed by a Cancel button. The right screenshot has the caption App from an alternative marketplace and shows a representation of the homescreen with Megabyte Mart and Backyard Birds installed.](https://docs-assets.developer.apple.com/published/04f5de82797e5c7eca1bf416f5a0f9c3/distributing-your-app-on-an-alternative-marketplace-1%402x.png)

Apps that reside on alternative marketplaces need to support iPhone or iPad, alternative app marketplaces don’t support other platforms. In addition, when App Store Connect sends your app to an alternative marketplace, it excludes any watchOS extensions or watch apps.

Apps on an alternative marketplace aren’t required to use MarketplaceKit. But you need to build your app with Xcode 14.1 or later and set the deployment target greater than or equal to the earliest version of iOS or iPadOS that Xcode 14.1 supports. If your app does call MarketplaceKit methods, build your app with Xcode 15.3 or later.

#### Customize Your App Depending on the Installation Source

If your app installs from more than one source, you can implement conditional code to do something different, such as displaying a different graphic, depending on the source from which a person installs your app. Use MarketplaceKit app distributor’s static [`current`](appdistributor/current.md) property to determine the installation source:

| App distributor | Installation source |
| --- | --- |
| [`AppDistributor.appStore`](appdistributor/appstore.md) | The App Store |
| [`AppDistributor.testFlight`](appdistributor/testflight.md) | TestFlight |
| [`AppDistributor.marketplace(_:)`](appdistributor/marketplace(_:).md) | Alternative app marketplace; the argument `String` identifies the marketplace bundle ID |
| [`AppDistributor.web`](appdistributor/web.md) | The developer’s website |
| [`AppDistributor.other`](appdistributor/other.md) | Enterprise or education developer programs |

In apps that people install from alternative marketplaces, use APIs that vary from apps on the App Store. Specifically, use:

- [`AdAttributionKit`](https://developer.apple.com/documentation/AdAttributionKit) for ads
- A custom e-commerce solution
- A social gaming network other than [`Game Center`](https://developer.apple.com/documentation/AppStoreConnectAPI/game-center) unless your app is also on the App Store
- [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets) to download large files in the background

Don’t use [`StoreKit`](https://developer.apple.com/documentation/StoreKit), the App Store’s [`In-App Purchase`](https://developer.apple.com/documentation/StoreKit/in-app-purchase) system, or [`On Demand Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/) in apps you distribute outside of the App Store.

#### Enable Your App to Run on Other Platforms

Apps can run on platforms that MarketplaceKit doesn’t support, including macOS using Mac Catalyst or  on Apple silicon, and visionOS. To check the platform, use `#if canImport(MarketplaceKit)`, which returns `false` for Mac apps built with Mac Catalyst and visionOS. Avoid importing MarketplaceKit on unsupported platforms, as follows:

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

To check for  apps that run on Apple silicon, use `ProcessInfo.processInfo.isiOSAppOnMac`:

```swift
if ProcessInfo.processInfo.isiOSAppOnMac {
    distributorName = "Unavailable"
} else {
    Task { currentDistributorName = await getCurrentDistributor() }
}
```

#### Establish a Marketplace Relationship and Enable Notifications

To distribute your app on a particular alternative app marketplace, contact the marketplace directly and it provides you with a unique ID that you upload to App Store Connect. Apple verifies the ID with the marketplace’s public key to confirm your agreement, or . For more information, see [`Manage distribution on an alternative app marketplace`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/manage-distribution-on-an-alternative-app-marketplace).

When you’re ready to submit your app for review, choose the Notarization review type; see [`Submit for Notarization`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/submit-for-notarization). app completes , your app becomes available for the marketplace to distribute. App Store Connect provides your Notarization-approved app in the form of an . The package contains instructions that the alternative app marketplace follows to assemble an installable version of your app. You can download the alternative distribution package and provide it to the marketplace manually or, enable notifications in App Store Connect, which sends the package to the marketplace automatically. When notifications are on, App Store Connect keeps the marketplace up-to-date on the alternative distribution packages for all your latest app versions.

#### Test Your App During Development

Your app can install from an alternative marketplace app only after passing [`Notarization`](https://developer.apple.comhttps://developer.apple.com/support/dma-and-apps-in-the-eu/#notarization-for-ios-apps). To test your app beforehand, set the installation source for development builds. Setting the installation source enables you to simulate an installation from a marketplace in production.

Set your target’s  build setting to a list of marketplace bundle IDs for the alternative marketplaces from which your app can install.

![A screenshot of Xcode with the project, AltDistTesting, selected in the project navigation sidebar, and the build settings tab open. Under targets, AltDistTesting is selected, under Deployment the setting Alternative Distribution - Marketplaces is set to com.megabytemart.megabytemart.](https://docs-assets.developer.apple.com/published/715e17e0c190e7540475997a1000d417/distributing-your-app-on-an-alternative-marketplace-2%402x.png)

> **Note**: The build setting by name is `MARKETPLACES`. Open your Xcode project in Xcode 15.3 or later and add the build setting manually if one by that title isn’t present.

This build setting overrides the [`current`](appdistributor/current.md) property for development builds, which enables you to test any custom code branching your app might do, such as displaying a different image or offering different menu items.

![A screenshot of Xcode Scheme settings window with Run selected in the sidebar and the options tab open. The Distribution pop-up menu shows the com.megabytemart.megabytemart option selected.](https://docs-assets.developer.apple.com/published/70e79d5d902f0366fe7fd4361d78a65f/distributing-your-app-on-an-alternative-marketplace-3%402x.png)

In your scheme’s Run task Options tab, Distribution selection menu, choose that marketplace’s bundle ID to simulate installation from that marketplace for runs on device through Xcode.

Similarly, to override the `current` distributor in a test plan, choose a marketplace bundle ID in the Distribution selection menu of your test plan’s configuration.

![A screenshot of Xcode with TestPlan selected in the project navigation sidebar and the Configurations tab open. The Distribution pop-up menu has com.megabytemart.megabytemart selected.](https://docs-assets.developer.apple.com/published/209510fc162d3ec1d862ab011027f876/distributing-your-app-on-an-alternative-marketplace-4%402x.png)

## See Also

- [Creating an alternative app marketplace](creating-an-alternative-app-marketplace.md)
  Enable the distribution of other third-party apps from within your marketplace app.
- [Distributing your app from your website](distributing-your-app-from-your-website.md)
  Configure your app and website to enable people to install your app on their devices from your website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MarketplaceKit/distributing-your-app-on-an-alternative-marketplace)*