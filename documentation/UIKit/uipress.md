# UIPress

**Framework**: UIKit  
**Kind**: class

An object that represents the presence or movement of a button press on the screen for a particular event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class UIPress
```

#### Overview

The press specifically encapsulates the pressing of some physically actuated button. All of the press types represent actual physical buttons on one of a variety of remotes. You access [`UIPress`](uipress.md) objects through [`UIEvent`](uievent.md) objects passed into responder objects for event handling. The [`gestureRecognizers`](uipress/gesturerecognizers.md) property returns the gesture recognizers — instances of a concrete subclass of [`UIGestureRecognizer`](uigesturerecognizer.md) — that are currently handling the given button press.

## Topics

### Getting a press object’s gesture recognizers
- [var force: CGFloat](uipress/force.md)
  The force of the button press.
- [var gestureRecognizers: [UIGestureRecognizer]?](uipress/gesturerecognizers.md)
  The gesture recognizers that are receiving the press.
### Responding to press events
- [var responder: UIResponder?](uipress/responder.md)
  A responder object.
### Getting the press’s location
- [var window: UIWindow?](uipress/window.md)
  The window in which the press initially occurred.
### Getting press attributes
- [var key: UIKey?](uipress/key.md)
  The key pressed or released on a physical keyboard.
- [var type: UIPress.PressType](uipress/type.md)
  The type of the specified press.
- [var phase: UIPress.Phase](uipress/phase-swift.property.md)
  The current press phase of the object.
- [var timestamp: TimeInterval](uipress/timestamp.md)
  The time when the press occurred or when it was last mutated.
### Constants
- [UIPress.Phase](uipress/phase-swift.enum.md)
  Constants that represent the phases of a button press.
- [UIPress.PressType](uipress/presstype.md)
  Constants that represent buttons that a person can press.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIPressesEvent](uipressesevent.md)
  An event that describes the state of a set of physical buttons that are available to the device, such as those on an associated remote or game controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress)*