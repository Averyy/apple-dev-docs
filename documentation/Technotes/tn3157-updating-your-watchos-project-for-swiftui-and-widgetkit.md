# TN3157: Updating your watchOS project for SwiftUI and WidgetKit

**Framework**: Technotes

Update your watchOS app project to adopt SwiftUI, WidgetKit, and other modern features.

#### Overview

Since the debut of Apple Watch, watchOS app development has the following important milestones:

- In 2015, watchOS 1 was released, together with WatchKit and ClockKit.
- In 2020, watchOS 7 was released. WatchKit storyboards were deprecated. New developments use SwiftUI.
- In 2022, Xcode 14 was released. It removes the support of creating a new WatchKit storyboard, and introduces single-target watchOS app.
- In 2023, watchOS 10 was released. ClockKit complications were deprecated, and the replacement is WidgetKit complications.

SwiftUI is cross-platform and provides many features unavailable in WatchKit, such as [`TimelineView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/timelineview) and [`TabView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/tabview). WidgetKit complications support Smart Stack in watchOS 10. Making a watchOS app single-target simplifies the project configuration. If you have an existing watchOS app, now is the time to get rid of the deprecated WatchKit storyboards and ClockKit complications, and adopt the modern features.

#### The Terminology

This technote uses the following terminology to refer a watchOS app with different characteristics:

- A  app relies on its companion iOS app to function.
- An  app works when the paired iPhone isn’t nearby, or when its companion iOS app isn’t installed. It may or may not have a companion iOS app.
- A  app has a watchOS app target and a WatchKit extension target for its core functionality.
- A  app has only a watchOS app target for its core functionality.
- A  app doesn’t have a companion iOS app.

> **Note**: Both single-target and dual-target apps can have other targets. For example, you can add targets to implement widgets or app intents for a single-target or dual-target app.

#### From Dependent to Independent

