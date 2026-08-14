# UIPageControlProgress

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
class UIPageControlProgress
```

## Topics

### Instance Properties
- [var currentProgress: Float](uipagecontrolprogress/currentprogress.md)
  The current progress value of the active page control indicator, between 0 and 1. Values outside of [0…1] will be clamped.
- [var delegate: (any UIPageControlProgressDelegate)?](uipagecontrolprogress/delegate.md)
  An object that defines the delegate of the page control progress.
- [var isProgressVisible: Bool](uipagecontrolprogress/isprogressvisible.md)
  Returns `YES` if the progress indicator is visible. The progress indicator is hidden when the user is actively interacting with the `UIPageControl`.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [UIPageControlTimerProgress](uipagecontroltimerprogress.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var progress: UIPageControlProgress?](uipagecontrol/progress.md)
  An object that defines the progress of the page control. Default is nil.
- [class UIPageControlTimerProgress](uipagecontroltimerprogress.md)
- [protocol UIPageControlProgressDelegate](uipagecontrolprogressdelegate.md)
- [protocol UIPageControlTimerProgressDelegate](uipagecontroltimerprogressdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrolprogress)*