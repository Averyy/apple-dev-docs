# address

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The address of the carrier network’s eSIM server.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var address: String { get set }
```

```objc
@property (nonatomic, strong, nonnull) NSString * address;
```

#### Discussion

The destination server must support the SMDP+ standard.

You must set this property for the request to be valid.

## See Also

### Specifying Request Properties
- [var confirmationCode: String?](./confirmationcode.md)
  The provisioning request’s confirmation code, provided by the network operator when initiating an eSIM download.
- [var eid: String?](./eid.md)
  The provisioning request’s eUICC identifier (EID).
- [var iccid: String?](./iccid.md)
  The provisioning request’s Integrated Circuit Card Identifier (ICCID).
- [var matchingID: String?](./matchingid.md)
  The provisioning request’s matching identifier (MatchingID).
- [var oid: String?](./oid.md)
  The provisioning request’s Object Identifier (OID).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest/address)*