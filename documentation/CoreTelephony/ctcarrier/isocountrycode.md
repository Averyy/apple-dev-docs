# isoCountryCode

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The ISO country code for the user’s cellular service provider.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0

> **Deprecated**: Deprecated; returns '--' at some point in the future

## Declaration

```swift
var isoCountryCode: String? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSString * isoCountryCode;
```

## Discussion

This property uses the ISO 3166-1 country code representation.

The value for this property is `nil` if any of the following apply:

- The device is in airplane mode.
- There is no SIM card in the device.
- The device is outside of cellular service range.

## See Also

### Getting Information About the Cellular Service Provider
- [var allowsVOIP: Bool](./allowsvoip.md)
  Indicates if the carrier allows making VoIP calls on its network.
- [var carrierName: String?](./carriername.md)
  The name of the user’s home cellular service provider.
- [var mobileCountryCode: String?](./mobilecountrycode.md)
  The mobile country code (MCC) for the user’s cellular service provider.
- [var mobileNetworkCode: String?](./mobilenetworkcode.md)
  The mobile network code for the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier/isocountrycode)*