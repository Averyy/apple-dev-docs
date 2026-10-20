# MPVolumeSettingsAlertIsVisible()

**Framework**: Media Player  
**Kind**: func  
**Role**: Function

Returns a Boolean value indicating whether the volume alert panel is currently visible.

**Availability**:
- iOS 2.0+ - Deprecated in 11.3
- iPadOS 2.0+ - Deprecated in 11.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use MPVolumeView to present volume controls.

## Declaration

```swift
func MPVolumeSettingsAlertIsVisible() -> Bool
```

```c
extern BOOL MPVolumeSettingsAlertIsVisible();
```

#### Return Value

[`true`](../Swift/true.md) if the volume alert is visible; otherwise, [`false`](../Swift/false.md).

## See Also

### Global volume setting methods
- [func MPVolumeSettingsAlertShow()](./mpvolumesettingsalertshow%28%29.md)
  Displays an alert panel for controlling the system volume.
- [func MPVolumeSettingsAlertHide()](./mpvolumesettingsalerthide%28%29.md)
  Hides the alert panel that controls the system volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumesettingsalertisvisible())*