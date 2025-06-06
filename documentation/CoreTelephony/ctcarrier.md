# CTCarrier

**Framework**: Core Telephony  
**Kind**: class

Information about the user’s cellular service provider, such as its unique identifier and whether it allows VoIP calls on its network.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CTCarrier
```

## Topics

### Getting Information About the Cellular Service Provider
- [var allowsVOIP: Bool](ctcarrier/allowsvoip.md)
  Indicates if the carrier allows making VoIP calls on its network.
- [var carrierName: String?](ctcarrier/carriername.md)
  The name of the user’s home cellular service provider.
- [var isoCountryCode: String?](ctcarrier/isocountrycode.md)
  The ISO country code for the user’s cellular service provider.
- [var mobileCountryCode: String?](ctcarrier/mobilecountrycode.md)
  The mobile country code (MCC) for the user’s cellular service provider.
- [var mobileNetworkCode: String?](ctcarrier/mobilenetworkcode.md)
  The mobile network code for the user’s cellular service provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CTTelephonyNetworkInfo](cttelephonynetworkinfo.md)
  An object that provides notifications of changes to the user’s cellular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcarrier)*