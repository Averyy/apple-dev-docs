# timings

**Framework**: Core Media  
**Kind**: property

Access sample timings.

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
var timings: CMSampleBuffer.TimingPerSample? { get set }
```

#### Discussion

When setting distinct timings, the number of entries must match [`count`](cmsamplebuffer/samplepropertiescollection/count.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/samplepropertiescollection/timings)*