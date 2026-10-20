# ScreenSharingConnectionDisplayConfigurationObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The display configuration for this connection.

**Availability**:
- macOS 14.0+

## Declaration

```
object ScreenSharingConnectionDisplayConfigurationObject
```

## Properties

- `DisplayType` (string) *(required)*: The type of display for the connection, which has these allowed values:

  - `Virtual1`: Create one virtual display.
  - `Virtual2`: Create two virtual displays.

  **Allowed Values**: `Virtual1`, `Virtual2`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/screensharingconnectiondisplayconfigurationobject)*