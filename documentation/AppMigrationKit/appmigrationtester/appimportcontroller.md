# AppMigrationTester.AppImportController

**Framework**: AppMigrationKit  
**Kind**: class  
**Role**: Class

A class you use to test your extension’s import code.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final class AppImportController
```

#### Overview

Use the [`importController`](./importcontroller.md) property to obtain an instance of this class, then use its methods to call the import-related code of your app migration extension.

## Topics

### Testing resource import
- [func importResources(from: URL, importRequest: ResourcesImportRequest?, progress: Progress?) async throws](./appimportcontroller/importresources%28from,importrequest,progress%29.md)
  Tells the migration extension to begin importing transportable resources into the app extension.
### Completing an import
- [func registerImportCompletion(with: MigrationStatus) async throws](./appimportcontroller/registerimportcompletion%28with%29.md)
  Tells your app that import completed with a given status.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Testing import
- [var importController: AppMigrationTester.AppImportController](./importcontroller.md)
  An instance of the controller object you use to test your import code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/appimportcontroller)*