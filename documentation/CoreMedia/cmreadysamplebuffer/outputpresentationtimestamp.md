# outputPresentationTimeStamp

**Framework**: Core Media  
**Kind**: property

The output presentation timestamp of the sample buffer.

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
var outputPresentationTimeStamp: CMTime { get set }
```

#### Discussion

This is the time at which the decoded, trimmed, stretched and possibly reversed samples should commence being presented. If this property has been set explicitly, the same value is returned.

Otherwise, the value is calculated as: `(PresentationTimeStamp + TrimDurationAtStart)` unless [`reverse`](cmsamplebuffer/attachmentkey/reverse.md) is true, in which case the value is calculated as: `(PresentationTimeStamp + Duration - TrimDurationAtEnd)`

These are generally correct for un-stretched, un-shifted playback. For general forward playback in a scaled edit, this property should be set to: `((PresentationTimeStamp + TrimDurationAtStart - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime` For general reversed playback: `((PresentationTimeStamp + Duration - TrimDurationAtEnd - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime`

- PresentationTimeStamp is `presentationTimeStamp` property of this sample buffer.
- Duration is `duration` property of this sample buffer.
- TrimDurationAtStart is the value of [`trimDurationAtStart`](cmsamplebuffer/attachmentkey/trimdurationatstart.md) attachment (default 0).
- TrimDurationAtEnd is the value of [`trimDurationAtEnd`](cmsamplebuffer/attachmentkey/trimdurationatend.md) attachment (default 0).
- SpeedMultiplier is the value of [`speedMultiplier`](cmsamplebuffer/attachmentkey/speedmultiplier.md) attachment (default 1).
- EditStartMediaTime is the start time of this playback segment.
- EditStartTrackTime is the start time of the media track.
- EditSpeedMultiplier is the speed of media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/outputpresentationtimestamp)*