# resignCurrent()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Restores the previous progress object to become the current progress object on the thread.

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
func resignCurrent()
```

```objc
- (void) resignCurrent;
```

#### Discussion

This method restores the current progress object to what it was before invoking [`becomeCurrent(withPendingUnitCount:)`](./becomecurrent%28withpendingunitcount%29.md).

Use this method after building your tree of progress objects, as [Reporting Progress for Multiple Operations](../progress.md#Reporting-Progress-for-Multiple-Operations) describes.

## See Also

### Accessing the Current Progress Object
- [class func current() -> Progress?](./current%28%29.md)
  Returns the progress instance, if any.
- [func becomeCurrent(withPendingUnitCount: Int64)](./becomecurrent%28withpendingunitcount%29.md)
  Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [func performAsCurrent<ReturnType>(withPendingUnitCount: Int64, using: () throws -> ReturnType) rethrows -> ReturnType](./performascurrent%28withpendingunitcount,using%29.md)
  Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.
- [- performAsCurrentWithPendingUnitCount:usingBlock:](../nsprogress/performascurrentwithpendingunitcount_usingblock_.md)
  Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/resigncurrent())*