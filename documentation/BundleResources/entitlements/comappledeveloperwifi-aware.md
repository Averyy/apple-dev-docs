# com.apple.developer.wifi-aware

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement the system requires for an app to use the Wi-Fi Aware framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Discussion

This entitlement works with the [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware) framework, which enables devices to securely discover, pair, and communicate with nearby devices without an internet connection or access point.

To use Wi-Fi Aware, add this entitlement to your app by enabling the Wi-Fi Aware capability on your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

Add the `Subscribe` string, the `Publish` string, or both to this entitlement, depending on your app’s intended features. The system requires this array to have at least one of the strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.wifi-aware)*