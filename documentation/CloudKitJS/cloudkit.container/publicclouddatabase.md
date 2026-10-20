# publicCloudDatabase

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

The database containing the data shared by all users.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute CloudKit.Database publicCloudDatabase;
```

## See Also

### Getting the Public and Private Databases
- [privateCloudDatabase](./privateclouddatabase.md)
  The database containing the user’s private data.
- [sharedCloudDatabase](./sharedclouddatabase.md)
  The database containing shared records accepted by the current user.
- [getDatabaseWithDatabaseScope](./getdatabasewithdatabasescope.md)
  Returns the specified (public, private, or shared) database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/publicclouddatabase)*