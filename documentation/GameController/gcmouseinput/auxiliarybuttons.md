# auxiliaryButtons

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The optional additional buttons on the mouse.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var auxiliaryButtons: [GCControllerButtonInput]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<GCControllerButtonInput *> * auxiliaryButtons;
```

## Discussion

If the mouse doesn’t have additional buttons, this property is `nil`.

## See Also

### Accessing Buttons
- [var leftButton: GCControllerButtonInput](./leftbutton.md)
  The left button on the mouse.
- [var rightButton: GCControllerButtonInput?](./rightbutton.md)
  The optional right button on the mouse.
- [var middleButton: GCControllerButtonInput?](./middlebutton.md)
  The optional middle button on the mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouseinput/auxiliarybuttons)*