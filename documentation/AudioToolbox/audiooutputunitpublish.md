# AudioOutputUnitPublish(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Registers an audio output unit for use by other applications.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioOutputUnitPublish(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString, _ inVersion: UInt32, _ inOutputUnit: AudioUnit) -> OSStatus
```

## See Also

- [func AudioOutputUnitGetHostIcon(AudioUnit, Float) -> UIImage?](audiooutputunitgethosticon(_:_:).md)
  The host app’s icon.
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](audiocomponentgeticon(_:).md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](audiocomponentgetlastactivetime(_:).md)
  The time at which the application publishing the component was last active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitpublish(_:_:_:_:))*