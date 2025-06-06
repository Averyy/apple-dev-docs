# failedZoneDeletes

**Framework**: CloudKit  
**Kind**: property

The unique identifiers of the record zones CloudKit is unable to delete, and the reasons why.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
let failedZoneDeletes: [CKRecordZone.ID : CKError]
```

## See Also

- [let failedZoneSaves: [CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave]](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesaves.md)
  The record zones that CloudKit is unable to modify.
- [CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesave.md)
  A type that describes an unsuccessful attempt to modify a single record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentdatabasechanges/failedzonedeletes)*