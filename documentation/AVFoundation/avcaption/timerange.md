# timeRange

**Framework**: AVFoundation  
**Kind**: property

The time range over which the system presents the caption.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

#### Discussion

Apple iTT format only permits captions to have overlapping time ranges if they’re associated with different regions.

CEA608 closed caption time ranges can’t start with zero, because the decoder needs transmission time. Align time ranges with the video frame rate.

## See Also

- [var text: String](avcaption/text.md)
  The caption text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption/timerange)*