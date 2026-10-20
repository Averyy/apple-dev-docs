# CKSyncEngineAccountChangeType

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
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum CKSyncEngineAccountChangeType
```

```c
enum CKSyncEngineAccountChangeType : NSInteger;
```

## Topics

### Account change types
- [CKSyncEngineAccountChangeType.signIn](./cksyncengineaccountchangetype/signin.md)
  A change indicating a sign-in to an iCloud account.
- [CKSyncEngineAccountChangeType.signOut](./cksyncengineaccountchangetype/signout.md)
  A change indicating a sign-out of an iCloud account.
- [CKSyncEngineAccountChangeType.switchAccounts](./cksyncengineaccountchangetype/switchaccounts.md)
  A change indicating a switch between two iCloud accounts.
### Initializers
- [init?(rawValue: Int)](./cksyncengineaccountchangetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineaccountchangetype)*