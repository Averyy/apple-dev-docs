# SFSafariCorrespondingMacOSAppBundleIdentifier

**Framework**: Bundle Resources  
**Kind**: typealias

A string bundle ID that identifies the corresponding macOS app that contains a content blocker or Safari web extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

#### Discussion

To enable extension syncing for your iOS app that contains a content blocker or Safari web extension, specify the bundle ID of the corresponding macOS app that contains the same content blocker or Safari web extension.

Only add this to your `Info.plist` if the bundle ID for your iOS app is different from the bundle ID for your macOS app.

For more information, see [`Syncing Safari web extensions across devices and platforms`](https://developer.apple.com/documentation/SafariServices/syncing-safari-web-extensions-across-devices-and-platforms).

## See Also

- [SFSafariCorrespondingIOSAppBundleIdentifier](information-property-list/sfsafaricorrespondingiosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding iOS app that contains a content blocker or Safari web extension.
- [SFSafariCorrespondingIOSExtensionBundleIdentifier](information-property-list/sfsafaricorrespondingiosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on iOS.
- [SFSafariCorrespondingMacOSExtensionBundleIdentifier](information-property-list/sfsafaricorrespondingmacosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/sfsafaricorrespondingmacosappbundleidentifier)*