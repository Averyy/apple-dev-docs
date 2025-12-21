# decodeTimeStamp

**Framework**: Core Media  
**Kind**: property

Numerically earliest sample decode timestamp in the sample buffer.

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
var decodeTimeStamp: CMTime { get }
```

#### Discussion

Return the decode timestamp of the first sample in the buffer, since even out-of-presentation-order samples are expected to be in decode order in the buffer.

Returns [`invalid`](cmtime/invalid.md) if `sampleTimings` is empty or contains invalid [`decodeTimeStamp`](cmsampletiminginfo/decodetimestamp.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/decodetimestamp)*