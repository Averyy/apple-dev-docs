# AudioUnitReset(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Resets an audio unit’s render state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitReset(_ inUnit: AudioUnit, _ inScope: AudioUnitScope, _ inElement: AudioUnitElement) -> OSStatus
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Return Value

A result code.

#### Discussion

This function resets the render state of an audio unit. For example, with a delay or reverb type of audio unit, it clears all of the delay lines maintained within the audio unit. Typically, you call this function when an audio unit was previously rendering and was taken out of the render chain (for example, if the track it is in gets muted) and is now being added back in (for example, unmuted). Your application should reset the audio unit before adding it back to the render chain so that it does not produce audio from its delay lines that is no longer valid.

This function clears memory. It does not allocate or free memory resources.

## Parameters

- `inUnit`: The audio unit whose render state you are resetting.
- `inScope`: The audio unit scope, typically set to  .
- `inElement`: The audio unit element, typically set to  .

## See Also

- [func AudioUnitInitialize(AudioUnit) -> OSStatus](audiounitinitialize(_:).md)
  Initializes an audio unit
- [func AudioUnitUninitialize(AudioUnit) -> OSStatus](audiounituninitialize(_:).md)
  Uninitializes an audio unit.
- [func AudioUnitProcess(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audiounitprocess(_:_:_:_:_:).md)
- [func AudioUnitProcessMultiple(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus](audiounitprocessmultiple(_:_:_:_:_:_:_:_:).md)
- [typealias AudioUnit](audiounit.md)
  The data type for a plug-in component that provides audio processing or audio data generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitreset(_:_:_:))*