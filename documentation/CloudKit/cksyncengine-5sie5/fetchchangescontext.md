# CKSyncEngine.FetchChangesContext

**Framework**: CloudKit  
**Kind**: struct

The context of an attempt to fetch changes from the server.

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
struct FetchChangesContext
```

#### Overview

The sync engine might attempt to fetch changes from the server for many reasons. For example, if you call [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md), it tries to fetch changes immediately. Or if it receives a push notification, it schedules an automatic sync and fetch changes when the scheduler task runs.

## Topics

### Instance Properties
- [let options: CKSyncEngine.FetchChangesOptions](cksyncengine-5sie5/fetchchangescontext/options.md)
  The options being used for this attempt to fetch changes.
- [let reason: CKSyncEngine.SyncReason](cksyncengine-5sie5/fetchchangescontext/reason.md)
  The reason why the sync engine is attempting to fetch changes.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchangescontext)*