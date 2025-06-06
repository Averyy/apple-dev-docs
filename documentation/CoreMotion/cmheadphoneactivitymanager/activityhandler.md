# CMHeadphoneActivityManager.ActivityHandler

**Framework**: Core Motion  
**Kind**: typealias

The type for a handler to be invoked when headphone motion activity data is available.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
typealias ActivityHandler = (CMMotionActivity?, (any Error)?) -> Void
```

## See Also

- [CMHeadphoneActivityManager.Status](cmheadphoneactivitymanager/status.md)
  Headphone connection status updates.
- [CMHeadphoneActivityManager.StatusHandler](cmheadphoneactivitymanager/statushandler.md)
  The type for a handler to be invoked with status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/activityhandler)*