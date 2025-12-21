# HotSpot Helper

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that permits an app to participate in navigating Wi-Fi network hotspots.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+

#### Discussion

Add this entitlement to your app to use the [`Hotspot helper`](https://developer.apple.com/documentation/NetworkExtension/hotspot-helper) API. For more information, see [`TN3111: iOS Wi-Fi API overview`](https://developer.apple.com/documentation/Technotes/tn3111-ios-wifi-api-overview).

To request this entitlement for your app, [`fill out the request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/hotspot-helper/).

## See Also

- [Access Wi-Fi Information Entitlement](entitlements/com.apple.developer.networking.wifi-info.md)
  A Boolean value indicating whether your app can access information about the connected Wi-Fi network.
- [Wireless Accessory Configuration Entitlement](entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [Multipath Entitlement](entitlements/com.apple.developer.networking.multipath.md)
  A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.
- [Hotspot Configuration Entitlement](entitlements/com.apple.developer.networking.hotspotconfiguration.md)
  A Boolean value indicating whether your app can use the hotspot manager to configure Wi-Fi networks.
- [ISO18092 system codes for NFC Tag Reader Session](entitlements/com.apple.developer.nfc.readersession.felica.systemcodes.md)
  A list of FeliCa system codes that the app supports.
- [Near Field Communication Tag Reader Session Formats Entitlement](entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.
- [ISO7816 application identifiers for NFC Tag Reader Session](entitlements/com.apple.developer.nfc.readersession.iso7816.select-identifiers.md)
  A list of application identifiers that the app supports.
- [com.apple.developer.nfc.hce](entitlements/com.apple.developer.nfc.hce.md)
  A Boolean value indicating whether your app can use the card session API.
- [com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes](entitlements/com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes.md)
  An array of identifier strings the app handles with the card session API.
- [com.apple.developer.nfc.hce.default-contactless-app](entitlements/com.apple.developer.nfc.hce.default-contactless-app.md)
  A Boolean value indicating whether your app can be a default app for contactless NFC with the card session API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.hotspothelper)*