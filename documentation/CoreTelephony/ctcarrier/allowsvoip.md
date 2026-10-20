# allowsVOIP

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

Indicates if the carrier allows making VoIP calls on its network.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0

> **Deprecated**: Deprecated; returns YES at some point in the future

## Declaration

```swift
var allowsVOIP: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL allowsVOIP;
```

#### Discussion

A read-only Boolean value that is [`true`](../../Swift/true.md) if the carrier allows making VoIP calls on its network, or [`false`](../../Swift/false.md) if not.

If you configure a device for a carrier and then remove the SIM card, this property retains the Boolean value indicating the carrier’s policy regarding VoIP. If you then install a new SIM card, its VoIP policy Boolean replaces the previous value of this property.

## See Also

### Getting Information About the Cellular Service Provider
- [var carrierName: String?](./carriername.md)
  The name of the user’s home cellular service provider.
- [var isoCountryCode: String?](./isocountrycode.md)
  The ISO country code for the user’s cellular service provider.
- [var mobileCountryCode: String?](./mobilecountrycode.md)
  The mobile country code (MCC) for the user’s cellular service provider.
- [var mobileNetworkCode: String?](./mobilenetworkcode.md)
  The mobile network code for the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier/allowsvoip)*