# Multipath Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- visionOS 1.0+

#### Discussion

This key Indicates whether your app may use Multipath protocols, such as Multipath TCP, to smoothly hand over traffic from one interface to another.

To add this entitlement to your app, enable the Multipath capability in Xcode.

## See Also

- [Improving network reliability using Multipath TCP](../Foundation/improving-network-reliability-using-multipath-tcp.md)
  Use the available radios in iOS devices to improve your app’s network reliability and performance.
- [var multipathServiceType: URLSessionConfiguration.MultipathServiceType](../Foundation/URLSessionConfiguration/multipathServiceType-swift.property.md)
  A service type that specifies the Multipath TCP connection policy for transmitting data over Wi-Fi and cellular interfaces.
- [Access Wi-Fi Information Entitlement](entitlements/com.apple.developer.networking.wifi-info.md)
  A Boolean value indicating whether your app can access information about the connected Wi-Fi network.
- [Wireless Accessory Configuration Entitlement](entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [Hotspot Configuration Entitlement](entitlements/com.apple.developer.networking.hotspotconfiguration.md)
  A Boolean value indicating whether your app can use the hotspot manager to configure Wi-Fi networks.
- [HotSpot Helper](entitlements/com.apple.developer.networking.hotspothelper.md)
  An entitlement that permits an app to participate in navigating Wi-Fi network hotspots.
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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.multipath)*