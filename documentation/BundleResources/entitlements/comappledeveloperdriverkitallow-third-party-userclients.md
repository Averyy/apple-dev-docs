# DriverKit Allow Third Party User Clients

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

#### Discussion

By default, an iPadOS driver accepts user-client connections from apps signed with the same team ID and the [`Communicates with Drivers`](entitlements/com.apple.developer.driverkit.communicates-with-drivers.md) entitlement. Set this entitlement to `true` on a driver to allow connections apps with other team IDs. The connecting apps must still have the [`Communicates with Drivers`](entitlements/com.apple.developer.driverkit.communicates-with-drivers.md) entitlement.

## See Also

- [com.apple.developer.driverkit.userclient-access](entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [com.apple.developer.driverkit.allow-any-userclient-access](entitlements/com.apple.developer.driverkit.allow-any-userclient-access.md)
  A Boolean value that determines whether a macOS driver accepts user client connections from any application.
- [Communicates with Drivers](entitlements/com.apple.developer.driverkit.communicates-with-drivers.md)
  A Boolean value that indicates whether an iPadOS app can communicate with drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.allow-third-party-userclients)*