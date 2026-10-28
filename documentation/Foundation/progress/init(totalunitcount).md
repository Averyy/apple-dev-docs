# init(totalUnitCount:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and returns a progress instance.

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
init(totalUnitCount unitCount: Int64)
```

```objc
+ (NSProgress *) progressWithTotalUnitCount:(int64_t) unitCount;
```

## Discussion

If a current progress object exists, the initializer uses it to set the value of the [`totalUnitCount`](./totalunitcount.md) property.

In many cases, you can precede code that does a substantial amount of work with an invocation of this method, then repeatedly set the [`completedUnitCount`](./completedunitcount.md) or [`isCancelled`](./iscancelled.md) property in the loop that does the work.

You can invoke this method on one thread and then message the returned [`Progress`](../progress.md) on another thread. For example, you can capture the created progress instance in a block that you pass to [`dispatch_async`](../../Dispatch/dispatch_async.md). In that block, you can invoke methods like [`becomeCurrent(withPendingUnitCount:)`](./becomecurrent%28withpendingunitcount%29.md) or [`resignCurrent()`](./resigncurrent%28%29.md), and set the [`completedUnitCount`](./completedunitcount.md) or [`isCancelled`](./iscancelled.md) properties as your app finishes its work.

## Parameters

- `unitCount`: The total number of units of work to assign to the progress instance.

## See Also

### Creating Progress Objects
- [init(parent: Progress?, userInfo: [ProgressUserInfoKey : Any]?)](./init%28parent,userinfo%29.md)
  Creates a new progress instance.
- [class func discreteProgress(totalUnitCount: Int64) -> Progress](./discreteprogress%28totalunitcount%29.md)
  Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.
- [init(totalUnitCount: Int64, parent: Progress, pendingUnitCount: Int64)](./init%28totalunitcount,parent,pendingunitcount%29.md)
  Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/init(totalunitcount:))*