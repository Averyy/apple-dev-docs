# outputDuration

**Framework**: Core Media  
**Kind**: property

The output duration of the sample buffer.

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
var outputDuration: CMTime { get }
```

#### Discussion

This is the duration of decoded, trimmed and stretched samples. It is calculated as: `(Duration - TrimDurationAtStart - TrimDurationAtEnd) / SpeedMultiplier`.

- Duration is `duration` property of this sample buffer.
- TrimDurationAtStart is the value of [`trimDurationAtStart`](cmsamplebuffer/attachmentkey/trimdurationatstart.md) attachment (default 0).
- TrimDurationAtEnd is the value of [`trimDurationAtEnd`](cmsamplebuffer/attachmentkey/trimdurationatend.md) attachment (default 0).
- SpeedMultiplier is the value of [`speedMultiplier`](cmsamplebuffer/attachmentkey/speedmultiplier.md) attachment (default 1).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/outputduration)*