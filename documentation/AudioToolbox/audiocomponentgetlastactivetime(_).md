# AudioComponentGetLastActiveTime(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

The time at which the application publishing the component was last active.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Inter-App Audio API is deprecated in favor of Audio Units

## Declaration

```swift
func AudioComponentGetLastActiveTime(_ comp: AudioComponent) -> CFAbsoluteTime
```

```c
extern CFAbsoluteTime AudioComponentGetLastActiveTime(AudioComponent comp);
```

## See Also

### Inter-App Audio
- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](./audiooutputunitpublish%28_,_,_,_%29.md)
  Registers an audio output unit for use by other applications.
- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](./audiooutputunitgethosticon%28_,_%29.md)
  The host app’s icon.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](./audiocomponentgeticon%28_,_%29.md)
  The UIImage of the audio component’s icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentgetlastactivetime(_:))*