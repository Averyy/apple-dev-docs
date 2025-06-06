# isCancellable

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the receiver is tracking work that you can cancel.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isCancellable: Bool { get set }
```

#### Discussion

By default, [`Progress`](progress.md) objects are cancelable.

You typically use this property to communicate whether controls for canceling appear in a progress-reporting user interface. [`Progress`](progress.md) itself doesn’t do anything with this property other than help pass the value from progress reporters to progress observers.

If an [`Progress`](progress.md) is cancelable, implement the ability to cancel progress either by setting a block for the [`cancellationHandler`](progress/cancellationhandler.md) property, or by polling the [`isCancelled`](progress/iscancelled.md) property periodically while performing the relevant work.

It’s valid for the value of this property to change during the lifetime of an [`Progress`](progress.md) object. By default, [`Progress`](progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

- [func cancel()](progress/cancel.md)
  Cancels progress tracking.
- [var totalUnitCount: Int64](progress/totalunitcount.md)
  The total number of tracked units of work for the current progress.
- [var completedUnitCount: Int64](progress/completedunitcount.md)
  The number of completed units of work for the current job.
- [var localizedDescription: String!](progress/localizeddescription.md)
  A localized description of tracked progress for the receiver.
- [var localizedAdditionalDescription: String!](progress/localizedadditionaldescription.md)
  A more specific localized description of tracked progress for the receiver.
- [var isCancelled: Bool](progress/iscancelled.md)
  A Boolean value that Indicates whether the receiver is tracking canceled work.
- [var cancellationHandler: (() -> Void)?](progress/cancellationhandler.md)
  The block to invoke when canceling progress.
- [var isPausable: Bool](progress/ispausable.md)
  A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [var isPaused: Bool](progress/ispaused.md)
  A Boolean value that indicates whether the receiver is tracking paused work.
- [var pausingHandler: (() -> Void)?](progress/pausinghandler.md)
  The block to invoke when pausing progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/iscancellable)*