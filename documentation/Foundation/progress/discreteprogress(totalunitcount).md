# discreteProgress(totalUnitCount:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a progress instance with the specified unit count that isn’t part of any existing progress tree.

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
class func discreteProgress(totalUnitCount unitCount: Int64) -> Progress
```

```objc
+ (NSProgress *) discreteProgressWithTotalUnitCount:(int64_t) unitCount;
```

#### Return Value

A new progress instance with its containing progress object set to `nil.`

#### Discussion

Use this method to create the top-level progress object that your custom classes return. The receiver of the returned progress object can add it to a progress tree using `Progress/addChild(_:withPendingUnitCount:)`.

You’re responsible for updating the progress count of the created progress object. You can invoke this method on one thread and then message the returned `NSProgress` on another thread. For example, you can capture the created progress instance in a block that you pass to [`dispatch_async`](../../Dispatch/dispatch_async.md). In that block, you can invoke methods like [`becomeCurrent(withPendingUnitCount:)`](./becomecurrent%28withpendingunitcount%29.md) or [`resignCurrent()`](./resigncurrent%28%29.md), and set the [`completedUnitCount`](./completedunitcount.md) or [`isCancelled`](./iscancelled.md) properties as your app finishes its work.

## Parameters

- `unitCount`: The total number of units of work to assign to the progress instance.

## See Also

### Creating Progress Objects
- [init(parent: Progress?, userInfo: [ProgressUserInfoKey : Any]?)](./init%28parent,userinfo%29.md)
  Creates a new progress instance.
- [init(totalUnitCount: Int64)](./init%28totalunitcount%29.md)
  Creates and returns a progress instance.
- [init(totalUnitCount: Int64, parent: Progress, pendingUnitCount: Int64)](./init%28totalunitcount,parent,pendingunitcount%29.md)
  Creates a progress instance for the specified progress object with a unit count that’s a portion of the containing object’s total unit count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/discreteprogress(totalunitcount:))*