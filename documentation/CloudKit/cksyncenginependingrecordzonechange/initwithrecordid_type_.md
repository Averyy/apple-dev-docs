# initWithRecordID:type:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a record zone change of the specified type for the given record.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (instancetype) initWithRecordID:(CKRecordID *) recordID type:(CKSyncEnginePendingRecordZoneChangeType) type;
```

#### Return Value

An initialized record zone change.

## Parameters

- `recordID`: The identifier of the record to change.
- `type`: The type of change to make.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginependingrecordzonechange/initwithrecordid:type:)*