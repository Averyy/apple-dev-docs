# desiredKeys

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The fields to fetch for the requested records.

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
var desiredKeys: [String]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * desiredKeys;
```

#### Discussion

Use this property to limit the amount of data that the system retrieves for each record during the fetch operation. This property contains an array of strings, each of which contains the name of a field from the target records. When you retrieve a record, the returned records only include fields with names that match one of the keys in this property. The default value is `nil`, which causes the system to fetch all keys of the record.

Because you can fetch records of different types, configure the array to include the merged set of all field names for the requested records and at least one field name from each record type.

If you intend to specify the desired set of keys, set the value of this property before executing the operation or submitting it to a queue.

## See Also

### Configuring the Fetch Record Changes Operation
- [var recordZoneID: CKRecordZone.ID?](./recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var previousServerChangeToken: CKServerChangeToken?](./previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of changed records to report with this operation object.
- [var moreComing: Bool](./morecoming.md)
  A Boolean value that indicates whether more results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/desiredkeys)*