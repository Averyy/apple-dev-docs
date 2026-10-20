# UIPageControlProgressDelegate

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
protocol UIPageControlProgressDelegate : NSObjectProtocol
```

```objc
@protocol UIPageControlProgressDelegate <NSObject>
```

## Topics

### Instance Methods
- [func pageControlProgress(UIPageControlProgress, initialProgressForPage: Int) -> Float](./uipagecontrolprogressdelegate/pagecontrolprogress%28_,initialprogressforpage%29.md)
  Returns the initial progress (between 0…1) for the specified page. By default, `currentProgress` is set to 0 when the page changes.
- [func pageControlProgressVisibilityDidChange(UIPageControlProgress)](./uipagecontrolprogressdelegate/pagecontrolprogressvisibilitydidchange%28_%29.md)
  Called when the page control progress visibility has changed, which could occur when the page control is being interacted with. The page control progress becomes hidden when the user begins to interact with the page control (when it begins continuous interaction), and is visible again when the user stops interacting with the control. Observe the page control progress visibility to pause or resume the paging content.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [UIPageControlTimerProgressDelegate](./uipagecontroltimerprogressdelegate.md)

## See Also

### Configuring page progress
- [var progress: UIPageControlProgress?](./uipagecontrol/progress.md)
  An object that defines the progress of the page control. Default is nil.
- [class UIPageControlProgress](./uipagecontrolprogress.md)
- [class UIPageControlTimerProgress](./uipagecontroltimerprogress.md)
- [protocol UIPageControlTimerProgressDelegate](./uipagecontroltimerprogressdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrolprogressdelegate)*