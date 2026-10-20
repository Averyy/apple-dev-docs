# observedProgress

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The progress object to use for updating the progress view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var observedProgress: Progress? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSProgress * observedProgress;
```

#### Discussion

When this property is set, the progress view updates its progress value automatically using information it receives from the [`Progress`](../../Foundation/progress.md) object. (Progress updates are animated.) Set the property to `nil` when you want to update the progress manually. The default value of this property is `nil`.

For more information about configuring a progress object to manage progress information, see [`Progress`](../../Foundation/progress.md).

## See Also

### Managing the progress bar
- [var progress: Float](./progress.md)
  The current progress of the progress view.
- [func setProgress(Float, animated: Bool)](./setprogress%28_,animated%29.md)
  Adjusts the current progress of the progress view, optionally animating the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprogressview/observedprogress)*