# SystemSoundID

**Framework**: Audio Toolbox  
**Kind**: typealias

A system sound object, identified with a sound file you want to play.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias SystemSoundID = UInt32
```

#### Discussion

Call the [`AudioServicesCreateSystemSoundID(_:_:)`](audioservicescreatesystemsoundid(_:_:).md) function to obtain a system sound object.

## See Also

- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](audioservicescreatesystemsoundid(_:_:).md)
  Creates a system sound object.
- [func AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus](audioservicesdisposesystemsoundid(_:).md)
  Disposes of a system sound object and associated resources.
- [System Sounds](1405222-system-sounds.md)
- [Alert Sound Identifiers](1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](audioservicesplayalertsound(_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/systemsoundid)*