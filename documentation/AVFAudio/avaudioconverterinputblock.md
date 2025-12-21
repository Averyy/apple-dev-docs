# AVAudioConverterInputBlock

**Framework**: AVFAudio  
**Kind**: typealias

A block to get input data for conversion, as necessary.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias AVAudioConverterInputBlock = (AVAudioPacketCount, UnsafeMutablePointer<AVAudioConverterInputStatus>) -> AVAudioBuffer?
```

## See Also

- [func convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus](avaudioconverter/convert(to:error:withinputfrom:).md)
  Performs a conversion between audio formats, if the system supports it.
- [func convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](avaudioconverter/convert(to:from:).md)
  Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.
- [enum AVAudioConverterInputStatus](avaudioconverterinputstatus.md)
  An option that indicates the status of an audio converter input block.
- [enum AVAudioConverterOutputStatus](avaudioconverteroutputstatus.md)
  An option that indicates the return status of an audio converter method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterinputblock)*