# valueChangedHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The block that the element calls when the user changes the level of pressure on the button.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var valueChangedHandler: GCControllerButtonValueChangedHandler? { get set }
```

```objc
@property (nonatomic, copy, nullable) GCControllerButtonValueChangedHandler valueChangedHandler;
```

## Discussion

Set this handler when you want to know when the pressure level changes.

## See Also

### Getting change information
- [var touchedChangedHandler: GCControllerButtonTouchedChangedHandler?](./touchedchangedhandler.md)
  The block that the element calls when the user touches the button.
- [typealias GCControllerButtonTouchedChangedHandler](../gccontrollerbuttontouchedchangedhandler.md)
  The signature for the block that executes when the user touches the button if the controller supports that feature.
- [var pressedChangedHandler: GCControllerButtonValueChangedHandler?](./pressedchangedhandler.md)
  The block that the element calls when the user presses or releases the button.
- [typealias GCControllerButtonValueChangedHandler](../gccontrollerbuttonvaluechangedhandler.md)
  The signature for the block that executes when a button’s state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/valuechangedhandler)*