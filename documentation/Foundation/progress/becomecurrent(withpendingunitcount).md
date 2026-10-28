# becomeCurrent(withPendingUnitCount:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.

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
func becomeCurrent(withPendingUnitCount unitCount: Int64)
```

```objc
- (void) becomeCurrentWithPendingUnitCount:(int64_t) unitCount;
```

## Discussion

Use this method to build a tree of progress objects, as [Reporting Progress for Multiple Operations](../progress.md#Reporting-Progress-for-Multiple-Operations) describes.

## Parameters

- `unitCount`: The number of units of work for the next progress object that initializes when you invoke [`init(parent:userInfo:)`](./init%28parent,userinfo%29.md) in the current thread with this progress object as the containing progress object.

  The number represents the portion of work to perform in relation to the total number of units of work, which is the value of the progress object’s [`totalUnitCount`](./totalunitcount.md) property. The units of work for this parameter must be the same units of work in the progress object’s [`totalUnitCount`](./totalunitcount.md) property.

## See Also

### Accessing the Current Progress Object
- [class func current() -> Progress?](./current%28%29.md)
  Returns the progress instance, if any.
- [func performAsCurrent<ReturnType>(withPendingUnitCount: Int64, using: () throws -> ReturnType) rethrows -> ReturnType](./performascurrent%28withpendingunitcount,using%29.md)
  Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.
- [func resignCurrent()](./resigncurrent%28%29.md)
  Restores the previous progress object to become the current progress object on the thread.
- [- performAsCurrentWithPendingUnitCount:usingBlock:](../nsprogress/performascurrentwithpendingunitcount_usingblock_.md)
  Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/becomecurrent(withpendingunitcount:))*