Apple Watch users expect that the apps to just work, even when they don’t have their iPhones with them. If you have a dependent watchOS app, consider making it independent. See [`Creating independent watchOS apps`](https://developer.apple.comhttps://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps#Convert-a-dependent-watchOS-app-to-an-independent-watchOS-app) for details.

#### From Dual Target to Single Target

If your watchOS app is dual-target, convert it to single-target. This simplifies the project configuration and eliminates any confusion about where to embed a resource or apply an entitlement. Single-target watchOS apps work on watchOS 7 and later. For more information, see [`Build a productivity app for Apple Watch`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10133/).

> **Note**: A single-target watchOS app requires watchOS 9.2 or later to inherit the HealthKit permissions granted to its companion iOS app. If your app uses HealthKit and needs to support earlier versions of watchOS, keep your dual-target app configuration.

To convert a dual-target app to a single target:

1. Create a complete back up for your project so you can roll back if something goes wrong.
2. In Xcode’s Project navigator, select the project, then choose Xcode > Editor > Validate Settings.
3. Select the “Project  - Upgrade  to a single-target watch app” checkbox if unselected, then choose Perform Changes to let Xcode do the conversion.
4. If you use storyboards, go through all the interface controllers, and change the class module to the watchOS app module. To do that, select an interface control,  and choose View > Inspectors > Identity; in the inspector, set the Class field in the Custom Class section.
5. Remove the files only relevant to the WatchKit extension, such as the extension’s `Info.plist`.
6. Clean up your project by re-organizing the groups and files in Xcode’s Project navigator.

The second step removes the WatchKit extension target and moves its associated source code and resources to the watchOS app target. At the code level, it replaces [`WKExtension`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkextension) and [`WKExtensionDelegate`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkextensiondelegate) with [`WKApplication`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkapplication) and [`WKApplicationDelegate`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkapplicationdelegate). It also changes the `Info.plist` of the watchOS app target as needed. For example, if your watchOS app has a complication, it moves the complication controller class, which is specified with [`CLKComplicationPrincipalClass`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/clkcomplicationprincipalclass), to the watchOS app target, and adds the `CLKComplicationPrincipalClass` and [`CLKComplicationSupportedFamilies`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/clkcomplicationsupportedfamilies) entries to the watchOS app’s `Info.plist`.

You now have a single-target watchOS app project. Verify that everything works well by running the project on an Apple Watch.

#### From Watchkit Storyboards to Swiftui

To adopt SwiftUI lifecycle in your watchOS app, start by adding a SwiftUI app ([`App`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/app)) struct:

```swift
import SwiftUI

@main
struct MyWatchApp: App {
    var body: some Scene {
        WindowGroup {
            Text("Hello, world!")
        }
    }
}
```

If you need to run the `WKApplicationDelegate` methods in the SwiftUI lifecycle, use [`WKApplicationDelegateAdaptor`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor) to connect the app delegate to the SwiftUI app. Otherwise, remove the delegate class.

```swift
import WatchKit
import SwiftUI

//@main
class MyWatchAppDelegate: NSObject, WKApplicationDelegate {...}

@main
struct MyWatchApp: App {
    @WKApplicationDelegateAdaptor var appDelegate: MyWatchAppDelegate
    var body: some Scene {...}
}
```

If you still use [`WKExtensionDelegate`](https://developer.apple.comhttps://developer.apple.com/documentation/watchkit/wkextensiondelegate) and need to run the extension delegate methods in the SwiftUI lifecycle, migrate `WKExtensionDelegate` to `WKApplicationDelegate`.

To migrate your WatchKit storyboard, rewrite the interface with SwiftUI. Alternatively, consider adopting SwiftUI incrementally by using [`WKHostingController`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/wkhostingcontroller) to host SwiftUI views in your WatchKit interface controllers.

#### From Clockkit to Widgetkit Complications

To migrate a ClockKit complication to WidgetKit:

1. Create a widget to replace the ClockKit complication. See [`Creating accessory widgets and watch complications`](https://developer.apple.comhttps://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications) for details.
2. Implement [`CLKComplicationWidgetMigrator`](https://developer.apple.comhttps://developer.apple.com/documentation/clockkit/clkcomplicationwidgetmigrator) in the complication controller class to migrate the ClockKit complication. See [`Migrating ClockKit complications to WidgetKit`](https://developer.apple.comhttps://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app#Migrate-complications-on-a-watch-face) for details.

> **Note**: When the ClockKit complication doesn’t have a descriptor, the system passes a descriptor with the default identifier ([`CLKDefaultComplicationIdentifier`](https://developer.apple.comhttps://developer.apple.com/documentation/clockkit/clkdefaultcomplicationidentifier)) to [`getWidgetConfiguration(from:completionHandler:)`](https://developer.apple.comhttps://developer.apple.com/documentation/clockkit/clkcomplicationwidgetmigrator/3972695-getwidgetconfiguration). Ignore the descriptor and return a [`CLKComplicationWidgetMigrationConfiguration`](https://developer.apple.comhttps://developer.apple.com/documentation/clockkit/clkcomplicationwidgetmigrationconfiguration) object with the appropriate widget kind.

#### From a Watch Only App to a Watchos App with a Companion Ios App

SwiftUI and WidgetKit are both cross-platform. If you have a watch-only app, you might want to enhance the watchOS app by adding an iOS companion app, and have the iOS app share SwiftUI views and widgets with the watchOS app.

> **Note**: After adding an iOS companion app and publishing it to the App Store, you can’t roll back to a watch-only app.

To add an iOS companion app to an existing watch-only app project:

1. Create a complete back up for your project so you can roll back if something goes wrong.
2. In Xcode, select your project in the Project navigator, then add a new iOS app target.
3. Select the iOS app target from the Targets list, click the Signing & Capabilities tab, then [`choose a team`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution/#Assign-the-project-to-a-team) from the Team pop-up menu and enter a [`bundle ID`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution/#Set-the-bundle-ID). Be sure that the iOS app’s bundle ID is the prefix of the watchOS app’s bundle ID. For example, if the watchOS app’s bundle ID is `com.YourCompany.ProductName.watchkitapp`, the iOS app’s bundle ID must be `com.YourCompany.ProductName`.
4. Select the General tab, then under Frameworks, Libraries, and Embedded Content, add the watchOS app as an embedded content of the iOS app.
5. Confirm that the [`WKCompanionAppBundleIdentifier`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/wkcompanionappbundleidentifier) key in the watchOS app’s `Info.plist` is set to the bundle ID of the iOS app.

You now have a project that has an independent watchOS app with a companion iOS app. By default, Xcode doesn’t install the iOS app when running the watchOS app. If you’d like to change the behavior, add the [`WKRunsIndependentlyOfCompanionApp`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/wkrunsindependentlyofcompanionapp) entry to the `Info.plist` of the watchOS app, then set its value to `NO`.

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3157-updating-your-watchos-project-for-swiftui-and-widgetkit)*