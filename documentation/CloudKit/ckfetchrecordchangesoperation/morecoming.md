# moreComing

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether more results are available.

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
var moreComing: Bool { get }
```

#### Discussion

If the server is unable to deliver all of the changed results with this operation object, it sets this property to [`true`](https://developer.apple.com/documentation/Swift/true) before executing the block in the [`fetchRecordChangesCompletionBlock`](ckfetchrecordchangesoperation/fetchrecordchangescompletionblock.md) property. To fetch the remaining changes, create a new [`CKFetchRecordChangesOperation`](ckfetchrecordchangesoperation.md) object using the change token that the server returns.

## See Also

- [var recordZoneID: CKRecordZone.ID?](ckfetchrecordchangesoperation/recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordchangesoperation/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [String]?](ckfetchrecordchangesoperation/desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](ckfetchrecordchangesoperation/resultslimit.md)
  The maximum number of changed records to report with this operation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/morecoming)*