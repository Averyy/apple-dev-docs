# AudioUnitProcessMultiple(_:_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitProcessMultiple(_ inUnit: AudioUnit, _ ioActionFlags: UnsafeMutablePointer<AudioUnitRenderActionFlags>?, _ inTimeStamp: UnsafePointer<AudioTimeStamp>, _ inNumberFrames: UInt32, _ inNumberInputBufferLists: UInt32, _ inInputBufferLists: UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, _ inNumberOutputBufferLists: UInt32, _ ioOutputBufferLists: UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus
```

## See Also

- [func AudioUnitInitialize(AudioUnit) -> OSStatus](audiounitinitialize(_:).md)
  Initializes an audio unit
- [func AudioUnitUninitialize(AudioUnit) -> OSStatus](audiounituninitialize(_:).md)
  Uninitializes an audio unit.
- [func AudioUnitProcess(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audiounitprocess(_:_:_:_:_:).md)
- [func AudioUnitReset(AudioUnit, AudioUnitScope, AudioUnitElement) -> OSStatus](audiounitreset(_:_:_:).md)
  Resets an audio unit’s render state.
- [typealias AudioUnit](audiounit.md)
  The data type for a plug-in component that provides audio processing or audio data generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitprocessmultiple(_:_:_:_:_:_:_:_:))*