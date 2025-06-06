# init(totalUnitCount:parent:pendingUnitCount:)

**Framework**: Foundation  
**Kind**: init

Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(totalUnitCount unitCount: Int64, parent: Progress, pendingUnitCount portionOfParentTotalUnitCount: Int64)
```

#### Discussion

Use this method to initialize a progress object with a specified containing progress object and unit count.

In many cases, you can precede code that does a substantial amount of work with an invocation of this method, then repeatedly set the [`completedUnitCount`](progress/completedunitcount.md) or [`isCancelled`](progress/iscancelled.md) property in the loop that does the work.

You can invoke this method on one thread and then message the returned [`Progress`](progress.md) on another thread. For example, you can capture the created progress instance in a block that you pass to [`dispatch_async`](https://developer.apple.com/documentation/dispatch/1453057-dispatch_async). In that block, you can invoke methods like [`becomeCurrent(withPendingUnitCount:)`](progress/becomecurrent(withpendingunitcount:).md) or [`resignCurrent()`](progress/resigncurrent().md), and set the [`completedUnitCount`](progress/completedunitcount.md) or [`isCancelled`](progress/iscancelled.md) properties as your app finishes its work.

## Parameters

- `unitCount`: The total number of units of work to assign to the progress instance.
- `parent`: The containing progress object for the created   object.
- `portionOfParentTotalUnitCount`: The unit count for the progress object.

## See Also

- [init(parent: Progress?, userInfo: [ProgressUserInfoKey : Any]?)](progress/init(parent:userinfo:).md)
  Creates a new progress instance.
- [class func discreteProgress(totalUnitCount: Int64) -> Progress](progress/discreteprogress(totalunitcount:).md)
  Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.
- [init(totalUnitCount: Int64)](progress/init(totalunitcount:).md)
  Creates and returns a progress instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/init(totalunitcount:parent:pendingunitcount:))*