# lifeTimeInDays

**Framework**: Network Extension  
**Kind**: property

The number of days the network retains the associated configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@NSCopying
var lifeTimeInDays: NSNumber { get set }
```

#### Discussion

The minimum value is 1 day and the maximum value is 365 days. If this property is not set or is set to an invalid value the configuration never expires.

This property doesn’t apply to Enterprise or HS2.0 networks.

## See Also

- [var ssid: String](nehotspotconfiguration/ssid.md)
  The SSID of an open, WEP, WPA/WPA2 personal, or WPA/WPA2 enterprise Wi-Fi network.
- [var ssidPrefix: String](nehotspotconfiguration/ssidprefix.md)
  The string used to match networks against a known SSID prefix.
- [var joinOnce: Bool](nehotspotconfiguration/joinonce.md)
  Restricts the lifetime of a configuration to the operating status of the app that created it.
- [var hidden: Bool](nehotspotconfiguration/hidden.md)
  A Boolean value that indicates the visibility of the SSID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/lifetimeindays)*