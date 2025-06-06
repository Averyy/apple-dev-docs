# ssid

**Framework**: Network Extension  
**Kind**: property

The SSID of an open, WEP, WPA/WPA2 personal, or WPA/WPA2 enterprise Wi-Fi network.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var ssid: String { get }
```

#### Discussion

An SSID is a string of 1-32 characters.

For Hotspot 2.0 networks, your application must use domain names instead of SSIDs.

This API does not support hidden SSIDs.

## See Also

- [var ssidPrefix: String](nehotspotconfiguration/ssidprefix.md)
  The string used to match networks against a known SSID prefix.
- [var lifeTimeInDays: NSNumber](nehotspotconfiguration/lifetimeindays.md)
  The number of days the network retains the associated configuration.
- [var joinOnce: Bool](nehotspotconfiguration/joinonce.md)
  Restricts the lifetime of a configuration to the operating status of the app that created it.
- [var hidden: Bool](nehotspotconfiguration/hidden.md)
  A Boolean value that indicates the visibility of the SSID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/ssid)*