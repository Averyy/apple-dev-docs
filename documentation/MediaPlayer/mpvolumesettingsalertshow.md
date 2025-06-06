# MPVolumeSettingsAlertShow()

**Framework**: Media Player  
**Kind**: func

Displays an alert panel for controlling the system volume.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func MPVolumeSettingsAlertShow()
```

#### Discussion

The alert panel displayed by this function floats above the contents of the current window. It contains a slider for adjusting the system volume setting and a Done button so that the user can dismiss the panel. You can also dismiss the panel programmatically using the [`MPVolumeSettingsAlertHide()`](mpvolumesettingsalerthide().md) function.

## See Also

- [func MPVolumeSettingsAlertHide()](mpvolumesettingsalerthide().md)
  Hides the alert panel that controls the system volume.
- [func MPVolumeSettingsAlertIsVisible() -> Bool](mpvolumesettingsalertisvisible().md)
  Returns a Boolean value indicating whether the volume alert panel is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumesettingsalertshow())*