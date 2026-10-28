# clearImportStatus()

**Framework**: AppMigrationKit  
**Kind**: method  
**Role**: Type Method

Sets the import status to a nil value to prevent further notification.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func clearImportStatus()
```

## Discussion

Calling this method sets [`importStatus`](./importstatus.md) to `nil`, which indicates that the app has notified the person using the app of the migration’s completion, and doesn’t need further notifications.

## See Also

### Accessing the import status
- [static var importStatus: MigrationStatus?](./importstatus.md)
  A property to indicate the status of import from another device into the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationstatus/clearimportstatus())*