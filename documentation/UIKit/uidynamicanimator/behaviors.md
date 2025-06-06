# behaviors

**Framework**: UIKit  
**Kind**: property

The dynamic behaviors managed by a dynamic animator.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var behaviors: [UIDynamicBehavior] { get }
```

## See Also

- [var elapsedTime: TimeInterval](uidynamicanimator/elapsedtime.md)
  Returns the time interval since the dynamic animator started running.
- [var isRunning: Bool](uidynamicanimator/isrunning.md)
  Returns true if the dynamic animator is running.
- [var referenceView: UIView?](uidynamicanimator/referenceview.md)
  The view that a dynamic animator was initialized with.
- [func updateItem(usingCurrentState: any UIDynamicItem)](uidynamicanimator/updateitem(usingcurrentstate:).md)
  Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/behaviors)*