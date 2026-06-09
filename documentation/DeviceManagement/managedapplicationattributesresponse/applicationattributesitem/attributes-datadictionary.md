# ManagedApplicationAttributesResponse.ApplicationAttributesItem.Attributes

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains a managed app’s attributes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagedApplicationAttributesResponse.ApplicationAttributesItem.Attributes
```

## Properties

- `AssociatedDomains` ([string]): This app’s associated domains. Available: iOS 13+ | iPadOS 13+ | visionOS 1.1+ | watchOS 10+
- `AssociatedDomainsEnableDirectDownloads` (boolean): If `true`, perform claimed site association verification directly at the domain instead of on Apple’s servers. Only set this to `true` for domains that can’t access the internet. Available: iOS 14+ | iPadOS 14+ | visionOS 1.1+ | watchOS 10+
- `CellularSliceUUID` (string): The data network name (DNN) or app category. For DNN, the value is `DNN:name`, where `name` is the carrier-provided DNN name. For app category, the value is `AppCategory:category`, where `category` is a carrier-provided string like “Enterprise1”. Available: iOS 17+ | iPadOS 17+
- `ContentFilterUUID` (string): The content Filter UUID assigned to this app. Available: iOS 16+ | iPadOS 16+ | visionOS 1.1+
- `DNSProxyUUID` (string): The DNS Proxy UUID assigned to this app. Available: iOS 16+ | iPadOS 16+ | visionOS 1.1+
- `Hideable` (boolean): If `false`, the system prevents the user from hiding the app. It doesn’t affect the user’s ability to leave it in the App Library, while removing it from the Home Screen. Available: iOS 18.1+ | iPadOS 18.1+
- `Lockable` (boolean): If `false`, the system prevents the user from locking the app. This also prevents the user from hiding the app. Available: iOS 18.1+ | iPadOS 18.1+
- `RelayUUID` (string): The relay UUID for this app. Available: iOS 17+ | iPadOS 17+ | visionOS 1.1+
- `Removable` (boolean): If `false`, this app isn’t removable while it’s a managed app. Available: iOS 14+ | iPadOS 14+ | tvOS 14+ | visionOS 1.1+ | watchOS 10+
- `TapToPayScreenLock` (boolean): If `true`, Tap to Pay on iPhone requires users to use Face ID or a passcode to unlock their device after every transaction that requires a customer’s card PIN. If `false`, the user can configure this setting on their device. Available: iOS 16.4+ | iPadOS 16.4+
- `VPNUUID` (string): A per-app VPN unique identifier for this app. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+ | watchOS 10+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationattributesresponse/applicationattributesitem/attributes-data.dictionary)*