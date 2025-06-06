# sourcePoint

**Framework**: UIKit  
**Kind**: property

The source location of the interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourcePoint: CGPoint { get }
```

#### Discussion

The system derives the suggested actions list from this point in the interaction’s view. By default, the menu also presents from this location. You can change the presentation source of the menu by implementing the delegate method [`editMenuInteraction(_:targetRectFor:)`](uieditmenuinteractiondelegate/editmenuinteraction(_:targetrectfor:).md).

## See Also

- [var preferredArrowDirection: UIEditMenuArrowDirection](uieditmenuconfiguration/preferredarrowdirection.md)
  The preferred direction the arrow of the edit menu is pointing.
- [enum UIEditMenuArrowDirection](uieditmenuarrowdirection.md)
  Constants that describe the direction the arrow of the edit menu is pointing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuconfiguration/sourcepoint)*