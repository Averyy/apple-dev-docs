# ManagedApplicationAttributesResponse.ApplicationAttributesItem.Attributes

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains a managed app’s attributes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagedApplicationAttributesResponse.ApplicationAttributesItem.Attributes
```

## Properties

- `AssociatedDomains` ([string]): This app’s associated domains. This value is available in iOS 13 and later.
- `AssociatedDomainsEnableDirectDownloads` (boolean): If `true`, perform claimed site association verification directly at the domain instead of on Apple’s servers. Only set this to `true` for domains that can’t access the internet. This value is available in iOS 14 and later.
- `CellularSliceUUID` (string): The data network name (DNN) or app category. For DNN, the value is `DNN:name`, where `name` is the carrier-provided DNN name. For app category, the value is `AppCategory:category`, where `category` is a carrier-provided string like “Enterprise1”. Available in iOS 17 and later.
- `ContentFilterUUID` (string): The content Filter UUID assigned to this app. Available in iOS 16 and later.
- `DNSProxyUUID` (string): The DNS Proxy UUID assigned to this app. Available in iOS 16 and later.
- `Hideable` (boolean): If `false`, the system prevents the user from hiding the app. It doesn’t affect the user’s ability to leave it in the App Library, while removing it from the Home Screen.
- `Lockable` (boolean): If `false`, the system prevents the user from locking the app. This also prevents the user from hiding the app.
- `RelayUUID` (string): The relay UUID for this app.
- `Removable` (boolean): If `false`, this app isn’t removable while it’s a managed app. This value is available in iOS 14 and later.
- `TapToPayScreenLock` (boolean): If `true`, Tap to Pay on iPhone requires users to use Face ID or a passcode to unlock their device after every transaction that requires a customer’s card PIN. If `false`, the user can configure this setting on their device. Available in iOS 16.4 and later.
- `VPNUUID` (string): A per-app VPN unique identifier for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationattributesresponse/applicationattributesitem/attributes-data.dictionary)*