# NSHapticFeedbackManager.PerformanceTime.drawCompleted

**Framework**: AppKit  
**Kind**: case

Instructs the system to provide haptic feedback to the user the next time the screen is updated.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case drawCompleted
```

## See Also

- [NSHapticFeedbackManager.PerformanceTime.default](nshapticfeedbackmanager/performancetime/default.md)
  Allows the system to choose the most appropriate time for feedback to be provided. Currently, this is the next time the screen is updated.
- [NSHapticFeedbackManager.PerformanceTime.now](nshapticfeedbackmanager/performancetime/now.md)
  Instructs the system to provide immediate haptic feedback to the user, rather than waiting for synchronization to occur with something visual occurring on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager/performancetime/drawcompleted)*