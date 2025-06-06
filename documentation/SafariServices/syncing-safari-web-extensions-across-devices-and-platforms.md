# Syncing Safari web extensions across devices and platforms

**Framework**: Safari Services

Let users install your extension on one device and then use and manage the extension on all their other iOS and macOS devices.

#### Overview

In Safari 15 or earlier, when a user wants to install your Safari web extension on multiple devices, they have to install your extension from the App Store and enable the extension in Safari Preferences on each device.

In Safari 16 and later, when a user installs your Safari web extension on one device, they can install your extension on another device directly from Safari Extensions Preferences, without visiting the App Store. When a user enables or disables your extension on one device, the system syncs that change to the user’s other devices that have the web extension installed. The user can disable syncing for a specific device. Syncing works for all Safari web extensions and content blockers.

In the following circumstances, extensions automatically sync with no configuration:

- Your extension only works in either macOS or iOS.
- Your extension uses the same bundle identifier in both macOS and iOS. This is the default for a new Safari web extension you create or convert in Xcode.

If your extension has different bundle identifiers in macOS and iOS, turn on syncing by configuring your Xcode project for both macOS and iOS.

> **Note**:  If you provide your extension in both iOS and macOS, consider selling them together as one product to improve the purchasing experience for your users. For more information, see [`Offering Universal Purchase`](https://developer.apple.comhttps://developer.apple.com/support/universal-purchase/).

 If you provide your extension in both iOS and macOS, consider selling them together as one product to improve the purchasing experience for your users. For more information, see [`Offering Universal Purchase`](https://developer.apple.comhttps://developer.apple.com/support/universal-purchase/).

##### Configure Your Macos App and Extension

In your Xcode project, configure your macOS app to refer to your iOS app to support extension syncing:

1. Select the top project item in the Project navigator pane.
2. Select the target for your macOS app.
3. Click the Info tab.
4. Add the [`SFSafariCorrespondingIOSAppBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingIOSAppBundleIdentifier) key to the Custom macOS Application Target Properties section.
5. Specify the bundle identifier of your corresponding iOS app as the value.

Next, configure your macOS extension for syncing:

1. Select the target for your macOS extension.
2. Click the Info tab.
3. Add the [`SFSafariCorrespondingIOSExtensionBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingIOSExtensionBundleIdentifier) key to the Custom macOS Bundle Target Properties section.
4. Specify the bundle identifier of your corresponding iOS extension as the value.

> **Note**:  The bundle identifiers for the iOS app and extension you specify must be from the same developer account as your macOS app and extension.

 The bundle identifiers for the iOS app and extension you specify must be from the same developer account as your macOS app and extension.

##### Configure Your Ios App and Extension

In your Xcode project, configure your iOS app to refer to your macOS app to support extension syncing:

1. Select the top project item in the Project navigator pane.
2. Select the target for your iOS app.
3. Click the Info tab.
4. Add the [`SFSafariCorrespondingMacOSAppBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingMacOSAppBundleIdentifier) key to the Custom iOS Target Properties section.
5. Specify the bundle identifier of your corresponding macOS app as the value.

Next, configure your iOS extension for syncing:

1. Select the target for your iOS extension.
2. Click the Info tab.
3. Add the [`SFSafariCorrespondingMacOSExtensionBundleIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SFSafariCorrespondingMacOSExtensionBundleIdentifier) key to the iOS Target Properties section.
4. Specify the bundle identifier of your corresponding macOS extension.

> **Note**:  The bundle identifiers for the macOS app and extension you specify must be from the same developer account as your iOS app and extension.

 The bundle identifiers for the macOS app and extension you specify must be from the same developer account as your iOS app and extension.

## See Also

- [Optimizing your web extension for Safari](optimizing-your-web-extension-for-safari.md)
  Support Dark Mode, reduce memory and power usage, and ensure feature compatibility to improve your web extension experience in Safari and web apps.
- [Adopting New Safari Web Extension APIs](adopting-new-safari-web-extension-apis.md)
  Improve your web extension in Safari with a non-persistent background page and new tab-override customization.
- [Assessing your Safari web extension’s browser compatibility](assessing-your-safari-web-extension-s-browser-compatibility.md)
  Review your Safari web extension implementation plan, manifest keys, and JavaScript API usage for compatibility with other browsers.
- [Troubleshooting your Safari web extension](troubleshooting-your-safari-web-extension.md)
  Use developer resources to investigate and resolve common problems with Safari web extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/syncing-safari-web-extensions-across-devices-and-platforms)*