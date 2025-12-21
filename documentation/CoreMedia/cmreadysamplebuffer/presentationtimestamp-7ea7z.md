# presentationTimeStamp

**Framework**: Core Media  
**Kind**: property

Numerically earliest sample presentation timestamp in the sample buffer.

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
var presentationTimeStamp: CMTime { get }
```

#### Discussion

For in-presentation-order samples, this is the presentation timestamp of the first sample.

For out-of-presentation-order samples, this is the presentation timestamp of the sample that will be presented first, which is not necessarily the first sample in the buffer.

Returns [`invalid`](cmtime/invalid.md) if `sampleTimings` is empty or contains invalid [`presentationTimeStamp`](cmsampletiminginfo/presentationtimestamp.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/presentationtimestamp-7ea7z)*