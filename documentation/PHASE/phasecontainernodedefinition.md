# PHASEContainerNodeDefinition

**Framework**: PHASE  
**Kind**: class

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

#### Overview

This node adds structure to the sound event tree while performing no conditional logic or audio playback of its own. By passing invocation to all its children at once, this class invokes the child nodes’ actions simultaneously.

## Topics

### Creating a Node
- [init()](phasecontainernodedefinition/init.md)
  Creates a container node.
- [init(identifier: String)](phasecontainernodedefinition/init(identifier:).md)
  Creates a container node with the given name.
- [class func new() -> Self](phasecontainernodedefinition/new.md)
  Creates a container node.
### Adding Descendent Nodes
- [func addSubtree(PHASESoundEventNodeDefinition)](phasecontainernodedefinition/addsubtree(_:).md)
  Adds a sound event node as a child.

## Relationships

### Inherits From
- [PHASESoundEventNodeDefinition](phasesoundeventnodedefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASESwitchNodeDefinition](phaseswitchnodedefinition.md)
  A node that passes invocation to only one of its child nodes.
- [class PHASERandomNodeDefinition](phaserandomnodedefinition.md)
  A sound event node that invokes one of its child nodes at random.
- [class PHASEBlendNodeDefinition](phaseblendnodedefinition.md)
  A node that smoothly fades between the audio of its child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecontainernodedefinition)*