# Matter Allow Setup Payload

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that allows an app to provide an optional Matter Setup payload while setting up a Matter device in an ecosystem.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Discussion

You may use this entitlement in the following ways:

- For adding a device that doesn’t have a Matter QR code to your ecosystem or Apple Home.
- For adding an already-paired Matter device from your ecosystem to Apple Home.
- For creating apps that have a built-in QR code scanner and have the ability to scan non-Matter QR codes.

If the caller provides the setup payload, the framework doesn’t show the user interface for QR code selection.

## See Also

- [HomeKit Entitlement](entitlements/com.apple.developer.homekit.md)
  A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.matter.allow-setup-payload)*