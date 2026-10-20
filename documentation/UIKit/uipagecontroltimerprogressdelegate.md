# UIPageControlTimerProgressDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
protocol UIPageControlTimerProgressDelegate : UIPageControlProgressDelegate
```

```objc
@protocol UIPageControlTimerProgressDelegate <UIPageControlProgressDelegate>
```

## Topics

### Instance Methods
- [func pageControlTimerProgress(UIPageControlTimerProgress, shouldAdvanceToPage: Int) -> Bool](./uipagecontroltimerprogressdelegate/pagecontroltimerprogress%28_,shouldadvancetopage%29.md)
  Determines if the time interval progress should advance to the next page upon progress completion of the current page’s duration. Default is YES.
- [func pageControlTimerProgressDidChange(UIPageControlTimerProgress)](./uipagecontroltimerprogressdelegate/pagecontroltimerprogressdidchange%28_%29.md)
  Called when the progress has changed from the time interval progress.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIPageControlProgressDelegate](./uipagecontrolprogressdelegate.md)

## See Also

### Configuring page progress
- [var progress: UIPageControlProgress?](./uipagecontrol/progress.md)
  An object that defines the progress of the page control. Default is nil.
- [class UIPageControlProgress](./uipagecontrolprogress.md)
- [class UIPageControlTimerProgress](./uipagecontroltimerprogress.md)
- [protocol UIPageControlProgressDelegate](./uipagecontrolprogressdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontroltimerprogressdelegate)*