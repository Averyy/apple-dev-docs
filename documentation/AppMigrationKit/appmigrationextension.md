# AppMigrationExtension

**Framework**: AppMigrationKit  
**Kind**: protocol

An app extension you extend to participate in data export and import.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol AppMigrationExtension : AppExtension, Sendable
```

#### Overview

During migration, the system calls your extension to collect and export its data to the receiving device. On import, the system calls your app extension just after app installation, but before the app is actually launchable.

The protocols specific to import and export operations extend this type, such as [`ResourcesExportingWithOptions`](resourcesexportingwithoptions.md) and [`ResourcesImporting`](resourcesimporting.md). For your app extension to successfully export or import data in response to a system call, it needs to conform to one or more of these child protocols.

## Topics

### Accessing migration data
- [var appContainer: MigrationDataContainer](appmigrationextension/appcontainer.md)
  The data container of the containing app.
- [struct MigrationDataContainer](migrationdatacontainer.md)
  An object describing an app’s data container

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [ResourcesExporting](resourcesexporting.md)
- [ResourcesExportingWithOptions](resourcesexportingwithoptions.md)
- [ResourcesImporting](resourcesimporting.md)

## See Also

- [com.apple.developer.app-migration.data-container-access](../BundleResources/Entitlements/com.apple.developer.app-migration.data-container-access.md)
  An entitlement required for app extensions to perform a one-time transfer of on-device data to or from another platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationextension)*