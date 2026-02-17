# CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave

**Framework**: CloudKit  
**Kind**: struct

A type that describes an unsuccessful attempt to modify a single record zone.

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
struct FailedZoneSave
```

## Topics

### Accessing the record zone
- [let zone: CKRecordZone](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesave/zone.md)
  The record zone that CloudKit is unable to modify.
### Accessing the error
- [let error: CKError](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesave/error.md)
  An error that describes the reason for the unsuccessful attempt to modify the associated record zone.
### Debugging the type
- [var description: String](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesave/description.md)
  A textual description of the type that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesave/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let failedZoneDeletes: [CKRecordZone.ID : CKError]](cksyncengine-5sie5/event/sentdatabasechanges/failedzonedeletes.md)
  The unique identifiers of the record zones CloudKit is unable to delete, and the reasons why.
- [let failedZoneSaves: [CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave]](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesaves.md)
  The record zones that CloudKit is unable to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentdatabasechanges/failedzonesave)*