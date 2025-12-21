# ResourcesExporting

**Framework**: AppMigrationKit  
**Kind**: protocol

A protocol for exporting transportable resources in a streaming archive format when the destination platform doesn’t require special migration options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol ResourcesExporting : ResourcesExportingWithOptions where Self.OptionsType == MigrationDefaultSupportedOptions
```

#### Overview

This protocol extends [`ResourcesExportingWithOptions`](resourcesexportingwithoptions.md) and sets its [`OptionsType`](resourcesexportingwithoptions/optionstype.md) to [`MigrationDefaultSupportedOptions`](migrationdefaultsupportedoptions.md), which indicates the destination platform doesn’t require any special options. If you know your export to the other platform doesn’t need these options, conform to this protocol in your app exension and implement the methods and properties defined by [`ResourcesExportingWithOptions`](resourcesexportingwithoptions.md).

As with [`ResourcesExportingWithOptions`](resourcesexportingwithoptions.md), this protocol is only appropriate for transportable resources, those that you can copy as-is from the current file system to the destination device.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [AppMigrationExtension](appmigrationextension.md)
- [ResourcesExportingWithOptions](resourcesexportingwithoptions.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol ResourcesExportingWithOptions](resourcesexportingwithoptions.md)
  A protocol for exporting transportable resources in an archive format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesexporting)*