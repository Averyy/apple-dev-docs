# init(compressedAudioDataBuffer:formatDescription:presentationTimeStamp:packetDescriptions:)

**Framework**: Core Media  
**Kind**: init

Creates a sample buffer carrying compressed audio media data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(compressedAudioDataBuffer content: Content, formatDescription: CMAudioFormatDescription, presentationTimeStamp: CMTime, packetDescriptions: [AudioStreamPacketDescription])
```

#### Discussion

Use this init when the audio format where the packet size isn’t constant, such as variable bit rate or when the channels have unequal sizes. The `packetDescriptions` are used along with `presentationTimeStamp` to calculate the sample count, sample sizes & sample timings.

## Parameters

- `formatDescription`: Format description of the content. The format must have audio media type.
- `presentationTimeStamp`: The time at which the first sample will be presented. Must be valid numeric time.
- `packetDescriptions`: Array of packet descriptions one for each sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/init(compressedaudiodatabuffer:formatdescription:presentationtimestamp:packetdescriptions:))*