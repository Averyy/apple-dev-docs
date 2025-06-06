# isFinished

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates the progress object is complete.

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
var isFinished: Bool { get }
```

#### Discussion

A progress object finishes when the [`completedUnitCount`](progress/completedunitcount.md) equals or exceeds the [`totalUnitCount`](progress/totalunitcount.md).

By default, [`Progress`](progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

- [var isIndeterminate: Bool](progress/isindeterminate.md)
  A Boolean value that indicates whether the tracked progress is indeterminate.
- [var fractionCompleted: Double](progress/fractioncompleted.md)
  The fraction of the overall work that the progress object completes, including work from its suboperations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/isfinished)*