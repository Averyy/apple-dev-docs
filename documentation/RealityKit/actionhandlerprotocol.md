# ActionHandlerProtocol

**Framework**: RealityKit  
**Kind**: protocol

The base protocol for action handlers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol ActionHandlerProtocol
```

#### Overview

One of two approaches can be taken when subscribing to, and responding to action events. Which approach is taken is dictated by complexity of the action, and user preference.

The simplest approach is to process action events using an external closure. This saves having to define a formal handler for the action. For example:

```swift
struct MyAction: EntityAction {
    ...
}
MyAction.subscribe(to: .started) { event in
    let action = event.action
    // Do something with the action.
}
```

The other approach is to use a formal handler. This requires defining a structure for the handler that conforms to the `ActionHandlerProtocol` and registering the handler so it can be instantiated when the action animation is played. It is only necessary to define the event functions for the event types that one wishes to respond to.

For example:

```swift
struct MyAction: EntityAction { }

struct MyActionHandler: ActionHandlerProtocol {

   typealias ActionType = MyAction

   // Application data can be stored within the handler.
   var applicationData: ApplicationData

   // Customizable init
   init(action: MyAction, player: Entity, currentLevel: Int) { ... }

   // Process start events
   mutating func actionStarted(event: EventType) { }
}

MyActionHandler.register { event in
    // Create the handler.
    return MyActionHandler(applicationData: appData)
}
```

## Topics

### Associated Types
- [associatedtype ActionType : EntityAction](actionhandlerprotocol/actiontype.md)
  The action type associated that is associated with the handler.
### Instance Methods
- [func actionEnded(event: Self.EventType)](actionhandlerprotocol/actionended(event:).md)
  The function used to respond to action ended events.
- [func actionPaused(event: Self.EventType)](actionhandlerprotocol/actionpaused(event:).md)
  The function used to respond to action paused events.
- [func actionResumed(event: Self.EventType)](actionhandlerprotocol/actionresumed(event:).md)
  The function used to respond to action resumed events.
- [func actionSkipped(event: Self.EventType)](actionhandlerprotocol/actionskipped(event:).md)
  The function used to respond to action skipped events.
- [func actionStarted(event: Self.EventType)](actionhandlerprotocol/actionstarted(event:).md)
  The function used to respond to action started events.
- [func actionTerminated(event: Self.EventType)](actionhandlerprotocol/actionterminated(event:).md)
  The function used to respond to action terminated events.
- [func actionUpdated(event: Self.EventType)](actionhandlerprotocol/actionupdated(event:).md)
  The function used to respond to action updated events.
### Type Aliases
- [ActionHandlerProtocol.EventType](actionhandlerprotocol/eventtype.md)
  The event type returned to each event function in the handler.
### Type Methods
- [static func register((Self.EventType) -> (any ActionHandlerProtocol)?)](actionhandlerprotocol/register(_:).md)
  Registers a handler that responds to raised action events for a particular action type.

## See Also

- [protocol EntityAction](entityaction.md)
  A protocol that defines an action for an entity.
- [struct ActionAnimation](actionanimation.md)
  Defines an an action animation.
- [enum ActionEntityResolution](actionentityresolution.md)
  Options available to determine the resolution method for a target entity in an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol)*