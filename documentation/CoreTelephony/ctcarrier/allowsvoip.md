# allowsVOIP

**Framework**: Core Telephony  
**Kind**: property

Indicates if the carrier allows making VoIP calls on its network.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var allowsVOIP: Bool { get }
```

#### Discussion

A read-only Boolean value that is [`true`](https://developer.apple.com/documentation/Swift/true) if the carrier allows making VoIP calls on its network, or [`false`](https://developer.apple.com/documentation/Swift/false) if not.

If you configure a device for a carrier and then remove the SIM card, this property retains the Boolean value indicating the carrier’s policy regarding VoIP. If you then install a new SIM card, its VoIP policy Boolean replaces the previous value of this property.

## See Also

- [var carrierName: String?](ctcarrier/carriername.md)
  The name of the user’s home cellular service provider.
- [var isoCountryCode: String?](ctcarrier/isocountrycode.md)
  The ISO country code for the user’s cellular service provider.
- [var mobileCountryCode: String?](ctcarrier/mobilecountrycode.md)
  The mobile country code (MCC) for the user’s cellular service provider.
- [var mobileNetworkCode: String?](ctcarrier/mobilenetworkcode.md)
  The mobile network code for the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier/allowsvoip)*