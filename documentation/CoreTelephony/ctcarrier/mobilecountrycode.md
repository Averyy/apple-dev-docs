# mobileCountryCode

**Framework**: Core Telephony  
**Kind**: property

The mobile country code (MCC) for the user’s cellular service provider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mobileCountryCode: String? { get }
```

#### Discussion

A read-only [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object that contains the numeric mobile country code for the user’s cellular service provider. MCCs are defined by ITU-T Recommendation E.212, “List of Mobile Country or Geographical Area Codes”. Typing this property as an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object, rather than a number type, preserves leading zeroes in MCCs.

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
- [var mobileNetworkCode: String?](ctcarrier/mobilenetworkcode.md)
  The mobile network code for the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier/mobilecountrycode)*