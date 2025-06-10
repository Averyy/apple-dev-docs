# CMSampleBuffer.TimingPerSample.sequential(startingAt:)

**Framework**: Core Media  
**Kind**: case

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
case sequential(startingAt: CMSampleTimingInfo)
```

#### Discussion

Only the fist sample will have the decode time specified here. Samples must have the same decode and presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/timingpersample/sequential(startingat:))*