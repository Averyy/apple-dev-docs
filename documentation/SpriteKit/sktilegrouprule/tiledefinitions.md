# tileDefinitions

**Framework**: SpriteKit  
**Kind**: property

The tile definitions used for this rule.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var tileDefinitions: [SKTileDefinition] { get set }
```

#### Discussion

When this rule is evaluated and its conditions met, one of the definitions is randomly selected for placement based on their placement weights.

## See Also

- [var adjacency: SKTileAdjacencyMask](sktilegrouprule/adjacency.md)
  The adjacency requirement for this rule.
- [struct SKTileAdjacencyMask](sktileadjacencymask.md)
  An enumeration defining how neighboring tiles are automatically placed next to each other.
- [var name: String?](sktilegrouprule/name.md)
  A name associated with the tile group rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilegrouprule/tiledefinitions)*