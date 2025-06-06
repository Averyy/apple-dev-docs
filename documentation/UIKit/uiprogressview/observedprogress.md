# observedProgress

**Framework**: UIKit  
**Kind**: property

The progress object to use for updating the progress view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var observedProgress: Progress? { get set }
```

#### Discussion

When this property is set, the progress view updates its progress value automatically using information it receives from the [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) object. (Progress updates are animated.) Set the property to `nil` when you want to update the progress manually. The default value of this property is `nil`.

For more information about configuring a progress object to manage progress information, see [`Progress`](https://developer.apple.com/documentation/Foundation/Progress).

## See Also

- [var progress: Float](uiprogressview/progress.md)
  The current progress of the progress view.
- [func setProgress(Float, animated: Bool)](uiprogressview/setprogress(_:animated:).md)
  Adjusts the current progress of the progress view, optionally animating the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/observedprogress)*