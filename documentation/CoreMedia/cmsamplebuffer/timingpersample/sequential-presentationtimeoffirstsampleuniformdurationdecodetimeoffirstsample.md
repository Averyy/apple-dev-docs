# sequential(presentationTimeOfFirstSample:uniformDuration:decodeTimeOfFirstSample:)

**Framework**: Core Media  
**Kind**: method

All samples are adjacent to each other and have the same duration.

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
static func sequential(presentationTimeOfFirstSample: CMTime, uniformDuration: CMTime, decodeTimeOfFirstSample: CMTime = .invalid) -> CMSampleBuffer.TimingPerSample
```

## Parameters

- `presentationTimeOfFirstSample`: Time at which the first sample is presented.
- `uniformDuration`: Duration shared by ever sample in the sample buffer.
- `decodeTimeOfFirstSample`: Time at which the first sample is decoded. Samples must have the same   decode and presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/timingpersample/sequential(presentationtimeoffirstsample:uniformduration:decodetimeoffirstsample:))*