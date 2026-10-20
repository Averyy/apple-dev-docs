# oid

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The provisioning request’s Object Identifier (OID).

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var oid: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * OID;
```

#### Discussion

This property is optional.

## See Also

### Specifying Request Properties
- [var address: String](./address.md)
  The address of the carrier network’s eSIM server.
- [var confirmationCode: String?](./confirmationcode.md)
  The provisioning request’s confirmation code, provided by the network operator when initiating an eSIM download.
- [var eid: String?](./eid.md)
  The provisioning request’s eUICC identifier (EID).
- [var iccid: String?](./iccid.md)
  The provisioning request’s Integrated Circuit Card Identifier (ICCID).
- [var matchingID: String?](./matchingid.md)
  The provisioning request’s matching identifier (MatchingID).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest/oid)*