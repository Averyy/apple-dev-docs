# previousServerChangeToken

**Framework**: CloudKit  
**Kind**: property

The token that identifies the starting point for retrieving changes.

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
@NSCopying
var previousServerChangeToken: CKServerChangeToken? { get set }
```

#### Discussion

Each fetch request returns a unique token in addition to any changes. The token passes as a parameter to your [`fetchRecordChangesCompletionBlock`](ckfetchrecordchangesoperation/fetchrecordchangescompletionblock.md) handler. During a subsequent fetch request, providing the previous token causes the server to return only the changes that occur after the previous fetch request. Tokens are opaque data objects that you can write to disk safely and reuse later.

Typically, you set the value of this property when you initialize the operation object. If you intend to change the record zone, update the value of the property before executing the operation or submitting it to a queue.

## See Also

- [var recordZoneID: CKRecordZone.ID?](ckfetchrecordchangesoperation/recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var desiredKeys: [String]?](ckfetchrecordchangesoperation/desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](ckfetchrecordchangesoperation/resultslimit.md)
  The maximum number of changed records to report with this operation object.
- [var moreComing: Bool](ckfetchrecordchangesoperation/morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/previousserverchangetoken)*