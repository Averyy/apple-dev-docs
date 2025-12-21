# AppMigrationTester

**Framework**: AppMigrationKit  
**Kind**: class

A test-only type your app uses to test app migration extensions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
actor AppMigrationTester
```

#### Overview

Use this type in unit tests that your containing app hosts. Calling the tester from your unit tests allows you to communicate with your app migration extension to valdiate your migration code.

In your tests, create an instance of `AppMigrationTester`, then access its [`exportController`](appmigrationtester/exportcontroller.md) and [`importController`](appmigrationtester/importcontroller.md) properties to exercise export and import functionality, respectively.

> ⚠️ **Warning**: Use `AppMigrationTester` only in unit tests, not in production code. The tester doesn’t operate in a production environment.

## Topics

### Creating a tester instance
- [init(platform: MigrationPlatform) async throws](appmigrationtester/init(platform:).md)
  Creates a tester instance for migrating to or from the specified platform.
### Testing export
- [var exportController: AppMigrationTester.AppExportController](appmigrationtester/exportcontroller.md)
  An instance of the controller object you use to test your export code.
- [AppMigrationTester.AppExportController](appmigrationtester/appexportcontroller.md)
  A class you use to test your extension’s export code.
### Testing import
- [var importController: AppMigrationTester.AppImportController](appmigrationtester/importcontroller.md)
  An instance of the controller object you use to test your import code.
- [AppMigrationTester.AppImportController](appmigrationtester/appimportcontroller.md)
  A class you use to test your extension’s import code.
### Supporting types
- [AppMigrationTester.DeviceToDeviceExportProperties](appmigrationtester/devicetodeviceexportproperties.md)
  Properties that describe the result of a device-to-device export.
- [AppMigrationTester.ResourcesExportResult](appmigrationtester/resourcesexportresult.md)
  The result of exporting resources to another device.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester)*