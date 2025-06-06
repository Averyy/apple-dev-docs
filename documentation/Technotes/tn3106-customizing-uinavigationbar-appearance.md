# TN3106: Customizing the appearance of UINavigationBar

**Framework**: Technotes

Adopt UINavigationBarAppearance for a navigation bar background color that’s consistent on iOS 13 and later.

#### Overview

[`UINavigationBar`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbar) in iOS 15 introduces changes to its appearance settings. It extends the usage of its [`scrollEdgeAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbar/3198027-scrolledgeappearance), which by default produces a transparent background, to all navigation bar styles.

The iOS 13 SDK introduced an appearance settings class [`UINavigationBarAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbarappearance). If you’re seeing a view controller with appearance issues like a black navigation bar or incorrect status bar content color when building with Xcode 13 and running on iOS 15, adopt `UINavigationBarAppearance`. For a view controller that scrolls its content, use it to apply both `standardAppearance` and `scrollEdgeAppearance` to the `UINavigationBar`.

#### Configure the Uinavigationbarappearance

Consider an app that uses `UITableViewController`, and has the following code in `application(_ :didFinishLaunchingWithOptions:)`:

```swift
UINavigationBar.appearance().isTranslucent = false
UINavigationBar.appearance().barTintColor = .systemRed
```

In iOS 14.x or later, the navigation bar color turns transparent (showing the black background underneath), yet iOS 13 draws the navigation bar in `.systemRed`.

To standardize the navigation bar’s appearance between these versions of iOS, use the `UINavigationBarAppearance` API. Use the following example to apply an opaque navigation bar colored `.systemRed` with white title text. Setting the text color here is only an example and of course is optional.

```swift
@available(iOS 13.0, *)
func customNavBarAppearance() -> UINavigationBarAppearance {
    let customNavBarAppearance = UINavigationBarAppearance()
    
    // Apply a red background.
    customNavBarAppearance.configureWithOpaqueBackground()
    customNavBarAppearance.backgroundColor = .systemRed
    
    // Apply white colored normal and large titles.
    customNavBarAppearance.titleTextAttributes = [.foregroundColor: UIColor.white]
    customNavBarAppearance.largeTitleTextAttributes = [.foregroundColor: UIColor.white]

    // Apply white color to all the nav bar buttons.
    let barButtonItemAppearance = UIBarButtonItemAppearance(style: .plain)
    barButtonItemAppearance.normal.titleTextAttributes = [.foregroundColor: UIColor.white]
    barButtonItemAppearance.disabled.titleTextAttributes = [.foregroundColor: UIColor.lightText]
    barButtonItemAppearance.highlighted.titleTextAttributes = [.foregroundColor: UIColor.label]
    barButtonItemAppearance.focused.titleTextAttributes = [.foregroundColor: UIColor.white]
    customNavBarAppearance.buttonAppearance = barButtonItemAppearance
    customNavBarAppearance.backButtonAppearance = barButtonItemAppearance
    customNavBarAppearance.doneButtonAppearance = barButtonItemAppearance
    
    return customNavBarAppearance
}
```

#### Configure the Entire App

To apply this appearance to the navigation bar throughout the entire app:

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    let newNavBarAppearance = customNavBarAppearance()
        
    let appearance = UINavigationBar.appearance()
    appearance.scrollEdgeAppearance = newNavBarAppearance
    appearance.compactAppearance = newNavBarAppearance
    appearance.standardAppearance = newNavBarAppearance
    if #available(iOS 15.0, *) {
        appearance.compactScrollEdgeAppearance = newNavBarAppearance
    }

    return true
}
```

#### Configure a View Controller

To apply this appearance to the navigation bar of an individual view controller:

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    let newNavBarAppearance = customNavBarAppearance()
    navigationController!.navigationBar.scrollEdgeAppearance = newNavBarAppearance
    navigationController!.navigationBar.compactAppearance = newNavBarAppearance
    navigationController!.navigationBar.standardAppearance = newNavBarAppearance
    if #available(iOS 15.0, *) {
        navigationController!.navigationBar.compactScrollEdgeAppearance = newNavBarAppearance
    }
}
```

If you’re using storyboards, instead configure both the appearance of the navigation bar and the elements within that bar.

To change the appearance of the navigation bar:

Choose “standard” and “scroll edge appearances” for the navigation bar, by setting the appearance proxy of `UINavigationBar`: “Standard”, and “ScrollEdge” appearances.

1. Open the project’s storyboard file.
2. Select the `UINavigationBar` from your `UINavigationController` scene.
3. In the Attributes Inspector pane turn on these Appearances: “Standard”, “Compact”, “Scroll Edge”, and “Compact Scroll Edge”.
4. For all four appearances, set the “Background” to “System Red Color”, for example.

Change the color of the title and button elements:

1. Change the bar button items color: set the View’s “Tint” color to “White Color”.
2. Change the Standard Text Attributes “Title” from “Inherited” to “Custom”.
3. Change the Standard Title Attributes “Title Color” from “Default” to “White Color”. Repeat steps 2 and 3 for: Scroll Edge and Compact Scroll Edge appearances.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3106-customizing-uinavigationbar-appearance)*