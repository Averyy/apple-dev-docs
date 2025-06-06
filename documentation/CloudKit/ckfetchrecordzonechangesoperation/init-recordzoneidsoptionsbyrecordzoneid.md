# init(recordZoneIDs:optionsByRecordZoneID:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for fetching record zone changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(recordZoneIDs: [CKRecordZone.ID], optionsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneOptions]? = nil)
```

#### Discussion

CloudKit configures the operation for retrieving all of the record zones that you specify. If you want to reduce the amount of data that CloudKit returns, provide zone options for each record zone.

## Parameters

- `recordZoneIDs`: The IDs of the record zones that you want to query for changes.
- `optionsByRecordZoneID`: A dictionary that maps record zone IDs to their corresponding options. You can specify   for this parameter.

## See Also

- [CKFetchRecordZoneChangesOperation.ZoneOptions](ckfetchrecordzonechangesoperation/zoneoptions.md)
  A configuration object that describes the information to fetch from a record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/init(recordzoneids:optionsbyrecordzoneid:))*