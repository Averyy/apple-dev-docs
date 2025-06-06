# GCControllerElement

**Framework**: Game Controller  
**Kind**: class

An input for a physical control, such as a button or thumbstick.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCControllerElement
```

#### Overview

`GCControllerElement` is an abstract superclass for specific types of elements that represent controls on a game controller. Use the respective subclasses to either get the input of an element directly or set a handler that the element calls when the user changes a value. This class provides support for common features.

For complex elements that have subelements, you can get the containing element using the [`collection`](gccontrollerelement/collection.md) property. For example, a direction pad ([`GCControllerDirectionPad`](gccontrollerdirectionpad.md)) has two axis control and four button subelements.

If the user binds a controller element to a system gesture, the system sends the input to the system gesture recognizer first. If it doesn’t recognize a gesture, the system sends the input to your app but with a delay. If it does recognize a gesture, it doesn’t send any input to your app.

To change this default behavior, you can set the [`preferredSystemGestureState`](gccontrollerelement/preferredsystemgesturestate.md) property to [`GCControllerElement.SystemGestureState.alwaysReceive`](gccontrollerelement/systemgesturestate/alwaysreceive.md) to receive the input simultaneously without delay. Alternatively, set it to [`GCControllerElement.SystemGestureState.disabled`](gccontrollerelement/systemgesturestate/disabled.md) to disable the system gesture and receive the input exclusively. Use the [`isBoundToSystemGesture`](gccontrollerelement/isboundtosystemgesture.md) property to check whether the user included an element in a system gesture.

Use the [`isAnalog`](gccontrollerelement/isanalog.md) property to determine whether an element’s input value is a range of values or a discrete digital value.

## Topics

### Accessing input values
- [var isAnalog: Bool](gccontrollerelement/isanalog.md)
  A Boolean value that indicates whether the element provides analog data.
### Getting a localized name
- [var localizedName: String?](gccontrollerelement/localizedname.md)
  The localized name for the element or the remapped element.
- [var unmappedLocalizedName: String?](gccontrollerelement/unmappedlocalizedname.md)
  The element’s localized name, not the remapped name.
### Displaying a symbol
- [var sfSymbolsName: String?](gccontrollerelement/sfsymbolsname.md)
  A system symbol for the element or the remapped element.
- [var unmappedSfSymbolsName: String?](gccontrollerelement/unmappedsfsymbolsname.md)
  The element’s system symbol, not the remapped symbol.
### Accessing elements by key
- [var aliases: Set<String>](gccontrollerelement/aliases.md)
  The element’s aliases you use when accessing it with the subscript notation.
### Getting the containing element
- [var collection: GCControllerElement?](gccontrollerelement/collection.md)
  The enclosing element for this element.
### Handling system gesture input
- [var isBoundToSystemGesture: Bool](gccontrollerelement/isboundtosystemgesture.md)
  A Boolean value that indicates whether the user binds the element to a system gesture.
- [var preferredSystemGestureState: GCControllerElement.SystemGestureState](gccontrollerelement/preferredsystemgesturestate.md)
  The preferred state for handling input when the user binds the element to a system gesture.
- [GCControllerElement.SystemGestureState](gccontrollerelement/systemgesturestate.md)
  A state for handling input when an element is part of a system gesture.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GCControllerAxisInput](gccontrolleraxisinput.md)
- [GCControllerButtonInput](gccontrollerbuttoninput.md)
- [GCControllerDirectionPad](gccontrollerdirectionpad.md)
- [GCControllerTouchpad](gccontrollertouchpad.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCControllerAxisInput](gccontrolleraxisinput.md)
  A control element that tracks movement along an axis.
- [class GCControllerButtonInput](gccontrollerbuttoninput.md)
  A control element that represents a button touch or press.
- [class GCControllerTouchpad](gccontrollertouchpad.md)
  A control element that represents a touch event on a touchpad.
- [class GCControllerDirectionPad](gccontrollerdirectionpad.md)
  A control element associated with a directional pad or a thumbstick.
- [class GCDeviceCursor](gcdevicecursor.md)
  A control element for the cursor used as a directional pad.
- [class GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
  A class that encapsulates the features of a DualSense adaptive trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement)*