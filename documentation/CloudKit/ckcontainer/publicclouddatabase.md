# publicCloudDatabase

**Framework**: CloudKit  
**Kind**: property

The app’s public database.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var publicCloudDatabase: CKDatabase { get }
```

#### Discussion

This database is available regardless of whether the user’s device has an iCloud account. The contents of the public database are readable by all users of the app, and users have write access to the records, and other objects, they create. The public database’s contents are visible in the developer portal, where you can assign roles to users and restrict access as necessary.

Data in the public database counts toward your app’s iCloud storage quota.

## See Also

- [var privateCloudDatabase: CKDatabase](ckcontainer/privateclouddatabase.md)
  The user’s private database.
- [var sharedCloudDatabase: CKDatabase](ckcontainer/sharedclouddatabase.md)
  The database that contains shared data.
- [func database(with: CKDatabase.Scope) -> CKDatabase](ckcontainer/database(with:).md)
  Returns the database with the specified scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/publicclouddatabase)*