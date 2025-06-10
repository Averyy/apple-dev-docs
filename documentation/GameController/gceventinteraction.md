# GCEventInteraction

**Framework**: Game Controller  
**Kind**: class

An interaction that indicates the view’s intent to receive game controller events through the Game Controller framework.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
class GCEventInteraction
```

#### Overview

On visionOS, users can interact with your app using a game controller. By default, the system converts game controller actions into pinch events and sends them to the view the user is gazing at, its gesture recognizers, and then up the responder chain.

If you use the Game Controller framework to handle game controller events for part of your user interface, add an instance of `GCEventInteraction` to the root of that part of your app’s view hierarchy.  For example, if you are writing a game using Metal, add this interaction to the view that hosts your game’s `CAMetalLayer`.

> **Note**: This class should not be subclassed.

## Topics

### Creating an interaction
- [init()](gceventinteraction/init.md)
### Receiving view events
- [var receivesEventsInView: Bool](gceventinteraction/receiveseventsinview.md)
  A Boolean value that determines whether events are delivered exclusively through the Game Controller framework.
- [struct GameControllerEventHandlingOptions](gamecontrollereventhandlingoptions.md)
### Getting the event types
- [var handledEventTypes: GCUIEventTypes](gceventinteraction/handledeventtypes.md)
  The types of game controller events that should be delivered through the Game Controller framework.
- [struct GCUIEventTypes](gcuieventtypes.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIInteraction](../UIKit/UIInteraction.md)

## See Also

- [var controllerPausedHandler: ((GCController) -> Void)?](gccontroller/controllerpausedhandler.md)
  The block that the framework calls when the user presses the pause button on the controller.
- [protocol GCGameControllerSceneDelegate](gcgamecontrollerscenedelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gceventinteraction)*