# becomeCurrent(withPendingUnitCount:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

Use this method to build a tree of progress objects, as [`Reporting Progress for Multiple Operations`](progress#Reporting-Progress-for-Multiple-Operations.md) describes.

## Parameters

- `unitCount`: The number represents the portion of work to perform in relation to the total number of units of work, which is the value of the progress object’s   property. The units of work for this parameter must be the same units of work in the progress object’s   property.

## See Also

- [class func current() -> Progress?](progress/current.md)
  Returns the progress instance, if any.
- [func addChild(Progress, withPendingUnitCount: Int64)](progress/addchild(_:withpendingunitcount:).md)
  Adds a process object as a suboperation of a progress tree.
- [func performAsCurrent<ReturnType>(withPendingUnitCount: Int64, using: () throws -> ReturnType) rethrows -> ReturnType](progress/performascurrent(withpendingunitcount:using:).md)
  Retrieves the current thread’s progress object, executes the specified block, and increments the progress object by the specified units of work.
- [func resignCurrent()](progress/resigncurrent.md)
  Restores the previous progress object to become the current progress object on the thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/becomecurrent(withpendingunitcount:))*