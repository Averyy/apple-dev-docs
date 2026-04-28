# ServicesBackgroundTasksLaunchdItemObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of launchd configurations.

**Availability**:
- macOS 15.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ServicesBackgroundTasksLaunchdItemObject
```

## Properties

- `Context` (string) *(required)*: Indicates whether the launchd configuration file is applied to the system daemon, or system agent domain.
- `FileAssetReference` (string) *(required)*: Specifies the identifier of an asset declaration containing a reference to the launchd configuration file for the background task. The referenced data must be a property list file conforming to the launchd.plist format. The asset’s “ContentType” and “Hash-SHA-256” keys in the “Reference” key are required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/servicesbackgroundtaskslaunchditemobject)*