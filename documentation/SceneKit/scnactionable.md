# SCNActionable

**Framework**: SceneKit  
**Kind**: protocol

Methods for running actions on nodes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol SCNActionable : NSObjectProtocol
```

#### Overview

[`SCNAction`](scnaction.md) objects represent reusable, animated actions that can be performed on nodes, such as moving or rotating them. You use an [`SCNAction`](scnaction.md) class method to create an action and then use methods in the [`SCNActionable`](scnactionable.md) protocol to run the action on a node. This protocol also defines methods for checking whether a node has any currently running actions and, if so, canceling them.

## Topics

### Running Actions
- [func runAction(SCNAction)](scnactionable/runaction(_:).md)
  Adds an action to the list of actions executed by the node.
- [func runAction(SCNAction, completionHandler: (() -> Void)?)](scnactionable/runaction(_:completionhandler:).md)
  Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
- [func runAction(SCNAction, forKey: String?)](scnactionable/runaction(_:forkey:).md)
  Adds an identifiable action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](scnactionable/runaction(_:forkey:completionhandler:).md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
### Inspecting a Node’s Running Actions
- [func action(forKey: String) -> SCNAction?](scnactionable/action(forkey:).md)
  Returns an action associated with a specific key.
- [var hasActions: Bool](scnactionable/hasactions.md)
  A Boolean value that indicates whether the node is currently executing any actions.
- [var actionKeys: [String]](scnactionable/actionkeys.md)
  The list of keys for which the node has attached actions.
### Canceling a Node’s Running Actions
- [func removeAction(forKey: String)](scnactionable/removeaction(forkey:).md)
  Removes an action associated with a specific key.
- [func removeAllActions()](scnactionable/removeallactions.md)
  Ends and removes all actions from the node.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SCNNode](scnnode.md)
- [SCNReferenceNode](scnreferencenode.md)

## See Also

- [class SCNAction](scnaction.md)
  A simple, reusable animation that changes attributes of any node you attach it to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable)*