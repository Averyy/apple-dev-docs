# SystemSoundID

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A system sound object, identified with a sound file you want to play.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias SystemSoundID = UInt32
```

```c
typedef UInt32 SystemSoundID;
```

#### Discussion

Call the [`AudioServicesCreateSystemSoundID(_:_:)`](./audioservicescreatesystemsoundid%28_,_%29.md) function to obtain a system sound object.

## See Also

### Creating and Disposing of System Sound Objects
- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](./audioservicescreatesystemsoundid%28_,_%29.md)
  Creates a system sound object.
- [func AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus](./audioservicesdisposesystemsoundid%28_%29.md)
  Disposes of a system sound object and associated resources.
- [System Sounds](./api-1405222-system-sounds.md)
- [Alert Sound Identifiers](./api-1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](./audioservicesplayalertsound%28_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/systemsoundid)*