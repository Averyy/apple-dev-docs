# AudioCodecReset(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Flushes all the audio data in the codec and clears the input buffer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecReset(_ inCodec: AudioCodec) -> OSStatus
```

#### Return Value

Returns `NoErr` if successful, otherwise, a result code. See `Result Codes` for a list of possible values.

#### Discussion

The input and output formats, magic cookie data, and other state variables are retained so that you needn’t call the [`AudioCodecInitialize(_:_:_:_:_:)`](audiocodecinitialize(_:_:_:_:_:).md) function again unless the values of some variables have changed.

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manger component instance, you can use the Component Manager (for example, the functions   and OpenAComponent) to obtain an audio codec object.

## See Also

- [func AudioCodecInitialize(AudioCodec, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioStreamBasicDescription>?, UnsafeRawPointer?, UInt32) -> OSStatus](audiocodecinitialize(_:_:_:_:_:).md)
  Sets up the specified codec to perform a data format translation.
- [func AudioCodecUninitialize(AudioCodec) -> OSStatus](audiocodecuninitialize(_:).md)
  Moves the codec from the initialized state back to the uninitialized state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecreset(_:))*