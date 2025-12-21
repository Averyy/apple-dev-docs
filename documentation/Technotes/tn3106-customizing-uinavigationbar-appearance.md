# TN3106: Customizing the appearance of UINavigationBar

**Framework**: Technotes

Adopt UINavigationBarAppearance for a navigation bar background color that’s consistent on iOS 13 through 18.

#### Overview

[`UINavigationBar`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbar) in iOS 15 introduces changes to its appearance settings. It extends the usage of its [`scrollEdgeAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbar/3198027-scrolledgeappearance), which by default produces a transparent background, to all navigation bar styles.

The iOS 13 SDK introduced an appearance settings class [`UINavigationBarAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbarappearance). If you’re seeing a view controller with appearance issues like a black navigation bar or incorrect status bar content color when building with Xcode 13 and running on iOS 15, adopt `UINavigationBarAppearance`. For a view controller that scrolls its content, use it to apply both `standardAppearance` and `scrollEdgeAppearance` to the `UINavigationBar`.

> ❗ **Important**: Starting in iOS 26, reduce your use of custom backgrounds in navigation elements and controls. While the techniques in this document remain valid for iOS 18 and earlier, prefer to remove custom effects and let the system determine the navigation bar background appearance. Any custom backgrounds and appearances you use in the navigation bar might overlay or interfere with Liquid Glass or other effects that the system provides, such as the scroll edge effect. To learn how to update your app to adopt Liquid Glass, see the following resources: - [`Adopting Liquid Glass`](https://developer.apple.comhttps://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- WWDC25 session 356: [`Get to know the new design system`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/356/)
- WWDC25 session 284: [`Build a UIKit app with the new design`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/284/).

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

-  Added information about the new design in iOS 26.
-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3106-customizing-uinavigationbar-appearance)*