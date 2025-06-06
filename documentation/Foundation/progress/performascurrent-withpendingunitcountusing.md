# performAsCurrent(withPendingUnitCount:using:)

**Framework**: Foundation  
**Kind**: method

Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func performAsCurrent<ReturnType>(withPendingUnitCount unitCount: Int64, using work: () throws -> ReturnType) rethrows -> ReturnType
```

#### Return Value

The return type and value of the block that you specify for the `work` parameter.

#### Discussion

Use this function as a convenience method to wrap an existing method or block to increment the current progress object. This function retrieves the current progress object, does the work you specify in the work block, and returns the value from that block. When the block is complete, this function increments the current progress object. This function is the same as calling [`becomeCurrent(withPendingUnitCount:)`](progress/becomecurrent(withpendingunitcount:).md), doing the work you specify in the block, and calling [`resignCurrent()`](progress/resigncurrent().md).

## Parameters

- `unitCount`: The number of units of work to increment for the current progress object. This number represents the portion of work that is complete in relation to the total number of units of work for the current thread’s progress object. The units of work for this parameter must be the same units of work as the current progress object’s   property.
- `work`: A block that wraps the work you specify to complete for incrementing the current progress.

## See Also

- [class func current() -> Progress?](progress/current.md)
  Returns the progress instance, if any.
- [func becomeCurrent(withPendingUnitCount: Int64)](progress/becomecurrent(withpendingunitcount:).md)
  Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [func addChild(Progress, withPendingUnitCount: Int64)](progress/addchild(_:withpendingunitcount:).md)
  Adds a process object as a suboperation of a progress tree.
- [func resignCurrent()](progress/resigncurrent.md)
  Restores the previous progress object to become the current progress object on the thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/performascurrent(withpendingunitcount:using:))*