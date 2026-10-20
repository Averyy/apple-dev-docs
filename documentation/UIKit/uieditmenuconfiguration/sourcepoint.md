# sourcePoint

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The source location of the interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var sourcePoint: CGPoint { get }
```

```objc
@property (nonatomic, assign, readonly) CGPoint sourcePoint;
```

#### Discussion

The system derives the suggested actions list from this point in the interaction’s view. By default, the menu also presents from this location. You can change the presentation source of the menu by implementing the delegate method [`editMenuInteraction(_:targetRectFor:)`](../uieditmenuinteractiondelegate/editmenuinteraction%28_,targetrectfor%29.md).

## See Also

### Configuring the menu
- [var preferredArrowDirection: UIEditMenuArrowDirection](./preferredarrowdirection.md)
  The preferred direction the arrow of the edit menu is pointing.
- [enum UIEditMenuArrowDirection](../uieditmenuarrowdirection.md)
  Constants that describe the direction the arrow of the edit menu is pointing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuconfiguration/sourcepoint)*