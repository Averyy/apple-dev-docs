# resignCurrent()

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

This method restores the current progress object to what it was before invoking [`becomeCurrent(withPendingUnitCount:)`](progress/becomecurrent(withpendingunitcount:).md).

Use this method after building your tree of progress objects, as [`Reporting Progress for Multiple Operations`](progress#Reporting-Progress-for-Multiple-Operations.md) describes.

## See Also

- [class func current() -> Progress?](progress/current.md)
  Returns the progress instance, if any.
- [func becomeCurrent(withPendingUnitCount: Int64)](progress/becomecurrent(withpendingunitcount:).md)
  Sets the progress object as the current object of the current thread, and assigns the amount of work for the next suboperation progress object to perform.
- [func addChild(Progress, withPendingUnitCount: Int64)](progress/addchild(_:withpendingunitcount:).md)
  Adds a process object as a suboperation of a progress tree.
- [func performAsCurrent<ReturnType>(withPendingUnitCount: Int64, using: () throws -> ReturnType) rethrows -> ReturnType](progress/performascurrent(withpendingunitcount:using:).md)
  Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/resigncurrent())*