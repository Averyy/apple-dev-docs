# ResourcesArchiver

**Framework**: AppMigrationKit  
**Kind**: class

An object your app uses to archive resources during an export operation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final class ResourcesArchiver
```

#### Overview

> ❗ **Important**: This class handles task cancellation automatically by throwing cancellation errors up the stack if the migration system cancels the export. Don’t catch the cancellation errors; doing so causes the system to kill the app extension.

## Topics

### Appending resources
- [func appendItem(at: URL, pathInArchive: String?) async throws](resourcesarchiver/appenditem(at:pathinarchive:).md)
  Sends a file to the archiver for export.

## See Also

- [func exportResources(to: sending ResourcesArchiver, request: MigrationRequestWithOptions<Self.OptionsType>) async throws](resourcesexportingwithoptions/exportresources(to:request:).md)
  Exports resources from the app, in response to a request from the migration system.
- [struct MigrationRequestWithOptions](migrationrequestwithoptions.md)
  An object that exposes properties of the migration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesarchiver)*