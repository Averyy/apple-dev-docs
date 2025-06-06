# addChild(_:withPendingUnitCount:)

**Framework**: Foundation  
**Kind**: method

Adds a process object as a suboperation of a progress tree.

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
func addChild(_ child: Progress, withPendingUnitCount inUnitCount: Int64)
```

#### Discussion

You assign the suboperation a portion of the receiver’s total unit count according to `inUnitCount`. For more information, see [`Reporting Progress for Multiple Operations`](progress#Reporting-Progress-for-Multiple-Operations.md).

## Parameters

- `child`: The progress instance to add to the progress tree.
- `inUnitCount`: The number of units of work for the new suboperation to complete.

## See Also

- [class func current() -> Progress?](progress/current.md)
  Returns the progress instance, if any.
- [func becomeCurrent(withPendingUnitCount: Int64)](progress/becomecurrent(withpendingunitcount:).md)
  Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [func performAsCurrent<ReturnType>(withPendingUnitCount: Int64, using: () throws -> ReturnType) rethrows -> ReturnType](progress/performascurrent(withpendingunitcount:using:).md)
  Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.
- [func resignCurrent()](progress/resigncurrent.md)
  Restores the previous progress object to become the current progress object on the thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/addchild(_:withpendingunitcount:))*