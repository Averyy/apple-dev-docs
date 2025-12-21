# sourceID

**Framework**: AdAttributionKit  
**Kind**: property

A four-digit integer that ad networks define to represent the ad campaign.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
var sourceID: Int { get }
```

#### Discussion

The `sourceID` is also known as the . Ad networks and developers define its meaning. This integer can have up to four digits. You might receive two, three, or all four digits of the `sourceID` in the first winning postback, based on the data tier of the postback. You can use the different digits of the source identifier to represent different aspects of your ad, such as campaign information, placement, locale, and so on. For more information about the values you might get in the postback, see [`Identifying the parameters in a postback`](identifying-the-parameters-in-a-postback.md).

> **Note**: A postback report represents this integer as a string in the `source-identifier` parameter in the payload of the JSON Web Signature (JWS). For more details about the parameters of a postback, see [`Identifying the parameters in a postback`](identifying-the-parameters-in-a-postback.md).

## See Also

- [var adNetworkID: String](appimpression/adnetworkid.md)
  The advertising network ID.
- [var advertisedItemID: UInt64](appimpression/advertiseditemid.md)
  The advertised item’s ID.
- [var compactJWSRepresentation: String](appimpression/compactjwsrepresentation.md)
  A string that presents the compact representation of the impression’s JSON Web Signature (JWS).
- [var eligibleForReengagement: Bool](appimpression/eligibleforreengagement.md)
  A Boolean value that indicates whether this impression is eligible for reengagement.
- [var id: UUID](appimpression/id.md)
  The impression’s unique ID.
- [var keyID: String](appimpression/keyid.md)
  The JSON Web Signature (JWS) key ID.
- [var publisherItemID: UInt64](appimpression/publisheritemid.md)
  The publisher app’s item ID.
- [var timestamp: Date](appimpression/timestamp.md)
  The impression’s timestamp, in milliseconds since 1970.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/sourceid)*