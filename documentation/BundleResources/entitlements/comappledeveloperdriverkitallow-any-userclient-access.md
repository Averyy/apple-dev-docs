# com.apple.developer.driverkit.allow-any-userclient-access

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that determines whether a macOS driver accepts user client connections from any application.

**Availability**:
- macOS 10.15+

#### Discussion

Add this entitlement to your dext that contains an [`IOUserClient`](https://developer.apple.com/documentation/DriverKit/IOUserClient) implementation. This entitlement allows any application to connect to the dext without having to specify bundle IDs, as [`com.apple.developer.driverkit.userclient-access`](entitlements/com.apple.developer.driverkit.userclient-access.md) requires.

## See Also

- [com.apple.developer.driverkit.userclient-access](entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [Communicates with Drivers](entitlements/com.apple.developer.driverkit.communicates-with-drivers.md)
  A Boolean value that indicates whether an iPadOS app can communicate with drivers.
- [DriverKit Allow Third Party User Clients](entitlements/com.apple.developer.driverkit.allow-third-party-userclients.md)
  A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.allow-any-userclient-access)*