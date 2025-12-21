# TN3105: Customizing the UIKit status bar style

**Framework**: Technotes

Configure the device’s status bar style to work well with your app’s user interface.

#### Overview

Status bar content elements must be readable or visible to the user. Your app’s status bar style or [`UIStatusBarStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uistatusbarstyle) should be set to a value that’s compatible with your app’s background color: [`lightContent`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uistatusbarstyle/lightcontent) or [`darkContent`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uistatusbarstyle/darkcontent).

You control the `UIStatusBarStyle` at the app level or view controller level. At the app level choose a single `UIStatusBarStyle` that works well with its overall background color scheme. At the view controller level choose a `UIStatusBarStyle` that is most compatible with its specific background color.

If you find that your status bar elements aren’t visible, the problem might be that its background color is the same color as its content color (black elements on black background or white elements on white background). Users may also have a difficult time recognizing the status bar content when the background color is dark gray and its `UIStatusBarStyle` set to `darkContent`.

If you have a dark colored background, set the `UIStatusBarStyle` to `lightContent`. If you have a light colored background, set the `UIStatusBarStyle` to `darkContent`.

#### Set a Style for the Entire App

For a single status bar style throughout your app, add [`UIViewControllerBasedStatusBarAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/uiviewcontrollerbasedstatusbarappearance) with a value of `false` to your `Info.plist`. Then add `UIStatusBarStyle` with the specific style. For example, to set a light content status bar, use the following:

```None
<key>UIStatusBarStyle</key>
<string>UIStatusBarStyleLightContent</string>

<key>UIViewControllerBasedStatusBarAppearance</key>
<false/>
```

#### Set a Style for Each View Controller

To allow individual view controllers to determine their status bar style, set `UIViewControllerBasedStatusBarAppearance` to `true`.

First, add the `UIViewControllerBasedStatusBarAppearance` property to the `Info.plist`:

```None
<key>UIViewControllerBasedStatusBarAppearance</key>
<true/>
```

Second, if your initial root view controller’s status bar style is light content, add the following to the `Info.plist`. This will make your initial view controller’s status bar style match up with the launch screen status bar style:

```None
<key>UIStatusBarStyle</key>
<string>UIStatusBarStyleLightContent</string>
```

Third, override each view controller’s [`preferredStatusBarStyle()`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uiviewcontroller/1621416-preferredstatusbarstyle) method. For example, to set the status bar’s content intended for use on dark backgrounds:

```swift

class ViewController: UIViewController {
	//..
    override var preferredStatusBarStyle: UIStatusBarStyle {
        return .lightContent
    }
    //..
}
```

If a particular view controller is embedded as a child or resides inside a [`UINavigationController`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationcontroller) stack, its parent or navigation controller determines the status bar style. If you want the containing view controller to give control of the status bar style to its children, override the [`childForStatusBarStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uiviewcontroller/1621433-childforstatusbarstyle) property. For example:

```swift
class MyNavigationController: UINavigationController {
    // Return the visible child view controller which determines the status bar style.
    override var childForStatusBarStyle: UIViewController? { return visibleViewController }
}
```

For every `UINavigationController` defined in your storyboard that wants to give status bar style control over to its children, be sure to set its Custom Class name to match the `UINavigationController` subclass name on the Identity inspector.

It is not necessary to override the `childForStatusBarStyle` property when using [`UITabBarController`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uitabbarcontroller). `UITabBarController` automatically forwards status bar style requests to its children.

When using this approach, any child view controller determines the status bar style that will match up with its color scheme or customization it uses with [`UINavigationBarAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbarappearance/). If you return `nil` or do not override this method, the status bar style for `self` is used. If the return value from this method changes, call the `setNeedsStatusBarAppearanceUpdate()` method.

#### Revision History

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3105-customizing-uistatusbar-syle)*