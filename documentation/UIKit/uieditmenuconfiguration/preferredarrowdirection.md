# preferredArrowDirection

**Framework**: UIKit  
**Kind**: property

The preferred direction the arrow of the edit menu is pointing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredArrowDirection: UIEditMenuArrowDirection { get set }
```

#### Discussion

The default, [`UIEditMenuArrowDirection.automatic`](uieditmenuarrowdirection/automatic.md), is an arrow pointing up or down at the object of focus, based on its location in the screen.

## See Also

- [enum UIEditMenuArrowDirection](uieditmenuarrowdirection.md)
  Constants that describe the direction the arrow of the edit menu is pointing.
- [var sourcePoint: CGPoint](uieditmenuconfiguration/sourcepoint.md)
  The source location of the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuconfiguration/preferredarrowdirection)*