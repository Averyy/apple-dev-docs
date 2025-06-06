# fetchCurrent(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Fetches information about the current Wi-Fi network.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func fetchCurrent() async -> NEHotspotNetwork?
```

#### Discussion

This method produces a non-`nil` [`NEHotspotNetwork`](nehotspotnetwork.md) object only when the requesting app meets at least one of the following criteria:

- The app is using the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) API and has user’s authorization to access precise location.
- The app used the [`NEHotspotConfiguration`](nehotspotconfiguration.md) API to configure the current Wi-Fi network.
- The app has active VPN configurations installed.
- The app has an active [`NEDNSSettingsManager`](nednssettingsmanager.md) configuration installed.

This method also requires the app to have the [`Access Wi-Fi Information Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.wifi-info), and produces `nil` if the app lacks this entitlement.

## Parameters

- `completionHandler`: A Swift closure or an ObjectiveC block that receives an   instance that contains the current SSID, BSSID, and security type.   This call doesn’t populate other fields in the object.   The block executes on the main thread and only after the call obtains the current Wi-Fi parameters from the system.   If any of the criteria discussed below aren’t fulfilled, the   parameter received by completion handler is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotnetwork/fetchcurrent(completionhandler:))*