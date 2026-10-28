# AudioServicesDisposeSystemSoundID(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioServicesDisposeSystemSoundID(SystemSoundID inSystemSoundID);
```

## Return Value

A result code.

## Parameters

- `inSystemSoundID`: The system sound object to dispose of.

## See Also

### Creating and Disposing of System Sound Objects
- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](./audioservicescreatesystemsoundid%28_,_%29.md)
  Creates a system sound object.
- [typealias SystemSoundID](./systemsoundid.md)
  A system sound object, identified with a sound file you want to play.
- [System Sounds](./api-1405222-system-sounds.md)
- [Alert Sound Identifiers](./api-1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](./audioservicesplayalertsound%28_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesdisposesystemsoundid(_:))*