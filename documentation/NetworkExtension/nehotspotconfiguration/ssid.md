# ssid

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSString * SSID;
```

## Discussion

An SSID is a string of 1-32 characters.

For Hotspot 2.0 networks, your application must use domain names instead of SSIDs.

This API does not support hidden SSIDs.

## See Also

### Accessing configuration properties
- [var ssidPrefix: String](./ssidprefix.md)
  The string used to match networks against a known SSID prefix.
- [var lifeTimeInDays: NSNumber](./lifetimeindays.md)
  The number of days the network retains the associated configuration.
- [var joinOnce: Bool](./joinonce.md)
  Restricts the lifetime of a configuration to the operating status of the app that created it.
- [var hidden: Bool](./hidden.md)
  A Boolean value that indicates the visibility of the SSID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfiguration/ssid)*