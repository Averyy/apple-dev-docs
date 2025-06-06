# CKSyncEngine.Event.AccountChange.ChangeType.switchAccounts(previousUser:currentUser:)

**Framework**: CloudKit  
**Kind**: case

A change indicating a switch between two iCloud accounts.

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
case switchAccounts(previousUser: CKRecord.ID, currentUser: CKRecord.ID)
```

#### Discussion

If the device changes iCloud accounts while your app isn’t running, [`CKSyncEngine`](cksyncengine-5sie5.md) notifies it about that change when the app next launches. Make sure to delete any locally stored data belonging to the `previousUser` account.

## See Also

- [CKSyncEngine.Event.AccountChange.ChangeType.signIn(currentUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signin(currentuser:).md)
  A change indicating a sign-in to an iCloud account.
- [CKSyncEngine.Event.AccountChange.ChangeType.signOut(previousUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signout(previoususer:).md)
  A change indicating a sign-out of an iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange/changetype-swift.enum/switchaccounts(previoususer:currentuser:))*