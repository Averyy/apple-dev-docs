# UIPressesEvent

**Framework**: UIKit  
**Kind**: class

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

## Topics

### Reading the event button presses
- [var allPresses: Set<UIPress>](uipressesevent/allpresses.md)
  The state of all physical buttons in the event.
- [func presses(for: UIGestureRecognizer) -> Set<UIPress>](uipressesevent/presses(for:).md)
  Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.

## Relationships

### Inherits From
- [UIEvent](uievent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIPress](uipress.md)
  An object that represents the presence or movement of a button press on the screen for a particular event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipressesevent)*