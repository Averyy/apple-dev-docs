# removeProgressMark(_:)

**Framework**: AppKit  
**Kind**: method

Removes progress mark from the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeProgressMark(_ progressMark: NSAnimation.Progress)
```

## Parameters

- `progressMark`: A `float` value (typed as NSAnimationProgress) that indicates the portion of the animation completed. The value should correspond to a progress mark set with [`addProgressMark(_:)`](nsanimation/addprogressmark(_:).md) or [`NSAnimation`](nsanimation.md).

## See Also

- [func addProgressMark(NSAnimation.Progress)](nsanimation/addprogressmark(_:).md)
  Adds the progress mark to the receiver.
- [var progressMarks: [NSNumber]](nsanimation/progressmarks.md)
  An array of floating-point numbers representing current progress marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/removeprogressmark(_:))*