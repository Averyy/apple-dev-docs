# sharedCloudDatabase

**Framework**: CloudKit JS  
**Kind**: property

The database containing shared records accepted by the current user.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute CloudKit.Database sharedCloudDatabase;
```

#### Discussion

The shared database allows the current user (a participant) to access records shared by other users (owners). Shared records are stored in the owner’s container and count towards the owner’s iCloud account storage quota.

## See Also

- [publicCloudDatabase](cloudkit.container/publicclouddatabase.md)
  The database containing the data shared by all users.
- [privateCloudDatabase](cloudkit.container/privateclouddatabase.md)
  The database containing the user’s private data.
- [getDatabaseWithDatabaseScope](cloudkit.container/getdatabasewithdatabasescope.md)
  Returns the specified (public, private, or shared) database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/sharedclouddatabase)*