# performAsCurrentWithPendingUnitCount:usingBlock:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```objc
- (void) performAsCurrentWithPendingUnitCount:(int64_t) unitCount usingBlock:(void (^)()) work;
```

## Discussion

Use this function as a convenience method to wrap an existing method or block to increment the current progress object. This function retrieves the current progress object, does the work you specify in the block. When the block is complete, this function increments the current progress object. This function is the same as calling [`becomeCurrent(withPendingUnitCount:)`](../progress/becomecurrent%28withpendingunitcount%29.md), doing the work you specify in the block, and calling [`resignCurrent()`](../progress/resigncurrent%28%29.md).

## See Also

### Accessing the Current Progress Object
- [class func current() -> Progress?](../progress/current%28%29.md)
  Returns the progress instance, if any.
- [func becomeCurrent(withPendingUnitCount: Int64)](../progress/becomecurrent%28withpendingunitcount%29.md)
  Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [func resignCurrent()](../progress/resigncurrent%28%29.md)
  Restores the previous progress object to become the current progress object on the thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsprogress/performascurrentwithpendingunitcount:usingblock:)*