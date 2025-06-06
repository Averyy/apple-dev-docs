# ScreenSharingConnectionGroup

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a group of screen-sharing connections.

**Availability**:
- macOS 14.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ScreenSharingConnectionGroup
```

#### Discussion

Specify `com.apple.configuration.screensharing.connection.group` as the declaration type.

##### Configuration Availability

| Allowed in Device Enrollment | macOS |
| --- | --- |
| Allowed in User Enrollment | macOS |
| Allowed in Local Enrollment | macOS |
| Allowed in System Scope | macOS |
| Allowed in User Scope | macOS |

## See Also

- [object ScreenSharingConnectionDisplayConfigurationObject](screensharingconnectiondisplayconfigurationobject.md)
  The display configuration for this connection.
- [object ScreenSharingHostSettings](screensharinghostsettings.md)
  The declaration to configure screen-sharing host settings and restrictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensharingconnectiongroup)*