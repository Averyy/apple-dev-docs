# duration

**Framework**: Core Media  
**Kind**: property

The unmodified sum of the durations of all samples in the sample buffer.

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
var duration: CMTime { get }
```

#### Discussion

If the buffer contains out-of-presentation-order samples, any gaps in the presentation timeline are not represented in the returned duration. The calculated duration is simply the sum of all the individual sample durations.

Returns [`invalid`](cmtime/invalid.md) if `sampleTimings` is empty or contains invalid [`duration`](cmsampletiminginfo/duration.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/duration-2ssr4)*