# updateItem(usingCurrentState:)

**Framework**: UIKit  
**Kind**: method

Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func updateItem(usingCurrentState item: any UIDynamicItem)
```

#### Discussion

A dynamic animator automatically reads the initial state (position and rotation) of each dynamic item you add to it, and then takes responsibility for updating the item’s state. If you actively change the state of a dynamic item  you’ve added it to a dynamic animator, call this method to ask the animator to read and incorporate the new state.

## Parameters

- `item`: The dynamic item whose state was changed by your app.

## See Also

- [var elapsedTime: TimeInterval](uidynamicanimator/elapsedtime.md)
  Returns the time interval since the dynamic animator started running.
- [var isRunning: Bool](uidynamicanimator/isrunning.md)
  Returns true if the dynamic animator is running.
- [var behaviors: [UIDynamicBehavior]](uidynamicanimator/behaviors.md)
  The dynamic behaviors managed by a dynamic animator.
- [var referenceView: UIView?](uidynamicanimator/referenceview.md)
  The view that a dynamic animator was initialized with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/updateitem(usingcurrentstate:))*