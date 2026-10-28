# recordZoneID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The ID of the record zone with the records you want to fetch.

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
var recordZoneID: CKRecordZone.ID? { get set }
```

```objc
@property (nonatomic, copy, nullable) CKRecordZoneID * recordZoneID;
```

## Discussion

Typically, you set the value of this property when you initialize the operation object. If you intend to change the record zone, update the value before executing the operation or submitting it to a queue.

## See Also

### Configuring the Fetch Record Changes Operation
- [var previousServerChangeToken: CKServerChangeToken?](./previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [String]?](./desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of changed records to report with this operation object.
- [var moreComing: Bool](./morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/recordzoneid)*