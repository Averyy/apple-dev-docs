# com.apple.developer.driverkit.userclient-access

**Framework**: Bundle Resources  
**Kind**: typealias

An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.

**Availability**:
- macOS 10.15+

#### Discussion

Add this entitlement to your app that opens the [`IOUserClient`](https://developer.apple.com/documentation/DriverKit/IOUserClient). Set its value to an array of bundle IDs of driver extensions that you want to use with DriverKit. If you have only one bundle ID, you can use either a single string or a one-element array.

On iPadOS, use the [`Communicates with Drivers`](entitlements/com.apple.developer.driverkit.communicates-with-drivers.md) entitlement instead.

## See Also

- [com.apple.developer.driverkit.allow-any-userclient-access](entitlements/com.apple.developer.driverkit.allow-any-userclient-access.md)
  A Boolean value that determines whether a macOS driver accepts user client connections from any application.
- [Communicates with Drivers](entitlements/com.apple.developer.driverkit.communicates-with-drivers.md)
  A Boolean value that indicates whether an iPadOS app can communicate with drivers.
- [DriverKit Allow Third Party User Clients](entitlements/com.apple.developer.driverkit.allow-third-party-userclients.md)
  A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.userclient-access)*