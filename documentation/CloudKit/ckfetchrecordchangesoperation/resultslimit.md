# resultsLimit

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of changed records to report with this operation object.

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
var resultsLimit: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger resultsLimit;
```

## Discussion

Use this property to limit the number of results in situations where you expect the number of changed records to be large. The default value is 0, which causes the server to return an appropriate number of results using dynamic conditions.

When the number of returned results exceeds the results limit, the operation object sets the [`moreComing`](./morecoming.md) property to [`true`](../../Swift/true.md) before executing the block in the [`fetchRecordChangesCompletionBlock`](./fetchrecordchangescompletionblock.md) property. In your block, check the value of that property, and if it’s [`true`](../../Swift/true.md), create a new [`CKFetchRecordChangesOperation`](../ckfetchrecordchangesoperation.md) object to fetch more results.

## See Also

### Configuring the Fetch Record Changes Operation
- [var recordZoneID: CKRecordZone.ID?](./recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var previousServerChangeToken: CKServerChangeToken?](./previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [String]?](./desiredkeys.md)
  The fields to fetch for the requested records.
- [var moreComing: Bool](./morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/resultslimit)*