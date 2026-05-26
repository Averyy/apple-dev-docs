# AudioComponentGetLastActiveTime(_:)

**Framework**: Audio Toolbox  
**Kind**: func

The time at which the application publishing the component was last active.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentGetLastActiveTime(_ comp: AudioComponent) -> CFAbsoluteTime
```

## See Also

- [func AudioOutputUnitPublish(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioUnit) -> OSStatus](audiooutputunitpublish(_:_:_:_:).md)
  Registers an audio output unit for use by other applications.
- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](audiooutputunitgethosticon(_:_:).md)
  The host app’s icon.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](audiocomponentgeticon(_:).md)
  The UIImage of the audio component’s icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentgetlastactivetime(_:))*