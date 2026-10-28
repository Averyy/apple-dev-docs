# AudioOutputUnitGetHostIcon(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

The host app’s icon.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Inter-App Audio API is deprecated in favor of Audio Units

## Declaration

```swift
func AudioOutputUnitGetHostIcon(_ au: AudioUnit, _ desiredPointSize: Float) -> UIImage?
```

```c
extern UIImage *AudioOutputUnitGetHostIcon(AudioUnit au, float desiredPointSize);
```

## Discussion

The [`UIImage`](../UIKit/uiimage.md) of the host app’s icon.

## See Also

### Inter-App Audio
- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](./audiooutputunitpublish%28_,_,_,_%29.md)
  Registers an audio output unit for use by other applications.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](./audiocomponentgeticon%28_,_%29.md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](./audiocomponentgetlastactivetime%28_%29.md)
  The time at which the application publishing the component was last active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitgethosticon(_:_:))*