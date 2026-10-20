# exportResources(request:progress:)

**Framework**: AppMigrationKit  
**Kind**: method  
**Role**: Instance Method

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

- `request`: An optional migration request instance to pass to the app extension’s export method. This value defaults to `nil`.
- `progress`: An optional [`Progress`](../../../Foundation/progress.md) object the extension uses to report its progress back to the unit test. This value defaults to `nil`.

## See Also

### Testing resource export
- [func exportResources<SupportedOptions>(request: MigrationRequestWithOptions<SupportedOptions>?, progress: Progress?) async throws -> AppMigrationTester.ResourcesExportResult](./exportresources%28request,progress%29-15m4v.md)
  Tells the migration extension to begin exporting its resources, using options defined by the destination platform.
- [AppMigrationTester.ResourcesExportResult](../resourcesexportresult.md)
  The result of exporting resources to another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/appexportcontroller/exportresources(request:progress:)-5mw8u)*