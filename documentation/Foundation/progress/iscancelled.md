# isCancelled

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that Indicates whether the receiver is tracking canceled work.

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
var isCancelled: Bool { get }
```

```objc
@property (readonly, getter=isCancelled) BOOL cancelled;
```

## Discussion

By default, [`Progress`](../progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

If the receiver has a canceled containing progress object, the receiver reports a canceled status.

## See Also

### Related Documentation
- [func cancel()](./cancel%28%29.md)
  Cancels progress tracking.
### Reporting Progress
- [var totalUnitCount: Int64](./totalunitcount.md)
  The total number of tracked units of work for the current progress.
- [var completedUnitCount: Int64](./completedunitcount.md)
  The number of completed units of work for the current job.
- [var localizedDescription: String!](./localizeddescription.md)
  A localized description of tracked progress for the receiver.
- [var localizedAdditionalDescription: String!](./localizedadditionaldescription.md)
  A more specific localized description of tracked progress for the receiver.
- [var isCancellable: Bool](./iscancellable.md)
  A Boolean value that indicates whether the receiver is tracking work that you can cancel.
- [var cancellationHandler: (() -> Void)?](./cancellationhandler.md)
  The block to invoke when canceling progress.
- [var isPausable: Bool](./ispausable.md)
  A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the receiver is tracking paused work.
- [var pausingHandler: (() -> Void)?](./pausinghandler.md)
  The block to invoke when pausing progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/iscancelled)*