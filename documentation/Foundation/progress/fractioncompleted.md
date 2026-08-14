# fractionCompleted

**Framework**: Foundation  
**Kind**: property

The fraction of the overall work that the progress object completes, including work from its suboperations.

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
var fractionCompleted: Double { get }
```

#### Discussion

If the receiver object doesn’t have any suboperations, [`fractionCompleted`](progress/fractioncompleted.md) is generally the result of dividing [`completedUnitCount`](progress/completedunitcount.md) by [`totalUnitCount`](progress/totalunitcount.md). Setting both [`totalUnitCount`](progress/totalunitcount.md) and [`completedUnitCount`](progress/completedunitcount.md) properties to zero indicates that there is no progress to track. In this case, the [`isIndeterminate`](progress/isindeterminate.md) property returns [`false`](https://developer.apple.com/documentation/swift/false) and the [`fractionCompleted`](progress/fractioncompleted.md) property returns `0.0`.

If the receiver does have suboperations, [`fractionCompleted`](progress/fractioncompleted.md) reflects progress from those progress objects in addition to its own [`completedUnitCount`](progress/completedunitcount.md). When the suboperations finish, the [`completedUnitCount`](progress/completedunitcount.md) of the containing progress object updates.

## See Also

- [var isIndeterminate: Bool](progress/isindeterminate.md)
  A Boolean value that indicates whether the tracked progress is indeterminate.
- [var isFinished: Bool](progress/isfinished.md)
  A Boolean value that indicates the progress object is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/fractioncompleted)*