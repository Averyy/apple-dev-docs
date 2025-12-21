# MigrationDataContainer

**Framework**: AppMigrationKit  
**Kind**: struct

An object describing an app’s data container

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct MigrationDataContainer
```

## Topics

### Identifying the app
- [let bundleIdentifier: String](migrationdatacontainer/bundleidentifier.md)
  The app’s bundle identifier.
### Accessing app directories
- [let containerRootDirectory: URL](migrationdatacontainer/containerrootdirectory.md)
  The root container directory of the app.
- [var applicationSupportDirectory: URL](migrationdatacontainer/applicationsupportdirectory.md)
  The application support directory within the container.
- [var documentsDirectory: URL](migrationdatacontainer/documentsdirectory.md)
  The documents directory within the app container.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var appContainer: MigrationDataContainer](appmigrationextension/appcontainer.md)
  The data container of the containing app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationdatacontainer)*