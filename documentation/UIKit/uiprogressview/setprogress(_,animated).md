# setProgress(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adjusts the current progress of the progress view, optionally animating the change.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setProgress(_ progress: Float, animated: Bool)
```

```objc
- (void) setProgress:(float) progress animated:(BOOL) animated;
```

## Discussion

The current progress is represented by a floating-point value between 0.0 and 1.0, inclusive, where 1.0 indicates the completion of the task. The default value is 0.0. Values less than 0.0 and greater than 1.0 are pinned to those limits.

## Parameters

- `progress`: The new progress value.
- `animated`: [`true`](../../Swift/true.md) if the change should be animated, [`false`](../../Swift/false.md) if the change should happen immediately.

## See Also

### Managing the progress bar
- [var progress: Float](./progress.md)
  The current progress of the progress view.
- [var observedProgress: Progress?](./observedprogress.md)
  The progress object to use for updating the progress view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/setprogress(_:animated:))*