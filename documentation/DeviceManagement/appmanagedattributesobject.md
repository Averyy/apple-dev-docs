# AppManagedAttributesObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of values associated with an app.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- visionOS 2.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AppManagedAttributesObject
```

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)

## Properties

- `AssociatedDomains` ([string]): An array of domain names to associate with the app.
- `AssociatedDomainsEnableDirectDownloads` (boolean): If `true`, the system enables direct downloads for the `AssociatedDomains`.
- `CellularSliceUUID` (string): The cellular slice identifier, which can be the data network name (DNN) or app category. For DNN, encode the value as “DNN:name”, where “name” is the carrier-provided DNN name. For app category, encode the value as “AppCategory:category”, where “category” is a carrier-provided string such as “Enterprise1”.
- `ContentFilterUUID` (string): The UUID of the content filter to associate with the app.
- `DNSProxyUUID` (string): The UUID of the DNS proxy to associate with the app.
- `Hideable` (boolean): If `false`, the system prevents the user from hiding the app. It doesn’t affect the user’s ability to leave it in the App Library, while removing it from the Home Screen.
- `Lockable` (boolean): If `false`, the system prevents the user from locking the app. This also prevents the user from hiding the app.
- `RelayUUID` (string): The UUID of the relay to associate with the app.
- `TapToPayScreenLock` (boolean): If `true`, the device automatically locks after every transaction that requires a customer’s card PIN. If `false`, the user can choose the behavior.
- `VPNUUID` (string): The UUID of the VPN to associate with the app.

## See Also

- [object AppManagedAppConfigDictionaryObject](appmanagedappconfigdictionaryobject.md)
  A dictionary of app config data and credentials.
- [object AppManagedExtensionConfigsObject](appmanagedextensionconfigsobject.md)
  A dictionary of values associated with an extension config.
- [object AppManagedInstallBehaviorObject](appmanagedinstallbehaviorobject.md)
  A dictionary that describes how and when to install an app.
- [object AppManagedUpdateBehaviorObject](appmanagedupdatebehaviorobject.md)
  Specifies the update behavior of the apps installed from the App Store. Apps in packages are not automatically updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appmanagedattributesobject)*