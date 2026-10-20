# previousServerChangeToken

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The token that identifies the starting point for retrieving changes.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- iPadOS 8.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CKFetchRecordZoneChangesOperation)
- macOS 10.10+ - Deprecated in 10.12 (renamed: CKFetchRecordZoneChangesOperation)
- tvOS 9.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CKFetchRecordZoneChangesOperation)
- watchOS 3.0+ - Deprecated in 3.0 (renamed: CKFetchRecordZoneChangesOperation)

## Declaration

```swift
@NSCopying
var previousServerChangeToken: CKServerChangeToken? { get set }
```

```objc
@property (nonatomic, copy, nullable) CKServerChangeToken * previousServerChangeToken;
```

#### Discussion

Each fetch request returns a unique token in addition to any changes. The token passes as a parameter to your [`fetchRecordChangesCompletionBlock`](./fetchrecordchangescompletionblock.md) handler. During a subsequent fetch request, providing the previous token causes the server to return only the changes that occur after the previous fetch request. Tokens are opaque data objects that you can write to disk safely and reuse later.

Typically, you set the value of this property when you initialize the operation object. If you intend to change the record zone, update the value of the property before executing the operation or submitting it to a queue.

## See Also

### Configuring the Fetch Record Changes Operation
- [var recordZoneID: CKRecordZone.ID?](./recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var desiredKeys: [String]?](./desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of changed records to report with this operation object.
- [var moreComing: Bool](./morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/previousserverchangetoken)*