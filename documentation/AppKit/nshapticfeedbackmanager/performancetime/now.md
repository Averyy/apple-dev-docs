# NSHapticFeedbackManager.PerformanceTime.now

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Instructs the system to provide immediate haptic feedback to the user, rather than waiting for synchronization to occur with something visual occurring on screen.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case now
```

```c
NSHapticFeedbackPerformanceTimeNow
```

## See Also

### Constants
- [NSHapticFeedbackManager.PerformanceTime.default](./default.md)
  Allows the system to choose the most appropriate time for feedback to be provided. Currently, this is the next time the screen is updated.
- [NSHapticFeedbackManager.PerformanceTime.drawCompleted](./drawcompleted.md)
  Instructs the system to provide haptic feedback to the user the next time the screen is updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager/performancetime/now)*