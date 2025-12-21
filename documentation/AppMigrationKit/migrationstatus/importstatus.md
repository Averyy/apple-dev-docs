# importStatus

**Framework**: AppMigrationKit  
**Kind**: property

A property to indicate the status of import from another device into the app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static var importStatus: MigrationStatus? { get }
```

#### Discussion

This value is `nil` unless a migration completed.

You can use this value to show a notification about the completed migration to the person using the app.

## See Also

- [static func clearImportStatus()](migrationstatus/clearimportstatus.md)
  Sets the import status to a nil value to prevent further notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationstatus/importstatus)*