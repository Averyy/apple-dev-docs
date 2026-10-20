# isFinished

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isFinished) BOOL finished;
```

#### Discussion

A progress object finishes when the [`completedUnitCount`](./completedunitcount.md) equals or exceeds the [`totalUnitCount`](./totalunitcount.md).

By default, [`Progress`](../progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

## See Also

### Observing Progress
- [var isIndeterminate: Bool](./isindeterminate.md)
  A Boolean value that indicates whether the tracked progress is indeterminate.
- [var fractionCompleted: Double](./fractioncompleted.md)
  The fraction of the overall work that the progress object completes, including work from its suboperations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/isfinished)*