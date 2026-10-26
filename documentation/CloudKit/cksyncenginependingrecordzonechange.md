# CKSyncEnginePendingRecordZoneChange

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that describes an unsent record modification.

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
@interface CKSyncEnginePendingRecordZoneChange : NSObject
```

## Topics

### Creating a record zone change
- [- initWithRecordID:type:](./cksyncenginependingrecordzonechange/initwithrecordid_type_.md)
  Creates a record zone change of the specified type for the given record.
### Accessing the modified record
- [recordID](./cksyncenginependingrecordzonechange/recordid.md)
  The identifier of the modified record.
- [type](./cksyncenginependingrecordzonechange/type.md)
  The type of change to make.
- [enum CKSyncEnginePendingRecordZoneChangeType](./cksyncenginependingrecordzonechangetype.md)
  A type of change in a record zone that needs to be sent to the server.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Modifying pending changes
- [- addPendingDatabaseChanges:](./cksyncenginestate/addpendingdatabasechanges_.md)
  Adds the specified database changes to the state.
- [- removePendingDatabaseChanges:](./cksyncenginestate/removependingdatabasechanges_.md)
  Removes the specified database changes from the state.
- [CKSyncEnginePendingZoneDelete](./cksyncenginependingzonedelete.md)
  An object that describes an unsent record zone deletion.
- [CKSyncEnginePendingZoneSave](./cksyncenginependingzonesave.md)
  An object that describes an unsent record zone modification.
- [CKSyncEnginePendingDatabaseChange](./cksyncenginependingdatabasechange.md)
  An object that describes an unsent database modification.
- [- addPendingRecordZoneChanges:](./cksyncenginestate/addpendingrecordzonechanges_.md)
  Adds the specified record zone changes to the state.
- [- removePendingRecordZoneChanges:](./cksyncenginestate/removependingrecordzonechanges_.md)
  Removes the specified record zone changes from the state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginependingrecordzonechange)*