# init(audioDataBuffer:formatDescription:sampleCount:presentationTimeStamp:)

**Framework**: Core Media  
**Kind**: init

Creates a sample buffer carrying audio media data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(audioDataBuffer content: Content, formatDescription: CMAudioFormatDescription, sampleCount: Int, presentationTimeStamp: CMTime)
```

#### Discussion

Use this init when the audio format is a linear PCM format or a constant bit rate (CBR) format. The `AudioStreamBasicDescription` in the format is used along with `sampleCount` & `presentationTimeStamp` to calculate the sample size & timings. The `AudioStreamBasicDescription/mBytesPerPacket` in the format description must be 0 for this init to consider it as a valid format. Otherwise, `init(compressedAudioDataBuffer:formatDescription:presentationTime:packetDescriptions:)` must be used along with a valid packet description array.

## Parameters

- `formatDescription`: Format description of the content. The format must have audio media type.
- `sampleCount`: Number of samples in the content. Must be greater than 0.
- `presentationTimeStamp`: The time at which the first sample will be presented. Must be valid numeric time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/init(audiodatabuffer:formatdescription:samplecount:presentationtimestamp:))*