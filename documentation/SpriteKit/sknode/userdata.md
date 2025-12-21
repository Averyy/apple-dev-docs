# userData

**Framework**: SpriteKit  
**Kind**: property

A dictionary containing arbitrary data.

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
var userData: NSMutableDictionary? { get set }
```

#### Discussion

You use this property to store your own data in a node. For example, you might store game-specific data about each node to use inside your game logic. This can be a useful alternative to creating your own node subclasses to hold game data.

SpriteKit does not do anything with the data stored in the node. However, the data is archived when the node is archived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sknode/userdata)*