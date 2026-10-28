# moreComing

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether more results are available.

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
var moreComing: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL moreComing;
```

## Discussion

If the server is unable to deliver all of the changed results with this operation object, it sets this property to [`true`](../../Swift/true.md) before executing the block in the [`fetchRecordChangesCompletionBlock`](./fetchrecordchangescompletionblock.md) property. To fetch the remaining changes, create a new [`CKFetchRecordChangesOperation`](../ckfetchrecordchangesoperation.md) object using the change token that the server returns.

## See Also

### Configuring the Fetch Record Changes Operation
- [var recordZoneID: CKRecordZone.ID?](./recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var previousServerChangeToken: CKServerChangeToken?](./previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [String]?](./desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of changed records to report with this operation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/morecoming)*