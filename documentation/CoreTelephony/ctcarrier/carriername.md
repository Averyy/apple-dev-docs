# carrierName

**Framework**: Core Telephony  
**Kind**: property

The name of the user’s home cellular service provider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var carrierName: String? { get }
```

#### Discussion

The carrier provides this string, formatting it for presentation to the user. The value does not change if the user is roaming; it always represents the provider with which the user has an account.

If you configure a device for a carrier and then remove the SIM card, this property retains the name of the carrier. If you then install a new SIM card, its carrier name replaces the previous value of this property.

The value for this property is `nil` if the user never configured a carrier for the device.

## See Also

- [var allowsVOIP: Bool](ctcarrier/allowsvoip.md)
  Indicates if the carrier allows making VoIP calls on its network.
- [var isoCountryCode: String?](ctcarrier/isocountrycode.md)
  The ISO country code for the user’s cellular service provider.
- [var mobileCountryCode: String?](ctcarrier/mobilecountrycode.md)
  The mobile country code (MCC) for the user’s cellular service provider.
- [var mobileNetworkCode: String?](ctcarrier/mobilenetworkcode.md)
  The mobile network code for the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier/carriername)*