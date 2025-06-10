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
### Instance Properties
- [var delegate: (any UIPageControlTimerProgressDelegate)?](uipagecontroltimerprogress/delegate.md)
- [var isRunning: Bool](uipagecontroltimerprogress/isrunning.md)
- [var preferredDuration: TimeInterval](uipagecontroltimerprogress/preferredduration.md)
- [var resetsToInitialPageAfterEnd: Bool](uipagecontroltimerprogress/resetstoinitialpageafterend.md)
### Instance Methods
- [func duration(forPage: Int) -> TimeInterval](uipagecontroltimerprogress/duration(forpage:).md)
- [func pauseTimer()](uipagecontroltimerprogress/pausetimer.md)
- [func resumeTimer()](uipagecontroltimerprogress/resumetimer.md)
- [func setDuration(TimeInterval, forPage: Int)](uipagecontroltimerprogress/setduration(_:forpage:).md)

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
- [class UIPageControlProgress](uipagecontrolprogress.md)
- [protocol UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)
- [protocol UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontroltimerprogress)*