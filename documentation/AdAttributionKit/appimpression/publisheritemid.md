# publisherItemID

**Framework**: AdAttributionKit  
**Kind**: property  
**Role**: Instance Property

The publisher app’s item ID.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var publisherItemID: UInt64 { get }
```

## Mentions

- [Generating JWS impressions](../generating-jws-impressions.md)

## See Also

### Accessing ad impression properties
- [var adNetworkID: String](./adnetworkid.md)
  The advertising network ID.
- [var advertisedItemID: UInt64](./advertiseditemid.md)
  The advertised item’s ID.
- [var compactJWSRepresentation: String](./compactjwsrepresentation.md)
  A string that presents the compact representation of the impression’s JSON Web Signature (JWS).
- [var eligibleForReengagement: Bool](./eligibleforreengagement.md)
  A Boolean value that indicates whether this impression is eligible for reengagement.
- [var id: UUID](./id.md)
  The impression’s unique ID.
- [var keyID: String](./keyid.md)
  The JSON Web Signature (JWS) key ID.
- [var sourceID: Int](./sourceid.md)
  A four-digit integer that ad networks define to represent the ad campaign.
- [var timestamp: Date](./timestamp.md)
  The impression’s timestamp, in milliseconds since 1970.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/publisheritemid)*