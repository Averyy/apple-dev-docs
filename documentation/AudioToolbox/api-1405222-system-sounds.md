# System Sounds

**Framework**: Audio Toolbox

## Topics

### Constants
- [var kSystemSoundID_FlashScreen: SystemSoundID](ksystemsoundid_flashscreen.md)
  On the desktop, use this constant with the [`AudioServicesPlayAlertSound(_:)`](audioservicesplayalertsound(_:).md) function to display a flash of light on the screen.
- [var kSystemSoundID_UserPreferredAlert: SystemSoundID](ksystemsoundid_userpreferredalert.md)
  On the desktop, use this constant with the [`AudioServicesPlayAlertSound(_:)`](audioservicesplayalertsound(_:).md) function to play the alert specified in the Sound preference pane.
- [var kUserPreferredAlert: SystemSoundID](kuserpreferredalert.md)
  A deprecated sound identifier.

## See Also

- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](audioservicescreatesystemsoundid(_:_:).md)
  Creates a system sound object.
- [func AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus](audioservicesdisposesystemsoundid(_:).md)
  Disposes of a system sound object and associated resources.
- [typealias SystemSoundID](systemsoundid.md)
  A system sound object, identified with a sound file you want to play.
- [Alert Sound Identifiers](1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](audioservicesplayalertsound(_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1405222-system-sounds)*