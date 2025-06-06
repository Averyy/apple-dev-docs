# AudioUnit

**Framework**: Audio Toolbox  
**Kind**: typealias

The data type for a plug-in component that provides audio processing or audio data generation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioUnit = AudioComponentInstance
```

#### Discussion

The various types of audio units are described in the [`Audio Unit Types`](1584142-audio_unit_types.md) enumeration. The subtypes of audio units provided by Apple are described in [`Converter Audio Unit Subtypes`](1584145-converter_audio_unit_subtypes.md), [`Effect Audio Unit Subtypes`](1584154-effect_audio_unit_subtypes.md), [`Mixer Audio Unit Subtypes`](1584150-mixer_audio_unit_subtypes.md), and [`Input/Output Audio Unit Subtypes`](1584139-input_output_audio_unit_subtypes.md).

## See Also

- [func AudioUnitInitialize(AudioUnit) -> OSStatus](audiounitinitialize(_:).md)
  Initializes an audio unit
- [func AudioUnitUninitialize(AudioUnit) -> OSStatus](audiounituninitialize(_:).md)
  Uninitializes an audio unit.
- [func AudioUnitProcess(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audiounitprocess(_:_:_:_:_:).md)
- [func AudioUnitProcessMultiple(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<UnsafePointer<AudioBufferList>>, UInt32, UnsafeMutablePointer<UnsafeMutablePointer<AudioBufferList>>) -> OSStatus](audiounitprocessmultiple(_:_:_:_:_:_:_:_:).md)
- [func AudioUnitReset(AudioUnit, AudioUnitScope, AudioUnitElement) -> OSStatus](audiounitreset(_:_:_:).md)
  Resets an audio unit’s render state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounit)*