# AppMigrationTester.AppExportController

**Framework**: AppMigrationKit  
**Kind**: class  
**Role**: Class

A class you use to test your extension’s export code.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final class AppExportController
```

## Overview

Use the [`exportController`](./exportcontroller.md) property to obtain an instance of this class, then use its methods to call the export-related code of your app migration extension.

## Topics

### Testing resource export
- [func exportResources<SupportedOptions>(request: MigrationRequestWithOptions<SupportedOptions>?, progress: Progress?) async throws -> AppMigrationTester.ResourcesExportResult](./appexportcontroller/exportresources%28request,progress%29-15m4v.md)
  Tells the migration extension to begin exporting its resources, using options defined by the destination platform.
- [func exportResources(request: MigrationRequest?, progress: Progress?) async throws -> AppMigrationTester.ResourcesExportResult](./appexportcontroller/exportresources%28request,progress%29-5mw8u.md)
  Tells the migration extension to begin exporting its resources.
- [AppMigrationTester.ResourcesExportResult](./resourcesexportresult.md)
  The result of exporting resources to another device.
### Supporting types
- [struct MigrationRequestWithOptions](../migrationrequestwithoptions.md)
  An object that exposes properties of the migration request.
- [typealias MigrationRequest](../migrationrequest.md)
  A migration request that uses the default supported options.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Testing export
- [var exportController: AppMigrationTester.AppExportController](./exportcontroller.md)
  An instance of the controller object you use to test your export code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/appexportcontroller)*