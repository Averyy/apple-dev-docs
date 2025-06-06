# setProgress(_:animated:)

**Framework**: UIKit  
**Kind**: method

Adjusts the current progress of the progress view, optionally animating the change.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setProgress(_ progress: Float, animated: Bool)
```

#### Discussion

The current progress is represented by a floating-point value between 0.0 and 1.0, inclusive, where 1.0 indicates the completion of the task. The default value is 0.0. Values less than 0.0 and greater than 1.0 are pinned to those limits.

## Parameters

- `progress`: The new progress value.
- `animated`:   if the change should be animated,   if the change should happen immediately.

## See Also

- [var progress: Float](uiprogressview/progress.md)
  The current progress of the progress view.
- [var observedProgress: Progress?](uiprogressview/observedprogress.md)
  The progress object to use for updating the progress view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/setprogress(_:animated:))*