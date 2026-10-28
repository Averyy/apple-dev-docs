# SCNActionable

**Framework**: SceneKit  
**Kind**: protocol  
**Role**: Protocol

Methods for running actions on nodes.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
protocol SCNActionable : NSObjectProtocol
```

```objc
@protocol SCNActionable <NSObject>
```

## Overview

[`SCNAction`](./scnaction.md) objects represent reusable, animated actions that can be performed on nodes, such as moving or rotating them. You use an [`SCNAction`](./scnaction.md) class method to create an action and then use methods in the [`SCNActionable`](./scnactionable.md) protocol to run the action on a node. This protocol also defines methods for checking whether a node has any currently running actions and, if so, canceling them.

## Topics

### Running Actions
- [func runAction(SCNAction)](./scnactionable/runaction%28_%29.md)
  Adds an action to the list of actions executed by the node.
- [func runAction(SCNAction, completionHandler: (() -> Void)?)](./scnactionable/runaction%28_,completionhandler%29.md)
  Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
- [func runAction(SCNAction, forKey: String?)](./scnactionable/runaction%28_,forkey%29.md)
  Adds an identifiable action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](./scnactionable/runaction%28_,forkey,completionhandler%29.md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
### Inspecting a Node’s Running Actions
- [func action(forKey: String) -> SCNAction?](./scnactionable/action%28forkey%29.md)
  Returns an action associated with a specific key.
- [var hasActions: Bool](./scnactionable/hasactions.md)
  A Boolean value that indicates whether the node is currently executing any actions.
- [var actionKeys: [String]](./scnactionable/actionkeys.md)
  The list of keys for which the node has attached actions.
### Canceling a Node’s Running Actions
- [func removeAction(forKey: String)](./scnactionable/removeaction%28forkey%29.md)
  Removes an action associated with a specific key.
- [func removeAllActions()](./scnactionable/removeallactions%28%29.md)
  Ends and removes all actions from the node.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [SCNNode](./scnnode.md)
- [SCNReferenceNode](./scnreferencenode.md)

## See Also

### Actions
- [class SCNAction](./scnaction.md)
  A simple, reusable animation that changes attributes of any node you attach it to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable)*