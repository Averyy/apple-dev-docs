# convert(to:from:)

**Framework**: AVFAudio  
**Kind**: method

Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func convert(to outputBuffer: AVAudioPCMBuffer, from inputBuffer: AVAudioPCMBuffer) throws
```

#### Discussion

The output buffer’s [`frameCapacity`](avaudiopcmbuffer/framecapacity.md) value needs to be at least at large as the [`frameLength`](avaudiopcmbuffer/framelength.md) value of the `inputBuffer`.

## Parameters

- `outputBuffer`: The output audio buffer.
- `inputBuffer`: The input audio buffer.

## See Also

- [func convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus](avaudioconverter/convert(to:error:withinputfrom:).md)
  Performs a conversion between audio formats, if the system supports it.
- [typealias AVAudioConverterInputBlock](avaudioconverterinputblock.md)
  A block to get input data for conversion, as necessary.
- [enum AVAudioConverterInputStatus](avaudioconverterinputstatus.md)
  An option that indicates the status of an audio converter input block.
- [enum AVAudioConverterOutputStatus](avaudioconverteroutputstatus.md)
  An option that indicates the return status of an audio converter method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/convert(to:from:))*