# UIPressesEvent

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An event that describes the state of a set of physical buttons that are available to the device, such as those on an associated remote or game controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPressesEvent
```

```objc
@interface UIPressesEvent : UIEvent
```

## Topics

### Reading the event button presses
- [var allPresses: Set<UIPress>](./uipressesevent/allpresses.md)
  The state of all physical buttons in the event.
- [func presses(for: UIGestureRecognizer) -> Set<UIPress>](./uipressesevent/presses%28for%29.md)
  Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.

## Relationships

### Inherits From
- [UIEvent](./uievent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Button presses
- [class UIPress](./uipress.md)
  An object that represents the presence or movement of a button press on the screen for a particular event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipressesevent)*