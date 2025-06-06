# database(with:)

**Framework**: CloudKit  
**Kind**: method

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

## Parameters

- `databaseScope`: The database’s scope. See   for the available options.

## See Also

- [var privateCloudDatabase: CKDatabase](ckcontainer/privateclouddatabase.md)
  The user’s private database.
- [var publicCloudDatabase: CKDatabase](ckcontainer/publicclouddatabase.md)
  The app’s public database.
- [var sharedCloudDatabase: CKDatabase](ckcontainer/sharedclouddatabase.md)
  The database that contains shared data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/database(with:))*