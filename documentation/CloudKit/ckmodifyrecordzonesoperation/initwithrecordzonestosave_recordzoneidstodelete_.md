# initWithRecordZonesToSave:recordZoneIDsToDelete:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates an operation for modifying the specified record zones.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
- (instancetype) initWithRecordZonesToSave:(NSArray<CKRecordZone *> *) recordZonesToSave recordZoneIDsToDelete:(NSArray<CKRecordZoneID *> *) recordZoneIDsToDelete;
```

#### Discussion

The record zones you intend to save or delete must all reside in the same database, which you specify when you configure the operation. If you delete a record zone, CloudKit deletes any records it contains.

## Parameters

- `recordZonesToSave`: The record zones to save. You can specify `nil` for this parameter.
- `recordZoneIDsToDelete`: The IDs of the record zones to delete. You can specify `nil` for this parameter.

## See Also

### Creating a Modify Zones Operation
- [init()](./init%28%29.md)
  Creates an empty modify record zones operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/initwithrecordzonestosave:recordzoneidstodelete:)*