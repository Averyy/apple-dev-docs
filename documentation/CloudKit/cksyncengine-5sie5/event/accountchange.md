# CKSyncEngine.Event.AccountChange

**Framework**: CloudKit  
**Kind**: struct

The user signed in or out of their account.

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
struct AccountChange
```

#### Overview

The sync engine automatically listens for account changes, and it sends this event when the user signs in or out. It’s your responsibility to react appropriately to this change and update your local persistence.

When the logged-in account changes, the sync engine resets its internal state. This means that it clears any pending database or record zone changes that you may have added.

Note that it’s possible the account changes multiple times while your app is quit. If this happens, you only receive one account change event representing the transition between the last known state and the current state.

> ❗ **Important**: When a sync engine detects a change to the device’s iCloud account, it resets its internal state, including unsaved changes to both records and record zones. Your app needs to handle this scenario gracefully.

## Topics

### Understanding the change
- [let changeType: CKSyncEngine.Event.AccountChange.ChangeType](cksyncengine-5sie5/event/accountchange/changetype-swift.property.md)
  The iCloud account’s change type.
- [CKSyncEngine.Event.AccountChange.ChangeType](cksyncengine-5sie5/event/accountchange/changetype-swift.enum.md)
  Describes a change to the device’s iCloud account.
- [enum CKSyncEngineAccountChangeType](cksyncengineaccountchangetype.md)
  Describes a change to the device’s iCloud account.
### Debugging the event
- [var description: String](cksyncengine-5sie5/event/accountchange/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/accountchange/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case accountChange(CKSyncEngine.Event.AccountChange)](cksyncengine-5sie5/event/accountchange(_:).md)
  The user signed in or out of their account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange)*