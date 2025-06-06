# CKSyncEngine.Event.AccountChange.ChangeType.signIn(currentUser:)

**Framework**: CloudKit  
**Kind**: case

A change indicating a sign-in to an iCloud account.

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
case signIn(currentUser: CKRecord.ID)
```

#### Discussion

If your app has locally stored data when [`CKSyncEngine`](cksyncengine-5sie5.md) notifies it about the device signing in to an iCloud account, perform one of the following actions:

- Keep the local data separate from any remote data
- Merge the local data with the account’s remote data
- Delete the local data
- Prompt the account’s owner to make the decision

## See Also

- [CKSyncEngine.Event.AccountChange.ChangeType.signOut(previousUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signout(previoususer:).md)
  A change indicating a sign-out of an iCloud account.
- [CKSyncEngine.Event.AccountChange.ChangeType.switchAccounts(previousUser:currentUser:)](cksyncengine-5sie5/event/accountchange/changetype-swift.enum/switchaccounts(previoususer:currentuser:).md)
  A change indicating a switch between two iCloud accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/accountchange/changetype-swift.enum/signin(currentuser:))*