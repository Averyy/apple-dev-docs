# desiredKeys

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The fields to fetch for the requested records.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- iPadOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- macOS 10.12+ - Deprecated in 10.14 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- tvOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- watchOS 3.0+ - Deprecated in 5.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)

## Declaration

```swift
var desiredKeys: [String]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * desiredKeys;
```

#### Discussion

Use this property to limit the amount of data that CloudKit retrieves for each record during the fetch operation. This property contains an array of strings, each of which is the name of a field from the target records. When you retrieve a record, CloudKit only includes fields with names that match one of the keys in this property. The default value is `nil`, which causes CloudKit to fetch all of the record’s keys.

Because you can fetch records of different types, configure the array to include the merged set of all field names for the requested records and at least one field name from each record type.

If you intend to specify the desired set of keys, set the value of this property before executing the operation or submitting it to a queue.

## See Also

### Zone Change Options
- [var previousServerChangeToken: CKServerChangeToken?](./previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of records to fetch from the record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/desiredkeys)*