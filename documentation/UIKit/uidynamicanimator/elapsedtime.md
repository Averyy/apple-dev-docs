# elapsedTime

**Framework**: UIKit  
**Kind**: property

Returns the time interval since the dynamic animator started running.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var elapsedTime: TimeInterval { get }
```

#### Return Value

The elapsed time since the dynamic animator started running.

## See Also

- [var isRunning: Bool](uidynamicanimator/isrunning.md)
  Returns true if the dynamic animator is running.
- [var behaviors: [UIDynamicBehavior]](uidynamicanimator/behaviors.md)
  The dynamic behaviors managed by a dynamic animator.
- [var referenceView: UIView?](uidynamicanimator/referenceview.md)
  The view that a dynamic animator was initialized with.
- [func updateItem(usingCurrentState: any UIDynamicItem)](uidynamicanimator/updateitem(usingcurrentstate:).md)
  Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/elapsedtime)*