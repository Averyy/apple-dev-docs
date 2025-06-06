# getConfiguredSSIDs(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Submits a completion handler the configuration manager calls to send your app the names of the SSIDs or Wi-Fi hotspot domains in the configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func configuredSSIDs() async -> [String]
```

#### Discussion

The hotspot configuration manager sends your app a list of network SSIDs or Hotspot 2.0 domain names from the configuration by calling the completion handler you pass to the method.

For Hotspot 2.0 Enterprise (802.1X) networks, the list contains HS 2.0 domain names, and for other Wi-Fi networks, it contains their SSID.

## Parameters

- `completionHandler`: A completion handler that accepts an array of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager/getconfiguredssids(completionhandler:))*