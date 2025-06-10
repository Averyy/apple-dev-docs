# CKSyncEngine.Event.AccountChange

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about a change to the device’s iCloud account.

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

> ❗ **Important**:  When a sync engine detects a change to the device’s iCloud account, it resets its internal state, including unsaved changes to both records and record zones. Your app needs to handle this scenario gracefully.

## Topics

### Understanding the change
- [let changeType: CKSyncEngine.Event.AccountChange.ChangeType](cksyncengine-5sie5/event/accountchange/changetype-swift.property.md)
  The iCloud account’s change type.
- [CKSyncEngine.Event.AccountChange.ChangeType](cksyncengine-5sie5/event/accountchange/changetype-swift.enum.md)
  Describes a change to the device’s iCloud account.
- [enum CKSyncEngineAccountChangeType](cksyncengineaccountchangetype.md)
  Describes a change to the device’s iCloud account.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case accountChange(CKSyncEngine.Event.AccountChange)](cksyncengine-5sie5/event/accountchange(_:).md)
  An event indicating a change to the device’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange)*