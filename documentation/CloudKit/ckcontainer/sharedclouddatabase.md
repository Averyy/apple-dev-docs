# sharedCloudDatabase

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The database that contains shared data.

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
var sharedCloudDatabase: CKDatabase { get }
```

```objc
@property (nonatomic, strong, readonly) CKDatabase * sharedCloudDatabase;
```

## Discussion

This database is only available if the device has an iCloud account. Permissions on the database are available only to the user according to the permissions of the enclosing [`CKShare`](../ckshare.md) instance, which represents the shared record. The current user doesn’t own the content in the shared database, and can view and modify that content only if the necessary permissions exist. Data in the shared database isn’t visible in the developer portal or to any user who doesn’t have access.

Data in the shared database counts toward your app’s iCloud storage quota.

If there isn’t an iCloud account on the user’s device, this property still returns a database, but any attempt to use it results in an error. To determine if there is an iCloud account on the device, use the [`accountStatus(completionHandler:)`](./accountstatus%28completionhandler%29.md) method.

## See Also

### Getting the Public and Private Databases
- [var privateCloudDatabase: CKDatabase](./privateclouddatabase.md)
  The user’s private database.
- [var publicCloudDatabase: CKDatabase](./publicclouddatabase.md)
  The app’s public database.
- [func database(with: CKDatabase.Scope) -> CKDatabase](./database%28with%29.md)
  Returns the database with the specified scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/sharedclouddatabase)*