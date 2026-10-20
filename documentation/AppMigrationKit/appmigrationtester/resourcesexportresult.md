# AppMigrationTester.ResourcesExportResult

**Framework**: AppMigrationKit  
**Kind**: struct  
**Role**: Structure

The result of exporting resources to another device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct ResourcesExportResult
```

## Topics

### Inspecting result properties
- [let extractedResourcesURL: URL](./resourcesexportresult/extractedresourcesurl.md)
  A URL that refers to the directory containing the the exported resources.
- [let exportProperties: AppMigrationTester.DeviceToDeviceExportProperties](./resourcesexportresult/exportproperties.md)
  Properties of the device-to-device export.
- [AppMigrationTester.DeviceToDeviceExportProperties](./devicetodeviceexportproperties.md)
  Properties that describe the result of a device-to-device export.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [AppMigrationTester.DeviceToDeviceExportProperties](./devicetodeviceexportproperties.md)
  Properties that describe the result of a device-to-device export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/resourcesexportresult)*