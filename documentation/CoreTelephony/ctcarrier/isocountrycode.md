# isoCountryCode

**Framework**: Core Telephony  
**Kind**: property

The ISO country code for the user’s cellular service provider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isoCountryCode: String? { get }
```

#### Discussion

This property uses the ISO 3166-1 country code representation.

The value for this property is `nil` if any of the following apply:

- The device is in airplane mode.
- There is no SIM card in the device.
- The device is outside of cellular service range.

## See Also

- [var allowsVOIP: Bool](ctcarrier/allowsvoip.md)
  Indicates if the carrier allows making VoIP calls on its network.
- [var carrierName: String?](ctcarrier/carriername.md)
  The name of the user’s home cellular service provider.
- [var mobileCountryCode: String?](ctcarrier/mobilecountrycode.md)
  The mobile country code (MCC) for the user’s cellular service provider.
- [var mobileNetworkCode: String?](ctcarrier/mobilenetworkcode.md)
  The mobile network code for the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier/isocountrycode)*