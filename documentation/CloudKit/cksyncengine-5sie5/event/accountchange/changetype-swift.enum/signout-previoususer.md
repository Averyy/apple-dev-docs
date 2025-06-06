# CKSyncEngine.Event.AccountChange.ChangeType.signOut(previousUser:)

**Framework**: CloudKit  
**Kind**: case

A change indicating a sign-out of an iCloud account.

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
case signOut(previousUser: CKRecord.ID)
```

#### Discussion

After the device signs out of the iCloud account, delete any locally stored data that belongs to that account.

## See Also

- [CKSyncEngine.Event.AccountChange.ChangeType.signIn(currentUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signin(currentuser:).md)
  A change indicating a sign-in to an iCloud account.
- [CKSyncEngine.Event.AccountChange.ChangeType.switchAccounts(previousUser:currentUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/switchaccounts(previoususer:currentuser:).md)
  A change indicating a switch between two iCloud accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signout(previoususer:))*