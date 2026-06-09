# init(timeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:)

**Framework**: AVKit  
**Kind**: init

Initializes a new timeline segment with the specified characteristics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(timeRange: CMTimeRange, auxiliaryContent: Bool, marked: Bool, requiresLinearPlayback: Bool, identifier: String?)
```

## Parameters

- `timeRange`: The time range defining the segment’s position and duration within the timeline.
- `auxiliaryContent`: Whether the segment contains main or auxiliary content.
- `marked`: Whether the segment should be visually highlighted in the timeline UI.
- `requiresLinearPlayback`: Whether the segment must be played sequentially without seeking or skipping.
- `identifier`: External identifier for tracking or analytics purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment/init(timerange:auxiliarycontent:marked:requireslinearplayback:identifier:))*