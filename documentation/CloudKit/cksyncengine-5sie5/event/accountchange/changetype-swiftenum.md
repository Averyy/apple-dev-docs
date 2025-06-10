# CKSyncEngine.Event.AccountChange.ChangeType

**Framework**: CloudKit  
**Kind**: enum

Describes a change to the device’s iCloud account.

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
enum ChangeType
```

## Topics

### Account change types
- [CKSyncEngine.Event.AccountChange.ChangeType.signIn(currentUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signin(currentuser:).md)
  A change indicating a sign-in to an iCloud account.
- [CKSyncEngine.Event.AccountChange.ChangeType.signOut(previousUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signout(previoususer:).md)
  A change indicating a sign-out of an iCloud account.
- [CKSyncEngine.Event.AccountChange.ChangeType.switchAccounts(previousUser:currentUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/switchaccounts(previoususer:currentuser:).md)
  A change indicating a switch between two iCloud accounts.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let changeType: CKSyncEngine.Event.AccountChange.ChangeType](cksyncengine-5sie5/event/accountchange/changetype-swift.property.md)
  The iCloud account’s change type.
- [enum CKSyncEngineAccountChangeType](cksyncengineaccountchangetype.md)
  Describes a change to the device’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange/changetype-swift.enum)*