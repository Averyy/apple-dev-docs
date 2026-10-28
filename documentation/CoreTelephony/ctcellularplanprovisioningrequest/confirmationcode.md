# confirmationCode

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The provisioning request’s confirmation code, provided by the network operator when initiating an eSIM download.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var confirmationCode: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * confirmationCode;
```

## Discussion

This property is optional.

## See Also

### Specifying Request Properties
- [var address: String](./address.md)
  The address of the carrier network’s eSIM server.
- [var eid: String?](./eid.md)
  The provisioning request’s eUICC identifier (EID).
- [var iccid: String?](./iccid.md)
  The provisioning request’s Integrated Circuit Card Identifier (ICCID).
- [var matchingID: String?](./matchingid.md)
  The provisioning request’s matching identifier (MatchingID).
- [var oid: String?](./oid.md)
  The provisioning request’s Object Identifier (OID).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest/confirmationcode)*