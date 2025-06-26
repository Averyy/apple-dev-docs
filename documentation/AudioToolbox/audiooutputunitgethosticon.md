# AudioOutputUnitGetHostIcon(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

The host app’s icon.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioOutputUnitGetHostIcon(_ au: AudioUnit, _ desiredPointSize: Float) -> UIImage?
```

#### Discussion

The [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) of the host app’s icon.

## See Also

- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](audiooutputunitpublish(_:_:_:_:).md)
  Registers an audio output unit for use by other applications.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](audiocomponentgeticon(_:).md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](audiocomponentgetlastactivetime(_:).md)
  The time at which the application publishing the component was last active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitgethosticon(_:_:))*