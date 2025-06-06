# progress

**Framework**: UIKit  
**Kind**: property

The current progress of the progress view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var progress: Float { get set }
```

#### Discussion

The current progress is represented by a floating-point value between 0.0 and 1.0, inclusive, where 1.0 indicates the completion of the task. The default value is 0.0. Values less than 0.0 and greater than 1.0 are pinned to those limits.

## See Also

- [func setProgress(Float, animated: Bool)](uiprogressview/setprogress(_:animated:).md)
  Adjusts the current progress of the progress view, optionally animating the change.
- [var observedProgress: Progress?](uiprogressview/observedprogress.md)
  The progress object to use for updating the progress view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/progress)*