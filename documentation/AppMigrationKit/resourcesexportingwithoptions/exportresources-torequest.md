# exportResources(to:request:)

**Framework**: AppMigrationKit  
**Kind**: method  
**Required**: Yes

Exports resources from the app, in response to a request from the migration system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func exportResources(to archiver: sending ResourcesArchiver, request: MigrationRequestWithOptions<Self.OptionsType>) async throws
```

#### Discussion

Implement this method in your app extension to export files from your app to the destination device.

## Parameters

- `archiver`: An archiver to receive files from your app. Call   with each item to export.
- `request`: A request object that describes the destination of the migration.

## See Also

- [class ResourcesArchiver](resourcesarchiver.md)
  An object your app uses to archive resources during an export operation.
- [struct MigrationRequestWithOptions](migrationrequestwithoptions.md)
  An object that exposes properties of the migration request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions/exportresources(to:request:))*