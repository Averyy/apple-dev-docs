# AVAudioConverterInputStatus

**Framework**: AVFAudio  
**Kind**: enum

An option that indicates the status of an audio converter input block.

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
enum AVAudioConverterInputStatus
```

## Topics

### Status Options
- [AVAudioConverterInputStatus.endOfStream](avaudioconverterinputstatus/endofstream.md)
  A status that indicates you’re at the end of an audio stream.
- [AVAudioConverterInputStatus.haveData](avaudioconverterinputstatus/havedata.md)
  A status that indicates the normal case where you supply data to the converter.
- [AVAudioConverterInputStatus.noDataNow](avaudioconverterinputstatus/nodatanow.md)
  A status that indicates you’re out of data.
### Initializers
- [init?(rawValue: Int)](avaudioconverterinputstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: AVAudioConverterInputBlock) -> AVAudioConverterOutputStatus](avaudioconverter/convert(to:error:withinputfrom:).md)
  Performs a conversion between audio formats, if the system supports it.
- [func convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](avaudioconverter/convert(to:from:).md)
  Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.
- [enum AVAudioConverterOutputStatus](avaudioconverteroutputstatus.md)
  An option that indicates the return status of an audio converter method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterinputstatus)*