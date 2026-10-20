# AppMigrationTester.DeviceToDeviceExportProperties

**Framework**: AppMigrationKit  
**Kind**: struct  
**Role**: Structure

Properties that describe the result of a device-to-device export.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct DeviceToDeviceExportProperties
```

## Topics

### Inspecting data size properties
- [let uncompressedBytes: Int](./devicetodeviceexportproperties/uncompressedbytes.md)
  The number of uncompressed bytes written to the exporter.
- [let compressedBytes: Int?](./devicetodeviceexportproperties/compressedbytes.md)
  The number of compressed bytes written to the migration infrastructure, if the extension uses compression.
- [let sizeEstimate: Int](./devicetodeviceexportproperties/sizeestimate.md)
  The size estimate provided by the app extension.
### Inspecting metadata properties
- [let version: String](./devicetodeviceexportproperties/version.md)
  The data version provided by the app extension.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [AppMigrationTester.ResourcesExportResult](./resourcesexportresult.md)
  The result of exporting resources to another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/devicetodeviceexportproperties)*