# audioIndependentSampleDecoderRefreshCount

**Framework**: Core Media  
**Kind**: property

Only present if the audio sample is an independent frame or immediate playout frame.

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
var audioIndependentSampleDecoderRefreshCount: Int? { get set }
```

#### Discussion

Zero indicates an Immediate Playout Frame. Non-zero indicates an Independent Frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/audioindependentsampledecoderrefreshcount)*