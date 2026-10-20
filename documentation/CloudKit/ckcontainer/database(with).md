# database(with:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Returns the database with the specified scope.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func database(with databaseScope: CKDatabase.Scope) -> CKDatabase
```

```objc
- (CKDatabase *) databaseWithDatabaseScope:(CKDatabaseScope) databaseScope;
```

## Parameters

- `databaseScope`: The database’s scope. See [`CKDatabase.Scope`](../ckdatabase/scope.md) for the available options.

## See Also

### Getting the Public and Private Databases
- [var privateCloudDatabase: CKDatabase](./privateclouddatabase.md)
  The user’s private database.
- [var publicCloudDatabase: CKDatabase](./publicclouddatabase.md)
  The app’s public database.
- [var sharedCloudDatabase: CKDatabase](./sharedclouddatabase.md)
  The database that contains shared data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/database(with:))*