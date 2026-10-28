# currentUser

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The current iCloud account’s record identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) CKRecordID * currentUser;
```

## Discussion

If the user just signed in or switched accounts, this is the new user record ID. If the user signed out, this is `nil`.

## See Also

### Understanding the change
- [changeType](./changetype.md)
  The iCloud account’s change type.
- [enum CKSyncEngineAccountChangeType](../cksyncengineaccountchangetype.md)
  Describes a change to the device’s iCloud account.
- [previousUser](./previoususer.md)
  The previous iCloud account’s record identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineaccountchangeevent/currentuser)*