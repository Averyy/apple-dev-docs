# AVAudioConverterInputStatus

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVAudioConverterInputStatus : NSInteger;
```

## Topics

### Creating an input status
- [init?(rawValue: Int)](./avaudioconverterinputstatus/init%28rawvalue%29.md)
### Reporting input status
- [AVAudioConverterInputStatus.endOfStream](./avaudioconverterinputstatus/endofstream.md)
  A status that indicates you’re at the end of an audio stream.
- [AVAudioConverterInputStatus.haveData](./avaudioconverterinputstatus/havedata.md)
  A status that indicates the normal case where you supply data to the converter.
- [AVAudioConverterInputStatus.noDataNow](./avaudioconverterinputstatus/nodatanow.md)
  A status that indicates you’re out of data.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Converting audio formats
- [func convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: (AVAudioPacketCount, UnsafeMutablePointer<AVAudioConverterInputStatus>) -> AVAudioBuffer?) -> AVAudioConverterOutputStatus](./avaudioconverter/convert%28to,error,withinputfrom%29.md)
  Performs a conversion between audio formats, if the system supports it.
- [typealias AVAudioConverterInputBlock](./avaudioconverterinputblock.md)
  A block to get input data for conversion, as necessary.
- [func convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](./avaudioconverter/convert%28to,from%29.md)
  Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.
- [enum AVAudioConverterOutputStatus](./avaudioconverteroutputstatus.md)
  An option that indicates the return status of an audio converter method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterinputstatus)*