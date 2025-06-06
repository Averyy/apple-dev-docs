# init(recordZonesToSave:recordZoneIDsToDelete:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for modifying the specified record zones.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
convenience init(recordZonesToSave: [CKRecordZone]? = nil, recordZoneIDsToDelete: [CKRecordZone.ID]? = nil)
```

#### Discussion

The record zones you intend to save or delete must all reside in the same database, which you specify when you configure the operation. If you delete a record zone, CloudKit deletes any records it contains.

## Parameters

- `recordZonesToSave`: The record zones to save. You can specify   for this parameter.
- `recordZoneIDsToDelete`: The IDs of the record zones to delete. You can specify   for this parameter.

## See Also

- [init()](ckmodifyrecordzonesoperation/init.md)
  Creates an empty modify record zones operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/init(recordzonestosave:recordzoneidstodelete:))*