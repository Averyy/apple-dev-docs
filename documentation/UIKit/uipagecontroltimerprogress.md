# UIPageControlTimerProgress

**Framework**: UIKit  
**Kind**: class

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class UIPageControlTimerProgress
```

## Topics

### Initializers
- [init(preferredDuration: TimeInterval)](uipagecontroltimerprogress/init(preferredduration:).md)
  Creates a time interval progress with a specified preferred duration.
### Instance Properties
- [var delegate: (any UIPageControlTimerProgressDelegate)?](uipagecontroltimerprogress/delegate.md)
  An object that defines the delegate of the page control progress.
- [var isRunning: Bool](uipagecontroltimerprogress/isrunning.md)
  Returns YES if the timer is currently active.
- [var preferredDuration: TimeInterval](uipagecontroltimerprogress/preferredduration.md)
  The preferred duration for the time interval progress, used when there is no custom page duration set for the current page. The preferred duration must be greater than 0.0
- [var resetsToInitialPageAfterEnd: Bool](uipagecontroltimerprogress/resetstoinitialpageafterend.md)
  Determines if the page control should loop back to page 0 after the last page. Default is NO.
### Instance Methods
- [func duration(forPage: Int) -> TimeInterval](uipagecontroltimerprogress/duration(forpage:).md)
  Returns the duration for the specified page, and `preferredDuration` when there is no custom duration set for the specified page.
- [func pauseTimer()](uipagecontroltimerprogress/pausetimer.md)
  Pause the timer if it is active.
- [func resumeTimer()](uipagecontroltimerprogress/resumetimer.md)
  Resume the timer if it is not currently active.
- [func setDuration(TimeInterval, forPage: Int)](uipagecontroltimerprogress/setduration(_:forpage:).md)
  Sets a custom duration for the specified page. Set 0.0 to remove the custom duration for the specified page.

## Relationships

### Inherits From
- [UIPageControlProgress](uipagecontrolprogress.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var progress: UIPageControlProgress?](uipagecontrol/progress.md)
  An object that defines the progress of the page control. Default is nil.
- [class UIPageControlProgress](uipagecontrolprogress.md)
- [protocol UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)
- [protocol UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontroltimerprogress)*