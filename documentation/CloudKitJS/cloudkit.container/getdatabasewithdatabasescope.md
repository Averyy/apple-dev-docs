# getDatabaseWithDatabaseScope

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Returns the specified (public, private, or shared) database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
CloudKit.Database getDatabaseWithDatabaseScope(
	CloudKit.DatabaseScope databaseScope
);
```

#### Return Value

The specified database.

#### Discussion

This is a convenience method that you can use instead of the specific properties.

## Parameters

- `databaseScope`: Specifies the type of database to return.

## See Also

### Getting the Public and Private Databases
- [publicCloudDatabase](./publicclouddatabase.md)
  The database containing the data shared by all users.
- [privateCloudDatabase](./privateclouddatabase.md)
  The database containing the user’s private data.
- [sharedCloudDatabase](./sharedclouddatabase.md)
  The database containing shared records accepted by the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/getdatabasewithdatabasescope)*