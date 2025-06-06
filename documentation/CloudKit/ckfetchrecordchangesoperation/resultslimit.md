# resultsLimit

**Framework**: CloudKit  
**Kind**: property

The maximum number of changed records to report with this operation object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var resultsLimit: Int { get set }
```

#### Discussion

Use this property to limit the number of results in situations where you expect the number of changed records to be large. The default value is 0, which causes the server to return an appropriate number of results using dynamic conditions.

When the number of returned results exceeds the results limit, the operation object sets the [`moreComing`](ckfetchrecordchangesoperation/morecoming.md) property to [`true`](https://developer.apple.com/documentation/swift/true) before executing the block in the [`fetchRecordChangesCompletionBlock`](ckfetchrecordchangesoperation/fetchrecordchangescompletionblock.md) property. In your block, check the value of that property, and if it’s [`true`](https://developer.apple.com/documentation/swift/true), create a new [`CKFetchRecordChangesOperation`](ckfetchrecordchangesoperation.md) object to fetch more results.

## See Also

- [var recordZoneID: CKRecordZone.ID?](ckfetchrecordchangesoperation/recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordchangesoperation/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [String]?](ckfetchrecordchangesoperation/desiredkeys.md)
  The fields to fetch for the requested records.
- [var moreComing: Bool](ckfetchrecordchangesoperation/morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/resultslimit)*