# AudioConverterFillComplexBufferRealtimeSafe(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func AudioConverterFillComplexBufferRealtimeSafe(_ inAudioConverter: AudioConverterRef, _ inInputDataProc: AudioConverterComplexInputDataProcRealtimeSafe, _ inInputDataProcUserData: UnsafeMutableRawPointer?, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus
```

#### Discussion

Identical to AudioConverterFillComplexBuffer, with the addition of a realtime-safety guarantee.

Conversions involving only PCM formats – interleaving, deinterleaving, channel count changes, sample rate conversions – are realtime-safe. Such conversions may use this API in order to obtain compiler checks involving the `CA_REALTIME_API` attributes.

At runtime, this function returns `kAudioConverterErr_OperationNotSupported` if the conversion requires non-realtime-safe functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterfillcomplexbufferrealtimesafe(_:_:_:_:_:_:))*