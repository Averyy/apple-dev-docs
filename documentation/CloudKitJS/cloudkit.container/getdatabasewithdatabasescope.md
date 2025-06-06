# getDatabaseWithDatabaseScope

**Framework**: CloudKit JS  
**Kind**: method

Returns the specified (public, private, or shared) database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
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

- [publicCloudDatabase](cloudkit.container/publicclouddatabase.md)
  The database containing the data shared by all users.
- [privateCloudDatabase](cloudkit.container/privateclouddatabase.md)
  The database containing the user’s private data.
- [sharedCloudDatabase](cloudkit.container/sharedclouddatabase.md)
  The database containing shared records accepted by the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/getdatabasewithdatabasescope)*