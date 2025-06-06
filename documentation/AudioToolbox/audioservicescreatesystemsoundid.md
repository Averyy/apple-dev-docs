# AudioServicesCreateSystemSoundID(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a system sound object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioServicesCreateSystemSoundID(_ inFileURL: CFURL, _ outSystemSoundID: UnsafeMutablePointer<SystemSoundID>) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `inFileURL`: The URL of the audio file to play.
- `outSystemSoundID`: On output, a system sound object associated with the specified audio file.

## See Also

- [func AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus](audioservicesdisposesystemsoundid(_:).md)
  Disposes of a system sound object and associated resources.
- [typealias SystemSoundID](systemsoundid.md)
  A system sound object, identified with a sound file you want to play.
- [System Sounds](1405222-system-sounds.md)
- [Alert Sound Identifiers](1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](audioservicesplayalertsound(_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicescreatesystemsoundid(_:_:))*