# addProgressMark(_:)

**Framework**: AppKit  
**Kind**: method

Adds the progress mark to the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func addProgressMark(_ progressMark: NSAnimation.Progress)
```

#### Discussion

A progress mark represents a percentage of the animation completed. When the animation reaches a progress mark, an [`animation(_:didReachProgressMark:)`](nsanimationdelegate/animation(_:didreachprogressmark:).md) message is sent to the delegate and an [`progressMarkNotification`](nsanimation/progressmarknotification.md) is broadcast to all observers. You might receive multiple notifications of progress advances over multiple marks.

## Parameters

- `progressMark`: A   value (typed as NSAnimationProgress) between 0.0 and 1.0. Values outside that range are pinned to 0.0 or 1.0, whichever is nearest.

## See Also

- [var currentProgress: NSAnimation.Progress](nsanimation/currentprogress.md)
  The current progress of the animation.
- [func removeProgressMark(NSAnimation.Progress)](nsanimation/removeprogressmark(_:).md)
  Removes progress mark from the receiver.
- [var progressMarks: [NSNumber]](nsanimation/progressmarks.md)
  An array of floating-point numbers representing current progress marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/addprogressmark(_:))*