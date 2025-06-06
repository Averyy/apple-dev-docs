# isRunning

**Framework**: UIKit  
**Kind**: property

Returns true if the dynamic animator is running.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var isRunning: Bool { get }
```

#### Discussion

The views associated with an animator’s behaviors can change position or change transform only when the animator is running. For optimization purposes, iOS can pause and then restart an animator. Use this method if you need to check whether or not your views are currently subject to changes in position or transform.

## See Also

- [var elapsedTime: TimeInterval](uidynamicanimator/elapsedtime.md)
  Returns the time interval since the dynamic animator started running.
- [var behaviors: [UIDynamicBehavior]](uidynamicanimator/behaviors.md)
  The dynamic behaviors managed by a dynamic animator.
- [var referenceView: UIView?](uidynamicanimator/referenceview.md)
  The view that a dynamic animator was initialized with.
- [func updateItem(usingCurrentState: any UIDynamicItem)](uidynamicanimator/updateitem(usingcurrentstate:).md)
  Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/isrunning)*