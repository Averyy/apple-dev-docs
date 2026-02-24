# CKSyncEngineAccountChangeType.signIn

**Framework**: CloudKit  
**Kind**: case

A change indicating a sign-in to an iCloud account.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case signIn
```

#### Discussion

If your app has locally-stored data when [`CKSyncEngine`](cksyncengine-4b4w9.md) notifies it about the device signing in to an iCloud account, perform one of the following actions:

- Keep the local data separate from any remote data
- Merge the local data with the account’s remote data
- Delete the local data
- Prompt the account’s owner to make the decision

## See Also

- [CKSyncEngineAccountChangeType.signOut](cksyncengineaccountchangetype/signout.md)
  A change indicating a sign-out of an iCloud account.
- [CKSyncEngineAccountChangeType.switchAccounts](cksyncengineaccountchangetype/switchaccounts.md)
  A change indicating a switch between two iCloud accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineaccountchangetype/signin)*