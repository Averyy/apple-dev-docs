# ssidPrefix

**Framework**: Network Extension  
**Kind**: property

The string used to match networks against a known SSID prefix.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var ssidPrefix: String { get }
```

#### Discussion

This property is only populated for configuration instances initialized with SSID prefix strings. The property is an empty string if the configuration instance has a full [`ssid`](nehotspotconfiguration/ssid.md).

## See Also

- [var ssid: String](nehotspotconfiguration/ssid.md)
  The SSID of an open, WEP, WPA/WPA2 personal, or WPA/WPA2 enterprise Wi-Fi network.
- [var lifeTimeInDays: NSNumber](nehotspotconfiguration/lifetimeindays.md)
  The number of days the network retains the associated configuration.
- [var joinOnce: Bool](nehotspotconfiguration/joinonce.md)
  Restricts the lifetime of a configuration to the operating status of the app that created it.
- [var hidden: Bool](nehotspotconfiguration/hidden.md)
  A Boolean value that indicates the visibility of the SSID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/ssidprefix)*