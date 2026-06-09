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

You assign the suboperation a portion of the receiver’s total unit count according to `inUnitCount`.

## Parameters

- `child`: The progress instance to add to the progress tree.
- `inUnitCount`: The number of units of work for the new suboperation to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/addchild(_:withpendingunitcount:)-9yrs3)*