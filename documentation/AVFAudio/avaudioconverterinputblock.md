# AVAudioConverterInputBlock

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A block to get input data for conversion, as necessary.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias AVAudioConverterInputBlock = (AVAudioPacketCount, UnsafeMutablePointer<AVAudioConverterInputStatus>) -> AVAudioBuffer?
```

```c
typedef AVAudioBuffer *(^)(unsigned int, enum AVAudioConverterInputStatus *) AVAudioConverterInputBlock;
```

## See Also

### Converting audio formats
- [func convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: (AVAudioPacketCount, UnsafeMutablePointer<AVAudioConverterInputStatus>) -> AVAudioBuffer?) -> AVAudioConverterOutputStatus](./avaudioconverter/convert%28to,error,withinputfrom%29.md)
  Performs a conversion between audio formats, if the system supports it.
- [func convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](./avaudioconverter/convert%28to,from%29.md)
  Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.
- [enum AVAudioConverterInputStatus](./avaudioconverterinputstatus.md)
  An option that indicates the status of an audio converter input block.
- [enum AVAudioConverterOutputStatus](./avaudioconverteroutputstatus.md)
  An option that indicates the return status of an audio converter method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterinputblock)*