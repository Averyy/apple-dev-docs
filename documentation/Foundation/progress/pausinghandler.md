# pausingHandler

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The block to invoke when pausing progress.

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
var pausingHandler: (@Sendable () -> Void)? { get set }
```

```objc
@property (copy, nullable) void (^pausingHandler)();
```

#### Discussion

If the receiver is a suboperation of another progress object, the system invokes the [`pausingHandler`](./pausinghandler.md) block when pausing the containing progress object.

##### Special Considerations

You’re responsible for pausing any work for the progress object.

You can invoke the pausing handler on any queue. If you must do work on a specific queue, dispatch to that queue from within the pausing handler block.

## See Also

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
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that Indicates whether the receiver is tracking canceled work.
- [var cancellationHandler: (() -> Void)?](./cancellationhandler.md)
  The block to invoke when canceling progress.
- [var isPausable: Bool](./ispausable.md)
  A Boolean value that indicates whether the receiver is tracking work that you can pause.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the receiver is tracking paused work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/pausinghandler)*