# options

**Framework**: AppMigrationKit  
**Kind**: property

Export options requested by the destination device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
let options: [OptionsType : Data]
```

#### Discussion

The target operating system of the migration defines the options supported for a migration, if any. Refer to the target operating system documentation to determine the options it supports.

> 💡 **Tip**: The use of migration options is uncommon. If you don’t need migration options, use [`ResourcesExporting`](resourcesexporting.md), which uses the no-op [`MigrationDefaultSupportedOptions`](migrationdefaultsupportedoptions.md) type, rather than [`ResourcesExportingWithOptions`](resourcesexportingwithoptions.md).

## See Also

- [let destinationPlatform: MigrationPlatform](migrationrequestwithoptions/destinationplatform.md)
  The destination platform of the migration request.
- [struct MigrationPlatform](migrationplatform.md)
  A type that identifies the platform used by the other device in a migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationrequestwithoptions/options)*