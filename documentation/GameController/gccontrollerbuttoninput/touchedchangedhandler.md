# touchedChangedHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The block that the element calls when the user touches the button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var touchedChangedHandler: GCControllerButtonTouchedChangedHandler? { get set }
```

```objc
@property (nonatomic, copy, nullable) GCControllerButtonTouchedChangedHandler touchedChangedHandler;
```

## Discussion

Set this handler when you want to know when the user touches the button before pressing the button.

## See Also

### Getting change information
- [typealias GCControllerButtonTouchedChangedHandler](../gccontrollerbuttontouchedchangedhandler.md)
  The signature for the block that executes when the user touches the button if the controller supports that feature.
- [var pressedChangedHandler: GCControllerButtonValueChangedHandler?](./pressedchangedhandler.md)
  The block that the element calls when the user presses or releases the button.
- [var valueChangedHandler: GCControllerButtonValueChangedHandler?](./valuechangedhandler.md)
  The block that the element calls when the user changes the level of pressure on the button.
- [typealias GCControllerButtonValueChangedHandler](../gccontrollerbuttonvaluechangedhandler.md)
  The signature for the block that executes when a button’s state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/touchedchangedhandler)*