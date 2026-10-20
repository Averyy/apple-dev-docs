# ResourcesArchiver

**Framework**: AppMigrationKit  
**Kind**: class  
**Role**: Class

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
- [func appendItem(at: URL, pathInArchive: String?) async throws](./resourcesarchiver/appenditem%28at,pathinarchive%29.md)
  Sends a file to the archiver for export.

## See Also

### Exporting resources
- [func exportResources(to: sending ResourcesArchiver, request: MigrationRequestWithOptions<Self.OptionsType>) async throws](./resourcesexportingwithoptions/exportresources%28to,request%29.md)
  Exports resources from the app, in response to a request from the migration system.
- [struct MigrationRequestWithOptions](./migrationrequestwithoptions.md)
  An object that exposes properties of the migration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesarchiver)*