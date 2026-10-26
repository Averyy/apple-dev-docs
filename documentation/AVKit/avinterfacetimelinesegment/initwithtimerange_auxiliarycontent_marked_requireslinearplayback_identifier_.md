# initWithTimeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Initializes a new timeline segment with the specified characteristics.

## Declaration

```objc
- (instancetype) initWithTimeRange:(CMTimeRange) timeRange auxiliaryContent:(BOOL) auxiliaryContent marked:(BOOL) marked requiresLinearPlayback:(BOOL) requiresLinearPlayback identifier:(NSString *) identifier;
```

## Parameters

- `timeRange`: The time range defining the segment’s position and duration within the timeline.
- `auxiliaryContent`: Whether the segment contains main or auxiliary content.
- `marked`: Whether the segment should be visually highlighted in the timeline UI.
- `requiresLinearPlayback`: Whether the segment must be played sequentially without seeking or skipping.
- `identifier`: External identifier for tracking or analytics purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment/initwithtimerange:auxiliarycontent:marked:requireslinearplayback:identifier:)*