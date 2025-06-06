# localizedAdditionalDescription

**Framework**: Foundation  
**Kind**: property

A more specific localized description of tracked progress for the receiver.

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
var localizedAdditionalDescription: String! { get set }
```

#### Discussion

If you don’t specify your own custom value for this property, [`Progress`](progress.md) uses the value of the [`kind`](progress/kind.md) property to determine how to use the values of other properties, as well as values in the user info dictionary, to return an automatically computed string. If it fails to do that, it returns an empty string.

The [`localizedAdditionalDescription`](progress/localizedadditionaldescription.md) is more specific than [`localizedDescription`](progress/localizeddescription.md) about the work the receiver is tracking at any particular moment. Depending on the kind of progress, the completed and total unit counts, and other parameters, localized additional descriptions resemble the following:

- 3 of 10 files
- 123 KB of 789.1 MB
- 3.3 MB of 103.92 GB – 2 hours remaining
- 1.61 GB of 3.22 GB (2 KB/sec) – 2 minutes remaining
- 1 minute remaining (1 KB/sec)

By default, [`Progress`](progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

- [var totalUnitCount: Int64](progress/totalunitcount.md)
  The total number of tracked units of work for the current progress.
- [var completedUnitCount: Int64](progress/completedunitcount.md)
  The number of completed units of work for the current job.
- [var localizedDescription: String!](progress/localizeddescription.md)
  A localized description of tracked progress for the receiver.
- [var isCancellable: Bool](progress/iscancellable.md)
  A Boolean value that indicates whether the receiver is tracking work that you can cancel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/localizedadditionaldescription)*