# AVAudioConverterOutputStatus

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVAudioConverterOutputStatus : NSInteger;
```

## Topics

### Creating an output status
- [init?(rawValue: Int)](./avaudioconverteroutputstatus/init%28rawvalue%29.md)
### Interpreting conversion results
- [AVAudioConverterOutputStatus.haveData](./avaudioconverteroutputstatus/havedata.md)
  A status that indicates that the method returns all of the requested data.
- [AVAudioConverterOutputStatus.inputRanDry](./avaudioconverteroutputstatus/inputrandry.md)
  A status that indicates the method doesn’t have enough input available to satisfy the request.
- [AVAudioConverterOutputStatus.endOfStream](./avaudioconverteroutputstatus/endofstream.md)
  A status that indicates the method reaches the end of the stream, and doesn’t return any data.
- [AVAudioConverterOutputStatus.error](./avaudioconverteroutputstatus/error.md)
  A status that indicates the method encounters an error.

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
- [enum AVAudioConverterInputStatus](./avaudioconverterinputstatus.md)
  An option that indicates the status of an audio converter input block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverteroutputstatus)*