# totalUnitCount

**Framework**: Foundation  
**Kind**: property

The total number of tracked units of work for the current progress.

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
var totalUnitCount: Int64 { get set }
```

#### Discussion

For an [`Progress`](progress.md) with a kind of [`file`](progresskind/file.md), the unit of this property is bytes, and the [`fileTotalCountKey`](progressuserinfokey/filetotalcountkey.md) and [`fileCompletedCountKey`](progressuserinfokey/filecompletedcountkey.md) keys in the `userInfo` dictionary report the overall count of files.

For any other kind of [`Progress`](progress.md), the unit of measurement doesn’t matter as long as it’s consistent. You can report the values to the user in the [`localizedDescription`](progress/localizeddescription.md) and [`localizedAdditionalDescription`](progress/localizedadditionaldescription.md).

## See Also

- [var fractionCompleted: Double](progress/fractioncompleted.md)
  The fraction of the overall work that the progress object completes, including work from its suboperations.
- [var completedUnitCount: Int64](progress/completedunitcount.md)
  The number of completed units of work for the current job.
- [var localizedDescription: String!](progress/localizeddescription.md)
  A localized description of tracked progress for the receiver.
- [var localizedAdditionalDescription: String!](progress/localizedadditionaldescription.md)
  A more specific localized description of tracked progress for the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/totalunitcount)*