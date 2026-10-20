# MPVolumeSettingsAlertShow()

**Framework**: Media Player  
**Kind**: func  
**Role**: Function

Displays an alert panel for controlling the system volume.

**Availability**:
- iOS 2.0+ - Deprecated in 11.3
- iPadOS 2.0+ - Deprecated in 11.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use MPVolumeView to present volume controls.

## Declaration

```swift
func MPVolumeSettingsAlertShow()
```

```c
extern void MPVolumeSettingsAlertShow();
```

#### Discussion

The alert panel displayed by this function floats above the contents of the current window. It contains a slider for adjusting the system volume setting and a Done button so that the user can dismiss the panel. You can also dismiss the panel programmatically using the [`MPVolumeSettingsAlertHide()`](./mpvolumesettingsalerthide%28%29.md) function.

## See Also

### Global volume setting methods
- [func MPVolumeSettingsAlertHide()](./mpvolumesettingsalerthide%28%29.md)
  Hides the alert panel that controls the system volume.
- [func MPVolumeSettingsAlertIsVisible() -> Bool](./mpvolumesettingsalertisvisible%28%29.md)
  Returns a Boolean value indicating whether the volume alert panel is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumesettingsalertshow())*