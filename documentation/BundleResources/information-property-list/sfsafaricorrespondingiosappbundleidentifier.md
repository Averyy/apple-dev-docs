# SFSafariCorrespondingIOSAppBundleIdentifier

**Framework**: Bundle Resources  
**Kind**: typealias

A string bundle ID that identifies the corresponding iOS app that contains a content blocker or Safari web extension.

**Availability**:
- macOS 13.0+

#### Discussion

To enable extension syncing for your macOS app that contains a content blocker or Safari web extension, specify the bundle ID of the corresponding iOS app that contains the same content blocker or Safari web extension.

Only add this to your `Info.plist` if the bundle ID for your macOS app is different from the bundle ID for your iOS app.

For more information, see [`Syncing Safari web extensions across devices and platforms`](https://developer.apple.com/documentation/SafariServices/syncing-safari-web-extensions-across-devices-and-platforms).

## See Also

- [SFSafariCorrespondingIOSExtensionBundleIdentifier](information-property-list/sfsafaricorrespondingiosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on iOS.
- [SFSafariCorrespondingMacOSAppBundleIdentifier](information-property-list/sfsafaricorrespondingmacosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding macOS app that contains a content blocker or Safari web extension.
- [SFSafariCorrespondingMacOSExtensionBundleIdentifier](information-property-list/sfsafaricorrespondingmacosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/sfsafaricorrespondingiosappbundleidentifier)*