# PHASERandomNodeDefinition

**Framework**: PHASE  
**Kind**: class

A sound event node that invokes one of its child nodes at random.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASERandomNodeDefinition
```

#### Overview

When the framework invokes a random node, it passes the invocation on to one of its children at random. The weight you choose for a child node in the [`addSubtree(_:weight:)`](phaserandomnodedefinition/addsubtree(_:weight:).md) argument skews the node’s selection chances.

##### Choose From Alternate Sounds

This class can model real-world cases where an event varies slightly, such as when footsteps sound slightly different because of the unique ground composition at each step.

![Illustration of a flowchart that represents a sound event node tree. The chart contains three boxes, which represent nodes. At left, a box labeled Random Node extends an arrow, which points to a box in the upper right that’s labeled Sampler Node Footstep Variation One. The box labeled Random Node extends another arrow, which points to a box in the lower right that’s labeled Sampler Node Footstep Variation Two. ](https://docs-assets.developer.apple.com/published/3e7605629beec5855ca52d33b3bf11de/media-3918860%402x.png)

The following code creates an instance of this class that selects from three different footstep sounds. The weights determine that an uncommon footstep noise plays half as frequently as the common footstep. And a third footstep noise plays 10% of the time.

**Swift**:

```swift
// Create several nodes from prior-registered footstep sound assets.
let footstep1 = PHASESamplerNodeDefinition(
    soundAssetIdentifier: "footstep1",
    mixerDefinition: myMixer, identifier: "footstep1")
let footstep2 = PHASESamplerNodeDefinition(
    soundAssetIdentifier: "footstep2",
    mixerDefinition: myMixer, identifier: "footstep2")
let footstep3 = PHASESamplerNodeDefinition(
    soundAssetIdentifier: "footstep3",    
    mixerDefinition: myMixer, identifier: "footstep3")

// Create the random node.
let randomNode = PHASERandomNodeDefinition(identifier: "randomNode")

// Connect leaf nodes to the tree and set the weights. 
randomNode.addSubtree(footstep1, weight: 10)
randomNode.addSubtree(footstep2, weight: 5)
randomNode.addSubtree(footstep3, weight: 1)
```

**Objective-C**:

```objc
// Create several nodes from prior-registered footstep sound assets.
PHASESamplerNodeDefinition* footstep1 = 
    [[PHASESamplerNodeDefinition alloc] 
        initWithSoundAssetUID:@"footstep1" 
        mixerDefinition:mixNode uid:@"footstep1"];
PHASESamplerNodeDefinition* footstep2 = 
    [[PHASESamplerNodeDefinition alloc] 
        initWithSoundAssetUID:@"footstep2" 
        mixerDefinition:mixNode uid:@"footstep2"];
PHASESamplerNodeDefinition* footstep3 = 
    [[PHASESamplerNodeDefinition alloc] 
        initWithSoundAssetUID:@"footstep3" 
        mixerDefinition:mixNode uid:@"footstep3"];

// Create the random node.
PHASERandomNodeDefinition* randomNode = 
    [[PHASERandomNodeDefinition alloc] initWithUID:@"randomNode"];

// Connect leaf nodes to the tree and set the weights. 
[randomNode addSubtree:footstep1 weight:@10];
[randomNode addSubtree:footstep2 weight:@5];
[randomNode addSubtree:footstep3 weight:@1];
```

## Topics

### Creating a Node
- [init()](phaserandomnodedefinition/init.md)
  Creates a random node.
- [convenience init(identifier: String)](phaserandomnodedefinition/init(identifier:).md)
  Creates a random node with the name you specify.
### Adding Descendent Nodes
- [func addSubtree(PHASESoundEventNodeDefinition, weight: NSNumber)](phaserandomnodedefinition/addsubtree(_:weight:).md)
  Adds a node tree that’s one of the random-selection options.
### Defining Selection Queue Length
- [var uniqueSelectionQueueLength: Int](phaserandomnodedefinition/uniqueselectionqueuelength.md)
  The length of the unique selection queue.

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
- [class PHASEBlendNodeDefinition](phaseblendnodedefinition.md)
  A node that smoothly fades between the audio of its child nodes.
- [class PHASEContainerNodeDefinition](phasecontainernodedefinition.md)
  A node that plays all its children at the same time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaserandomnodedefinition)*