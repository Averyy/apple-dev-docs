# UIPointerInteraction

**Framework**: Uikit  
**Kind**: class

An interaction that enables support for effects on a view or customizes the pointer’s appearance within a region of an app.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPointerInteraction
```

#### Overview

If you use a [`UIButton`](uibutton.md) as an interface object, use the button’s [`isPointerInteractionEnabled`](uibutton/ispointerinteractionenabled.md) and [`pointerStyleProvider`](uibutton/pointerstyleprovider-1d4d2.md) to customize the proposed effect before constructing your own custom pointer effect using a [`UIPointerInteraction`](uipointerinteraction.md).

> **Note**:  In iPadOS, the visual interactions when using mouse or trackpad input versus Apple Pencil input are slightly different: For example, pointer styles such as the system pointer aren’t visible while using Apple Pencil. However, both input devices support effect-based pointers, but have a slightly different visual appearance depending on which device is in use.

## Topics

### Create pointer interactions
- [init(delegate: (any UIPointerInteractionDelegate)?)](uipointerinteraction/init(delegate:).md)
  Initializes a pointer interaction object with a specified delegate object.
### Manage pointer interactions
- [var delegate: (any UIPointerInteractionDelegate)?](uipointerinteraction/delegate.md)
  An object that responds to pointer movements.
- [protocol UIPointerInteractionDelegate](uipointerinteractiondelegate.md)
  An interface for handling pointer movements within the interaction’s view.
### Activate pointer interactions
- [var isEnabled: Bool](uipointerinteraction/isenabled.md)
  A Boolean value that indicates whether the pointer interaction is an enabled state.
### Trigger a pointer update
- [func invalidate()](uipointerinteraction/invalidate.md)
  Causes the interaction to update the pointer in response to an event.

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
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [protocol UIPointerInteractionDelegate](uipointerinteractiondelegate.md)
  An interface for handling pointer movements within the interaction’s view.
- [Integrating pointer interactions into your iPad app](integrating-pointer-interactions-into-your-ipad-app.md)
  Support touch interactions in your iPad app by adding pointer interactions to your views.
- [Enhancing your iPad app with pointer interactions](enhancing-your-ipad-app-with-pointer-interactions.md)
  Provide a great user experience with pointing devices, by incorporating pointer content effects and shape customizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uipointerinteraction)*