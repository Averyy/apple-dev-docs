# EntityAction Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var isAdditive: Bool](impulseaction/isadditive.md)
  A Boolean value that determines whether this action additively blends with the prior stage.
- [var isReversible: Bool](impulseaction/isreversible.md)
  A Boolean value that determines whether the action reverses prior operations when playback is reverses.
### Type Methods
- [static func registerAction()](impulseaction/registeraction-9ik3c.md)
  Registers the action into the action-types registry.
- [static func registerAction()](impulseaction/registeraction-g4ku.md)
  Registers the serializable action into the action-types registry.
- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> Void)](impulseaction/subscribe(to:_:)-1ehr8.md)
  Subscribes to an action event.
- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> Void)](impulseaction/subscribe(to:_:)-6fzb.md)
  Subscribes to a serializable action event.
- [static func unsubscribe(from: ActionEventType)](impulseaction/unsubscribe(from:).md)
  Unsubscribes from an action event.
- [static func unsubscribeAll()](impulseaction/unsubscribeall.md)
  Unsubscribes from all action events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/impulseaction/entityaction-implementations)*