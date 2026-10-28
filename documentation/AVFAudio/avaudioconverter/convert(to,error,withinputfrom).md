# convert(to:error:withInputFrom:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Performs a conversion between audio formats, if the system supports it.

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
func convert(to outputBuffer: AVAudioBuffer, error outError: NSErrorPointer, withInputFrom inputBlock: (AVAudioPacketCount, UnsafeMutablePointer<AVAudioConverterInputStatus>) -> AVAudioBuffer?) -> AVAudioConverterOutputStatus
```

```objc
- (AVAudioConverterOutputStatus) convertToBuffer:(AVAudioBuffer *) outputBuffer error:(NSError **) outError withInputFromBlock:(AVAudioConverterInputBlock) inputBlock;
```

## Return Value

An [`AVAudioConverterOutputStatus`](../avaudioconverteroutputstatus.md) type that indicates the conversion status.

## Discussion

The method attempts to fill the buffer to its capacity. On return, the buffer’s length indicates the number of sample frames the framework successfully converts.

## Parameters

- `outputBuffer`: The output audio buffer.
- `outError`: The error if the conversion fails.
- `inputBlock`: A block the framework calls to get input data.

## Topics

### Input callback
- [typealias AVAudioConverterInputBlock](../avaudioconverterinputblock.md)
  A block to get input data for conversion, as necessary.

## See Also

### Converting audio formats
- [typealias AVAudioConverterInputBlock](../avaudioconverterinputblock.md)
  A block to get input data for conversion, as necessary.
- [func convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](./convert%28to,from%29.md)
  Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.
- [enum AVAudioConverterInputStatus](../avaudioconverterinputstatus.md)
  An option that indicates the status of an audio converter input block.
- [enum AVAudioConverterOutputStatus](../avaudioconverteroutputstatus.md)
  An option that indicates the return status of an audio converter method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/convert(to:error:withinputfrom:))*