# UIPageControlTimerProgress

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIPageControlTimerProgress : UIPageControlProgress
```

## Topics

### Initializers
- [init(preferredDuration: TimeInterval)](./uipagecontroltimerprogress/init%28preferredduration%29.md)
  Creates a time interval progress with a specified preferred duration.
### Instance Properties
- [var delegate: (any UIPageControlTimerProgressDelegate)?](./uipagecontroltimerprogress/delegate.md)
  An object that defines the delegate of the page control progress.
- [var isRunning: Bool](./uipagecontroltimerprogress/isrunning.md)
  Returns YES if the timer is currently active.
- [var preferredDuration: TimeInterval](./uipagecontroltimerprogress/preferredduration.md)
  The preferred duration for the time interval progress, used when there is no custom page duration set for the current page. The preferred duration must be greater than 0.0
- [var resetsToInitialPageAfterEnd: Bool](./uipagecontroltimerprogress/resetstoinitialpageafterend.md)
  Determines if the page control should loop back to page 0 after the last page. Default is NO.
### Instance Methods
- [func duration(forPage: Int) -> TimeInterval](./uipagecontroltimerprogress/duration%28forpage%29.md)
  Returns the duration for the specified page, and `preferredDuration` when there is no custom duration set for the specified page.
- [func pauseTimer()](./uipagecontroltimerprogress/pausetimer%28%29.md)
  Pause the timer if it is active.
- [func resumeTimer()](./uipagecontroltimerprogress/resumetimer%28%29.md)
  Resume the timer if it is not currently active.
- [func setDuration(TimeInterval, forPage: Int)](./uipagecontroltimerprogress/setduration%28_,forpage%29.md)
  Sets a custom duration for the specified page. Set 0.0 to remove the custom duration for the specified page.

## Relationships

### Inherits From
- [UIPageControlProgress](./uipagecontrolprogress.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring page progress
- [var progress: UIPageControlProgress?](./uipagecontrol/progress.md)
  An object that defines the progress of the page control. Default is nil.
- [class UIPageControlProgress](./uipagecontrolprogress.md)
- [protocol UIPageControlProgressDelegate](./uipagecontrolprogressdelegate.md)
- [protocol UIPageControlTimerProgressDelegate](./uipagecontroltimerprogressdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontroltimerprogress)*