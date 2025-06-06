# AudioCodecUninitialize(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Moves the codec from the initialized state back to the uninitialized state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecUninitialize(_ inCodec: AudioCodec) -> OSStatus
```

#### Return Value

Returns `NoErr` if successful, otherwise, a result code. See `Result Codes` for a list of possible values.

#### Discussion

This function returns the codec to the uninitialized state. The codec may then be configured freely. This function does not flush the input buffer or clear input and output formats, magic cookie data, and other state variables. It is not necessary to call this function before closing the codec.

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manger component instance, you can use the Component Manager (for example, the functions   and OpenAComponent) to obtain an audio codec object.

## See Also

- [func AudioCodecSetProperty(AudioCodec, AudioCodecPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiocodecsetproperty(_:_:_:_:).md)
  Sets the value of a codec property.
- [func AudioCodecInitialize(AudioCodec, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioStreamBasicDescription>?, UnsafeRawPointer?, UInt32) -> OSStatus](audiocodecinitialize(_:_:_:_:_:).md)
  Sets up the specified codec to perform a data format translation.
- [func AudioCodecReset(AudioCodec) -> OSStatus](audiocodecreset(_:).md)
  Flushes all the audio data in the codec and clears the input buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecuninitialize(_:))*