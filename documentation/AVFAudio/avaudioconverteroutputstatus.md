# AVAudioConverterOutputStatus

**Framework**: AVFAudio  
**Kind**: enum

An option that indicates the return status of an audio converter method.

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
enum AVAudioConverterOutputStatus
```

## Topics

### Status Options
- [AVAudioConverterOutputStatus.haveData](avaudioconverteroutputstatus/havedata.md)
  A status that indicates that the method returns all of the requested data.
- [AVAudioConverterOutputStatus.inputRanDry](avaudioconverteroutputstatus/inputrandry.md)
  A status that indicates the method doesn’t have enough input available to satisfy the request.
- [AVAudioConverterOutputStatus.endOfStream](avaudioconverteroutputstatus/endofstream.md)
  A status that indicates the method reaches the end of the stream, and doesn’t return any data.
- [AVAudioConverterOutputStatus.error](avaudioconverteroutputstatus/error.md)
  A status that indicates the method encounters an error.
### Initializers
- [init?(rawValue: Int)](avaudioconverteroutputstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus](avaudioconverter/convert(to:error:withinputfrom:).md)
  Performs a conversion between audio formats, if the system supports it.
- [func convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](avaudioconverter/convert(to:from:).md)
  Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.
- [enum AVAudioConverterInputStatus](avaudioconverterinputstatus.md)
  An option that indicates the status of an audio converter input block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverteroutputstatus)*