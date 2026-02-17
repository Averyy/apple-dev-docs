# previousServerChangeToken

**Framework**: CloudKit  
**Kind**: property

The token that identifies the starting point for retrieving changes.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var previousServerChangeToken: CKServerChangeToken? { get set }
```

#### Discussion

Each fetch request returns a unique token in addition to any changes. CloudKit passes the token to your [`recordZoneFetchResultBlock`](ckfetchrecordzonechangesoperation/recordzonefetchresultblock.md) handler. During a subsequent fetch request, providing the previous token causes the server to return only the changes since the previous fetch request. Tokens are opaque values that you can write to disk safely and reuse later.

## See Also

- [var resultsLimit: Int](ckfetchrecordzonechangesoperation/zoneconfiguration/resultslimit.md)
  The maximum number of records to fetch from the record zone.
- [var desiredKeys: [CKRecord.FieldKey]?](ckfetchrecordzonechangesoperation/zoneconfiguration/desiredkeys.md)
  The fields to fetch for the requested records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneconfiguration/previousserverchangetoken)*