# exportResources(request:progress:)

**Framework**: AppMigrationKit  
**Kind**: method

Tells the migration extension to begin exporting its resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final func exportResources(request: MigrationRequest? = nil, progress: Progress? = nil) async throws -> AppMigrationTester.ResourcesExportResult
```

#### Return Value

The results of the export.

## Parameters

- `request`: An optional migration request instance to pass to the app extension’s export method. This value defaults to  .
- `progress`: An optional   object the extension uses to report its progress back to the unit test. This value defaults to  .

## See Also

- [func exportResources<SupportedOptions>(request: MigrationRequestWithOptions<SupportedOptions>?, progress: Progress?) async throws -> AppMigrationTester.ResourcesExportResult](appmigrationtester/appexportcontroller/exportresources(request:progress:)-15m4v.md)
  Tells the migration extension to begin exporting its resources, using options defined by the destination platform.
- [AppMigrationTester.ResourcesExportResult](appmigrationtester/resourcesexportresult.md)
  The result of exporting resources to another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/appexportcontroller/exportresources(request:progress:)-5mw8u)*