# CKSyncEngine.Event.AccountChange.ChangeType

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Describes a change to the device’s iCloud account.

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
enum ChangeType
```

## Topics

### Account change types
- [CKSyncEngine.Event.AccountChange.ChangeType.signIn(currentUser:)](./changetype-swift.enum/signin%28currentuser%29.md)
  A change indicating a sign-in to an iCloud account.
- [CKSyncEngine.Event.AccountChange.ChangeType.signOut(previousUser:)](./changetype-swift.enum/signout%28previoususer%29.md)
  A change indicating a sign-out of an iCloud account.
- [CKSyncEngine.Event.AccountChange.ChangeType.switchAccounts(previousUser:currentUser:)](./changetype-swift.enum/switchaccounts%28previoususer,currentuser%29.md)
  A change indicating a switch between two iCloud accounts.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Understanding the change
- [let changeType: CKSyncEngine.Event.AccountChange.ChangeType](./changetype-swift.property.md)
  The iCloud account’s change type.
- [enum CKSyncEngineAccountChangeType](../../../cksyncengineaccountchangetype.md)
  Describes a change to the device’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange/changetype-swift.enum)*