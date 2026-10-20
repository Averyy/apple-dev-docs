# CKSyncEngineAccountChangeType.signOut

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

A change indicating a sign-out of an iCloud account.

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
case signOut
```

```c
CKSyncEngineAccountChangeTypeSignOut
```

#### Discussion

You should delete any locally-stored data for the previous account.

## See Also

### Account change types
- [CKSyncEngineAccountChangeType.signIn](./signin.md)
  A change indicating a sign-in to an iCloud account.
- [CKSyncEngineAccountChangeType.switchAccounts](./switchaccounts.md)
  A change indicating a switch between two iCloud accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineaccountchangetype/signout)*