# AudioServicesDisposeSystemSoundID(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Disposes of a system sound object and associated resources.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioServicesDisposeSystemSoundID(_ inSystemSoundID: SystemSoundID) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `inSystemSoundID`: The system sound object to dispose of.

## See Also

- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](audioservicescreatesystemsoundid(_:_:).md)
  Creates a system sound object.
- [typealias SystemSoundID](systemsoundid.md)
  A system sound object, identified with a sound file you want to play.
- [System Sounds](1405222-system-sounds.md)
- [Alert Sound Identifiers](1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](audioservicesplayalertsound(_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesdisposesystemsoundid(_:))*