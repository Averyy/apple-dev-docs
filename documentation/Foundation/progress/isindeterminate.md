# isIndeterminate

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the tracked progress is indeterminate.

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
var isIndeterminate: Bool { get }
```

#### Discussion

Use [`isIndeterminate`](progress/isindeterminate.md) progress only when you’re unable to determine a reasonable value for either [`completedUnitCount`](progress/completedunitcount.md) or [`totalUnitCount`](progress/totalunitcount.md). Progress is indeterminate when the value of the [`totalUnitCount`](progress/totalunitcount.md) or [`completedUnitCount`](progress/completedunitcount.md) is less than zero or if both values are zero. When progress is indeterminate, [`fractionCompleted`](progress/fractioncompleted.md) returns `0.0` and [`isFinished`](progress/isfinished.md) returns `false`.

By default, [`Progress`](progress.md) is KVO-compliant for this property. It sends notifications on the same thread that updates the property.

The following code snippet clarifies the behavior for setting both [`totalUnitCount`](progress/totalunitcount.md) and [`completedUnitCount`](progress/completedunitcount.md) to `0`.

```swift
let progress = Progress(totalUnitCount: 0) 
progress.completedUnitCount = 0 // default 
print("totalUnitCount: (progress.totalUnitCount)") 
print("completedUnitCount: (progress.completedUnitCount)") 
print("isIndeterminate: (progress.isIndeterminate)") 
print("fractionCompleted: (progress.fractionCompleted)") 
print("isFinished: (progress.isFinished)")
/*
Code Output:
totalUnitCount: 0 completedUnitCount: 0 isIndeterminate: true fractionCompleted: 0.0 isFinished: false
*/
```

## See Also

- [var fractionCompleted: Double](progress/fractioncompleted.md)
  The fraction of the overall work that the progress object completes, including work from its suboperations.
- [var isFinished: Bool](progress/isfinished.md)
  A Boolean value that indicates the progress object is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/isindeterminate)*