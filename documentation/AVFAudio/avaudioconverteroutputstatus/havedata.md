# AVAudioConverterOutputStatus.haveData

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A status that indicates that the method returns all of the requested data.

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
case haveData
```

```c
AVAudioConverterOutputStatus_HaveData
```

## See Also

### Interpreting conversion results
- [AVAudioConverterOutputStatus.inputRanDry](./inputrandry.md)
  A status that indicates the method doesn’t have enough input available to satisfy the request.
- [AVAudioConverterOutputStatus.endOfStream](./endofstream.md)
  A status that indicates the method reaches the end of the stream, and doesn’t return any data.
- [AVAudioConverterOutputStatus.error](./error.md)
  A status that indicates the method encounters an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverteroutputstatus/havedata)*