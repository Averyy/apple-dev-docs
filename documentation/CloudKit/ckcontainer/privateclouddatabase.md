# privateCloudDatabase

**Framework**: CloudKit  
**Kind**: property

The user’s private database.

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
var privateCloudDatabase: CKDatabase { get }
```

#### Discussion

The user’s private database is only available if the device has an iCloud account. Only the user can access their private database, by default. They own all of the database’s content and can view and modify that content. Data in the private database isn’t visible in the developer portal.

Data in the private database counts toward the user’s iCloud storage quota.

If there isn’t an iCloud account on the user’s device, this property still returns a database, but any attempt to use it results in an error. To determine if there is an iCloud account on the device, use the [`accountStatus(completionHandler:)`](ckcontainer/accountstatus(completionhandler:).md) method.

## See Also

- [var publicCloudDatabase: CKDatabase](ckcontainer/publicclouddatabase.md)
  The app’s public database.
- [var sharedCloudDatabase: CKDatabase](ckcontainer/sharedclouddatabase.md)
  The database that contains shared data.
- [func database(with: CKDatabase.Scope) -> CKDatabase](ckcontainer/database(with:).md)
  Returns the database with the specified scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/privateclouddatabase)*