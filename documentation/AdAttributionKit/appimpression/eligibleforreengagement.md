# eligibleForReengagement

**Framework**: AdAttributionKit  
**Kind**: property

A Boolean value that indicates whether this impression is eligible for reengagement.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+

## Declaration

```swift
var eligibleForReengagement: Bool { get }
```

## See Also

- [var adNetworkID: String](appimpression/adnetworkid.md)
  The advertising network ID.
- [var advertisedItemID: UInt64](appimpression/advertiseditemid.md)
  The advertised item’s ID.
- [var compactJWSRepresentation: String](appimpression/compactjwsrepresentation.md)
  A string that presents the compact representation of the impression’s JSON Web Signature (JWS).
- [var id: UUID](appimpression/id.md)
  The impression’s unique ID.
- [var keyID: String](appimpression/keyid.md)
  The JSON Web Signature (JWS) key ID.
- [var publisherItemID: UInt64](appimpression/publisheritemid.md)
  The publisher app’s item ID.
- [var sourceID: Int](appimpression/sourceid.md)
  A four-digit integer that ad networks define to represent the ad campaign.
- [var timestamp: Date](appimpression/timestamp.md)
  The impression’s timestamp, in milliseconds since 1970.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/eligibleforreengagement)*