# hidden

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates the visibility of the SSID.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var hidden: Bool { get set }
```

#### Discussion

Set this value to [`true`](https://developer.apple.com/documentation/Swift/true) to make the system perform an active scan for the Service Set Identifier (SSID). If the access point is already broadcasting the SSID, set this value to [`false`](https://developer.apple.com/documentation/Swift/false).

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var ssid: String](nehotspotconfiguration/ssid.md)
  The SSID of an open, WEP, WPA/WPA2 personal, or WPA/WPA2 enterprise Wi-Fi network.
- [var ssidPrefix: String](nehotspotconfiguration/ssidprefix.md)
  The string used to match networks against a known SSID prefix.
- [var lifeTimeInDays: NSNumber](nehotspotconfiguration/lifetimeindays.md)
  The number of days the network retains the associated configuration.
- [var joinOnce: Bool](nehotspotconfiguration/joinonce.md)
  Restricts the lifetime of a configuration to the operating status of the app that created it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/hidden)*