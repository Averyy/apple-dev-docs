# init(recordZoneIDs:optionsByRecordZoneID:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an operation for fetching record zone changes.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 5.0

> **Deprecated**: Use [`init(recordZoneIDs:configurationsByRecordZoneID:)`](./init%28recordzoneids,configurationsbyrecordzoneid%29.md) instead.

## Declaration

```swift
convenience init(recordZoneIDs: [CKRecordZone.ID], optionsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneOptions]? = nil)
```

```objc
- (instancetype) initWithRecordZoneIDs:(NSArray<CKRecordZoneID *> *) recordZoneIDs optionsByRecordZoneID:(NSDictionary<CKRecordZoneID *,CKFetchRecordZoneChangesOptions *> *) optionsByRecordZoneID;
```

#### Discussion

CloudKit configures the operation for retrieving all of the record zones that you specify. If you want to reduce the amount of data that CloudKit returns, provide zone options for each record zone.

## Parameters

- `recordZoneIDs`: The IDs of the record zones that you want to query for changes.
- `optionsByRecordZoneID`: A dictionary that maps record zone IDs to their corresponding options. You can specify `nil` for this parameter.

## See Also

### Deprecated Methods
- [CKFetchRecordZoneChangesOperation.ZoneOptions](./zoneoptions.md)
  A configuration object that describes the information to fetch from a record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/init(recordzoneids:optionsbyrecordzoneid:))*