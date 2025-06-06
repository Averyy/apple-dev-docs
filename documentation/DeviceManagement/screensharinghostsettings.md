# ScreenSharingHostSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure screen-sharing host settings and restrictions.

**Availability**:
- macOS 14.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ScreenSharingHostSettings
```

#### Discussion

Specify `com.apple.configuration.screensharing.host.settings` as the declaration type.

##### Configuration Availability

| Allowed in Device Enrollment | macOS |
| --- | --- |
| Allowed in User Enrollment | - |
| Allowed in Local Enrollment | macOS |
| Allowed in System Scope | macOS |
| Allowed in User Scope | - |

## See Also

- [object ScreenSharingConnectionDisplayConfigurationObject](screensharingconnectiondisplayconfigurationobject.md)
  The display configuration for this connection.
- [object ScreenSharingConnectionGroup](screensharingconnectiongroup.md)
  The declaration to configure a group of screen-sharing connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensharinghostsettings)*