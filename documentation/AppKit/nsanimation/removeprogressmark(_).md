# removeProgressMark(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes progress mark from the receiver.

**Availability**:
- macOS

## Declaration

```swift
func removeProgressMark(_ progressMark: NSAnimation.Progress)
```

```objc
- (void) removeProgressMark:(NSAnimationProgress) progressMark;
```

## Parameters

- `progressMark`: A `float` value (typed as NSAnimationProgress) that indicates the portion of the animation completed. The value should correspond to a progress mark set with [`addProgressMark(_:)`](./addprogressmark%28_%29.md) or [`NSAnimation`](../nsanimation.md).

## See Also

### Managing Progress Marks
- [func addProgressMark(NSAnimation.Progress)](./addprogressmark%28_%29.md)
  Adds the progress mark to the receiver.
- [var progressMarks: [NSNumber]](./progressmarks.md)
  An array of floating-point numbers representing current progress marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/removeprogressmark(_:))*