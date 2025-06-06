# invalidateTimelineContent()

**Framework**: SwiftUI  
**Kind**: method

Resets any pre-rendered views the system has from the timeline.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- watchOS 8.0+

## Declaration

```swift
func invalidateTimelineContent()
```

#### Discussion

When entering Always On Display, the system might pre-render frames. If the content of these frames must change in a way that isn’t reflected by the schedule or the timeline view’s current bindings — for example, because the user changes the title of a future calendar event — call this method to request that the frames be regenerated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineview/context/invalidatetimelinecontent())*