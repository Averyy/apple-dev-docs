# resultsLimit

**Framework**: CloudKit  
**Kind**: property

The maximum number of records to fetch from the record zone.

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
var resultsLimit: Int { get set }
```

#### Discussion

Use this property to limit the number of results in situations where you expect a large number of records. The default value is 0, which causes the server to return an appropriate number of records using dynamic conditions.

When the number of records that CloudKit returns exceeds this limit, the operation sets the `moreComing` property to [`true`](https://developer.apple.com/documentation/swift/true) when executing the [`recordZoneFetchResultBlock`](ckfetchrecordzonechangesoperation/recordzonefetchresultblock.md) handler.

## See Also

- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordzonechangesoperation/zoneconfiguration/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [CKRecord.FieldKey]?](ckfetchrecordzonechangesoperation/zoneconfiguration/desiredkeys.md)
  The fields to fetch for the requested records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneconfiguration/resultslimit)*