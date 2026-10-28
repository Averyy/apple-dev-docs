# kUserPreferredAlert

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

A deprecated sound identifier.

**Availability**:
- macOS

## Declaration

```swift
var kUserPreferredAlert: SystemSoundID { get }
```

```c
kUserPreferredAlert
```

## Discussion

Use [`kSystemSoundID_UserPreferredAlert`](./ksystemsoundid_userpreferredalert.md) instead.

## See Also

### Constants
- [var kSystemSoundID_FlashScreen: SystemSoundID](./ksystemsoundid_flashscreen.md)
  On the desktop, use this constant with the [`AudioServicesPlayAlertSound(_:)`](./audioservicesplayalertsound%28_%29.md) function to display a flash of light on the screen.
- [var kSystemSoundID_UserPreferredAlert: SystemSoundID](./ksystemsoundid_userpreferredalert.md)
  On the desktop, use this constant with the [`AudioServicesPlayAlertSound(_:)`](./audioservicesplayalertsound%28_%29.md) function to play the alert specified in the Sound preference pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kuserpreferredalert)*