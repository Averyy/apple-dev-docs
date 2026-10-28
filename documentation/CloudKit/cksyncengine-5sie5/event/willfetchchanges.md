# CKSyncEngine.Event.WillFetchChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

The sync engine is about to fetch changes from the server.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct WillFetchChanges
```

## Overview

The sync engine delivers the changes themselves via [`CKSyncEngine.Event.FetchedDatabaseChanges`](./fetcheddatabasechanges.md) and [`CKSyncEngine.Event.FetchedRecordZoneChanges`](./fetchedrecordzonechanges.md).

Note that this event might not always occur every time you call [`fetchChanges(_:)`](../fetchchanges%28_%29.md). For example, if you call [`fetchChanges(_:)`](../fetchchanges%28_%29.md) concurrently while the engine is already fetching changes, this event might not be sent. Similarly, if there’s no logged-in account, the engine might short-circuit the call to [`fetchChanges(_:)`](../fetchchanges%28_%29.md), and this event won’t be sent.

## Topics

### Debugging the event
- [var description: String](./willfetchchanges/description.md)
  The textual description of the event that’s suitable for logging.
### Instance Properties
- [let context: CKSyncEngine.FetchChangesContext](./willfetchchanges/context.md)
### Default Implementations
- [CustomStringConvertible Implementations](./willfetchchanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Remote database changes
- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](./willfetchchanges%28_%29.md)
  The sync engine is about to fetch changes from the server.
- [case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)](./fetcheddatabasechanges%28_%29.md)
  The sync engine has fetched new database changes from the server.
- [CKSyncEngine.Event.FetchedDatabaseChanges](./fetcheddatabasechanges.md)
  A type that provides information about fetched database changes.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](./didfetchchanges%28_%29.md)
  The sync engine finished fetching changes from the server.
- [CKSyncEngine.Event.DidFetchChanges](./didfetchchanges.md)
  A type that provides information about a finished database fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/willfetchchanges)*