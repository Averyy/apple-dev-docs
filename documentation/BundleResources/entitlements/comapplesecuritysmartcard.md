# com.apple.security.smartcard

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean that indicates whether your app has access to smart card slots and smart cards.

**Availability**:
- macOS 10.10+

#### Discussion

Add this entitlement to your app with a value of `true` if you want to use the [`TKSmartCardSlotManager`](https://developer.apple.com/documentation/CryptoTokenKit/TKSmartCardSlotManager) class. For an app without the entitlement, the slot manager’s [`default`](https://developer.apple.com/documentation/CryptoTokenKit/TKSmartCardSlotManager/default) value is `nil`. The system also requires this entitlement for sandboxed applications that access smart cards using legacy `PCSC` framework APIs.

## See Also

- [Audio Input Entitlement](entitlements/com.apple.security.device.audio-input.md)
  A Boolean value that indicates whether the app may record audio using the built-in microphone and access audio input using Core Audio.
- [Camera entitlement](entitlements/com.apple.security.device.camera.md)
  A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.
- [com.apple.security.device.microphone](entitlements/com.apple.security.device.microphone.md)
  A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](entitlements/com.apple.security.device.usb.md)
  A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](entitlements/com.apple.security.print.md)
  A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](entitlements/com.apple.security.device.bluetooth.md)
  A Boolean value indicating whether your app may interact with Bluetooth devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.smartcard)*