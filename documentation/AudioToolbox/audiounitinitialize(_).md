# AudioUnitInitialize(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Initializes an audio unit

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitInitialize(_ inUnit: AudioUnit) -> OSStatus
```

```c
extern OSStatus AudioUnitInitialize(AudioUnit inUnit);
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](./migrating-your-audio-unit-host-to-the-auv3-api.md)

## Return Value

A result code.

## Discussion

On successful initialization, the audio formats for input and output are valid and the audio unit is ready to render. During initialization, an audio unit allocates memory according to the maximum number of audio frames it can produce in response to a single render call.

Usually, the state of an audio unit (such as its I/O formats and memory allocations) cannot be changed while an audio unit is initialized.

## Parameters

- `inUnit`: The audio unit to initialize.

## See Also

### Initializing the Audio Unit
- [func AudioUnitUninitialize(AudioUnit) -> OSStatus](./audiounituninitialize%28_%29.md)
  Uninitializes an audio unit.
- [func AudioUnitProcess(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](./audiounitprocess%28_,_,_,_,_%29.md)
- [func AudioUnitProcessMultiple(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus](./audiounitprocessmultiple%28_,_,_,_,_,_,_,_%29.md)
- [func AudioUnitReset(AudioUnit, AudioUnitScope, AudioUnitElement) -> OSStatus](./audiounitreset%28_,_,_%29.md)
  Resets an audio unit’s render state.
- [typealias AudioUnit](./audiounit.md)
  The data type for a plug-in component that provides audio processing or audio data generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitinitialize(_:))*