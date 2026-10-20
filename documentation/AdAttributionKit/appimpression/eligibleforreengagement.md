# eligibleForReengagement

**Framework**: AdAttributionKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this impression is eligible for reengagement.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var eligibleForReengagement: Bool { get }
```

## See Also

### Accessing ad impression properties
- [var adNetworkID: String](./adnetworkid.md)
  The advertising network ID.
- [var advertisedItemID: UInt64](./advertiseditemid.md)
  The advertised item’s ID.
- [var compactJWSRepresentation: String](./compactjwsrepresentation.md)
  A string that presents the compact representation of the impression’s JSON Web Signature (JWS).
- [var id: UUID](./id.md)
  The impression’s unique ID.
- [var keyID: String](./keyid.md)
  The JSON Web Signature (JWS) key ID.
- [var publisherItemID: UInt64](./publisheritemid.md)
  The publisher app’s item ID.
- [var sourceID: Int](./sourceid.md)
  A four-digit integer that ad networks define to represent the ad campaign.
- [var timestamp: Date](./timestamp.md)
  The impression’s timestamp, in milliseconds since 1970.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/eligibleforreengagement)*