# mobileNetworkCode

**Framework**: Core Telephony  
**Kind**: property

The mobile network code for the user’s cellular service provider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mobileNetworkCode: String? { get }
```

#### Discussion

A read-only [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object that represents the numeric mobile network code (MNC) for the user’s cellular service provider. Typing this property as an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object, rather than a number type, preserves leading zeroes in MNCs.

The value for this property is `nil` if any of the following apply:

- There is no SIM card in the device.
- The device is outside of cellular service range.

The value may be `nil` on hardware prior to iPhone 4S when in airplane mode.

## See Also

- [var allowsVOIP: Bool](ctcarrier/allowsvoip.md)
  Indicates if the carrier allows making VoIP calls on its network.
- [var carrierName: String?](ctcarrier/carriername.md)
  The name of the user’s home cellular service provider.
- [var isoCountryCode: String?](ctcarrier/isocountrycode.md)
  The ISO country code for the user’s cellular service provider.
- [var mobileCountryCode: String?](ctcarrier/mobilecountrycode.md)
  The mobile country code (MCC) for the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier/mobilenetworkcode)*