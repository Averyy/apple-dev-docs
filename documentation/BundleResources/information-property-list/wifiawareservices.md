# WiFiAwareServices

**Framework**: Bundle Resources  
**Kind**: dictionary

Dictionaries of Wi-Fi Aware services that the app can publish or subscribe to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Overview

This key works with the [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware) framework, to define the services your app publishes, or to specify the services your app subscribes to, or both.

The system requires your app to have the [`com.apple.developer.wifi-aware`](entitlements/com.apple.developer.wifi-aware.md) entitlement, configured according to services you specify in this key to interact with the specified services at runtime.

For information on defining the services, see [`Adopting Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware/Adopting-Wi-Fi-Aware).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wifiawareservices)*