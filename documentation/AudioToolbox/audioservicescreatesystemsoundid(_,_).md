# AudioServicesCreateSystemSoundID(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus AudioServicesCreateSystemSoundID(CFURLRef inFileURL, SystemSoundID *outSystemSoundID);
```

#### Return Value

A result code.

## Parameters

- `inFileURL`: The URL of the audio file to play.
- `outSystemSoundID`: On output, a system sound object associated with the specified audio file.

## See Also

### Creating and Disposing of System Sound Objects
- [func AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus](./audioservicesdisposesystemsoundid%28_%29.md)
  Disposes of a system sound object and associated resources.
- [typealias SystemSoundID](./systemsoundid.md)
  A system sound object, identified with a sound file you want to play.
- [System Sounds](./api-1405222-system-sounds.md)
- [Alert Sound Identifiers](./api-1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](./audioservicesplayalertsound%28_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicescreatesystemsoundid(_:_:))*