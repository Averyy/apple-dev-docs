# PHASEContainerNodeDefinition

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A node that plays all its children at the same time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEContainerNodeDefinition
```

```objc
@interface PHASEContainerNodeDefinition : PHASESoundEventNodeDefinition
```

## Overview

This node adds structure to the sound event tree while performing no conditional logic or audio playback of its own. By passing invocation to all its children at once, this class invokes the child nodes’ actions simultaneously.

## Topics

### Creating a Node
- [init()](./phasecontainernodedefinition/init%28%29.md)
  Creates a container node.
- [init(identifier: String)](./phasecontainernodedefinition/init%28identifier%29.md)
  Creates a container node with the given name.
- [class func new() -> Self](./phasecontainernodedefinition/new%28%29.md)
  Creates a container node.
### Adding Descendent Nodes
- [func addSubtree(PHASESoundEventNodeDefinition)](./phasecontainernodedefinition/addsubtree%28_%29.md)
  Adds a sound event node as a child.

## Relationships

### Inherits From
- [PHASESoundEventNodeDefinition](./phasesoundeventnodedefinition.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Control Nodes
- [class PHASESwitchNodeDefinition](./phaseswitchnodedefinition.md)
  A node that passes invocation to only one of its child nodes.
- [class PHASERandomNodeDefinition](./phaserandomnodedefinition.md)
  A sound event node that invokes one of its child nodes at random.
- [class PHASEBlendNodeDefinition](./phaseblendnodedefinition.md)
  A node that smoothly fades between the audio of its child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecontainernodedefinition)*