# init(recordZoneIDs:configurationsByRecordZoneID:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for fetching record zone changes.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+
- watchOS 5.0+
- Swift 4.2+

## Declaration

```swift
convenience init(recordZoneIDs: [CKRecordZone.ID]? = nil, configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]? = nil)
```

#### Discussion

CloudKit configures the operation for retrieving all of the record zones that you specify. If you want to reduce the amount of data that CloudKit returns, provide zone configurations for each record zone.

## Parameters

- `recordZoneIDs`: The IDs of the record zones that you want to query for changes. You can specify   for this parameter.
- `configurationsByRecordZoneID`: A dictionary that maps record zone IDs to their corresponding configurations. You can specify   for this parameter.

## See Also

- [init()](ckfetchrecordzonechangesoperation/init.md)
  Creates an empty fetch record zone changes operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/init(recordzoneids:configurationsbyrecordzoneid:))*