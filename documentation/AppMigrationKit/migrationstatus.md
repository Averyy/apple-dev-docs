# MigrationStatus

**Framework**: AppMigrationKit  
**Kind**: enum

A type the containing app uses to determine the status of a completed import.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum MigrationStatus
```

#### Overview

After the first time the app launches, check this type’s static variable [`importStatus`](migrationstatus/importstatus.md) to determine whether a migration took place and, if so, whether it succeeded. To determine the status, check to see if `importStatus` is non-`nil` and that its value is [`MigrationStatus.success`](migrationstatus/success.md). After a successful migration, notify the person using the app that migration succeeded, and call the static method [`clearImportStatus()`](migrationstatus/clearimportstatus().md).

## Topics

### Accessing the import status
- [static var importStatus: MigrationStatus?](migrationstatus/importstatus.md)
  A property to indicate the status of import from another device into the app.
- [static func clearImportStatus()](migrationstatus/clearimportstatus.md)
  Sets the import status to a nil value to prevent further notification.
### Examining migration statuses
- [MigrationStatus.success](migrationstatus/success.md)
  The migration completed successfully.
- [MigrationStatus.failure(_:)](migrationstatus/failure(_:).md)
  The migration failed with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationstatus)*