# Communicates with Drivers

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an iPadOS app can communicate with drivers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

#### Discussion

When `true`, this entitlement allows your app to open user clients to one or more drivers.

On macOS, use the [`com.apple.developer.driverkit.userclient-access`](entitlements/com.apple.developer.driverkit.userclient-access.md) entitlement instead.

## See Also

- [com.apple.developer.driverkit.userclient-access](entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [com.apple.developer.driverkit.allow-any-userclient-access](entitlements/com.apple.developer.driverkit.allow-any-userclient-access.md)
  A Boolean value that determines whether a macOS driver accepts user client connections from any application.
- [DriverKit Allow Third Party User Clients](entitlements/com.apple.developer.driverkit.allow-third-party-userclients.md)
  A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.communicates-with-drivers)*