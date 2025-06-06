# rootNode

**Framework**: GameplayKit  
**Kind**: property

The SpriteKit scene managed by this [`GKScene`](gkscene.md) object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var rootNode: (any GKSceneRootNodeType)? { get set }
```

#### Discussion

The [`GKSceneRootNodeType`](gkscenerootnodetype.md) protocol is an indirect type for game scene classes that the [`GKScene`](gkscene.md) class can load. [`SKScene`](https://developer.apple.com/documentation/SpriteKit/SKScene) is the only class currently supported for loading with the [`GKScene`](gkscene.md) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkscene/rootnode)*