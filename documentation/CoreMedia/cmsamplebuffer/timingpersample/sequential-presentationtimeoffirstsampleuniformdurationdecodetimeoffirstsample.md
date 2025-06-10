# sequential(presentationTimeOfFirstSample:uniformDuration:decodeTimeOfFirstSample:)

**Framework**: Core Media  
**Kind**: method

All samples are adjacent to each other and have the same duration.

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
static func sequential(presentationTimeOfFirstSample: CMTime, uniformDuration: CMTime, decodeTimeOfFirstSample: CMTime = .invalid) -> CMSampleBuffer.TimingPerSample
```

## Parameters

- `presentationTimeOfFirstSample`: Time at which the first sample is presented.
- `uniformDuration`: Duration shared by ever sample in the sample buffer.
- `decodeTimeOfFirstSample`: Time at which the first sample is decoded. Samples must have the same   decode and presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/timingpersample/sequential(presentationtimeoffirstsample:uniformduration:decodetimeoffirstsample:))*