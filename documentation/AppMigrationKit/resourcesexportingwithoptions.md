# ResourcesExportingWithOptions

**Framework**: AppMigrationKit  
**Kind**: protocol

A protocol for exporting transportable resources in an archive format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
protocol ResourcesExportingWithOptions : AppMigrationExtension
```

#### Overview

Conform to this protocol in your app extension to export transportable resources: files on disk that can you can copy as-is to the destination device without converting to an intermediate transport format.

Only use this approach when your app’s files require no changes before exporting. If you convert files locally to an intermediate transport format, export might fail if there’s not enough free space on the file system.

During export, the system prevents launching your app and any of its extensions. This ensures the migration system has exclusive access to the app contents. The export process may also archive, compress, or de-duplicate the files during transport.

Make continuous progress while exporting by repeatedly calling the archiver’s [`appendItem(at:pathInArchive:)`](resourcesarchiver/appenditem(at:pathinarchive:).md) method as each resource is ready. If the framework determines that your extension is hung, it may terminate the extension without migrating the app’s data to the destination.

## Topics

### Exporting resources
- [func exportResources(to: sending ResourcesArchiver, request: MigrationRequestWithOptions<Self.OptionsType>) async throws](resourcesexportingwithoptions/exportresources(to:request:).md)
  Exports resources from the app, in response to a request from the migration system.
- [class ResourcesArchiver](resourcesarchiver.md)
  An object your app uses to archive resources during an export operation.
- [struct MigrationRequestWithOptions](migrationrequestwithoptions.md)
  An object that exposes properties of the migration request.
### Declaring resource properties
- [var resourcesSizeEstimate: Int](resourcesexportingwithoptions/resourcessizeestimate.md)
  The estimated size of all resources to export, in bytes.
- [var resourcesVersion: String](resourcesexportingwithoptions/resourcesversion.md)
  A property that identifies the version of the format the export uses.
- [var resourcesCompressible: Bool](resourcesexportingwithoptions/resourcescompressible.md)
  A property that indicates whether the archiver attempts to compress the resources passed to it.
### Declaring export options
- [associatedtype OptionsType : CaseIterable, Hashable, RawRepresentable, Sendable](resourcesexportingwithoptions/optionstype.md)
  A type that indicates the options supported by the destination device.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [AppMigrationExtension](appmigrationextension.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [ResourcesExporting](resourcesexporting.md)

## See Also

- [protocol ResourcesExporting](resourcesexporting.md)
  A protocol for exporting transportable resources in a streaming archive format when the destination platform doesn’t require special migration options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions)*