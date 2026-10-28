# lifeTimeInDays

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy) NSNumber * lifeTimeInDays;
```

## Discussion

The minimum value is 1 day and the maximum value is 365 days. If this property is not set or is set to an invalid value the configuration never expires.

This property doesn’t apply to Enterprise or HS2.0 networks.

## See Also

### Accessing configuration properties
- [var ssid: String](./ssid.md)
  The SSID of an open, WEP, WPA/WPA2 personal, or WPA/WPA2 enterprise Wi-Fi network.
- [var ssidPrefix: String](./ssidprefix.md)
  The string used to match networks against a known SSID prefix.
- [var joinOnce: Bool](./joinonce.md)
  Restricts the lifetime of a configuration to the operating status of the app that created it.
- [var hidden: Bool](./hidden.md)
  A Boolean value that indicates the visibility of the SSID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/lifetimeindays)*