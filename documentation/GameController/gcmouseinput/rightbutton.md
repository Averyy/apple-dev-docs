# rightButton

**Framework**: Game Controller  
**Kind**: property

The optional right button on the mouse.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var rightButton: GCControllerButtonInput? { get }
```

#### Discussion

If the mouse doesn’t have a right button, this property is `nil`.

## See Also

- [var leftButton: GCControllerButtonInput](gcmouseinput/leftbutton.md)
  The left button on the mouse.
- [var middleButton: GCControllerButtonInput?](gcmouseinput/middlebutton.md)
  The optional middle button on the mouse.
- [var auxiliaryButtons: [GCControllerButtonInput]?](gcmouseinput/auxiliarybuttons.md)
  The optional additional buttons on the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouseinput/rightbutton)*