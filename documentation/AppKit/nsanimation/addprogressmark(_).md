# addProgressMark(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the progress mark to the receiver.

**Availability**:
- macOS

## Declaration

```swift
func addProgressMark(_ progressMark: NSAnimation.Progress)
```

```objc
- (void) addProgressMark:(NSAnimationProgress) progressMark;
```

## Discussion

A progress mark represents a percentage of the animation completed. When the animation reaches a progress mark, an [`animation(_:didReachProgressMark:)`](../nsanimationdelegate/animation%28_,didreachprogressmark%29.md) message is sent to the delegate and an [`progressMarkNotification`](./progressmarknotification.md) is broadcast to all observers. You might receive multiple notifications of progress advances over multiple marks.

## Parameters

- `progressMark`: A `float` value (typed as NSAnimationProgress) between 0.0 and 1.0. Values outside that range are pinned to 0.0 or 1.0, whichever is nearest.

## See Also

### Related Documentation
- [var currentProgress: NSAnimation.Progress](./currentprogress.md)
  The current progress of the animation.
### Managing Progress Marks
- [func removeProgressMark(NSAnimation.Progress)](./removeprogressmark%28_%29.md)
  Removes progress mark from the receiver.
- [var progressMarks: [NSNumber]](./progressmarks.md)
  An array of floating-point numbers representing current progress marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/addprogressmark(_:))*