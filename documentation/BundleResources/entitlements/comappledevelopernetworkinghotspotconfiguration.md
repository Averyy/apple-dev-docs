# Hotspot Configuration Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether your app can use the hotspot manager to configure Wi-Fi networks.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

#### Discussion

This key indicates whether your app may use the [`NEHotspotConfigurationManager`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotConfigurationManager) and [`NEHotspotConfiguration`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotConfiguration) classes to configure Wi-Fi networks.

To add this entitlement to your app, enable the Hotspot Configuration capability in Xcode.

## See Also

- [class NEHotspotHelper](../NetworkExtension/NEHotspotHelper.md)
  A class to register a hotspot helper.
- [Access Wi-Fi Information Entitlement](entitlements/com.apple.developer.networking.wifi-info.md)
  A Boolean value indicating whether your app can access information about the connected Wi-Fi network.
- [Wireless Accessory Configuration Entitlement](entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [Multipath Entitlement](entitlements/com.apple.developer.networking.multipath.md)
  A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.
- [HotSpot Helper](entitlements/com.apple.developer.networking.hotspothelper.md)
  An entitlement that permits an app to participate in navigating Wi-Fi network hotspots.
- [Near Field Communication Tag Reader Session Formats Entitlement](entitlements/com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.
- [com.apple.developer.nfc.hce](entitlements/com.apple.developer.nfc.hce.md)
  A Boolean value indicating whether your app can use the card session API.
- [com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes](entitlements/com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes.md)
  An array of identifier strings the app handles with the card session API.
- [com.apple.developer.nfc.hce.default-contactless-app](entitlements/com.apple.developer.nfc.hce.default-contactless-app.md)
  A Boolean value indicating whether your app can be a default app for contactless NFC with the card session API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.hotspotconfiguration)*