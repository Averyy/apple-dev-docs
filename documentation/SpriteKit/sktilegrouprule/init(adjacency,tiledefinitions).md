# init(adjacency:tileDefinitions:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a new tile group rule with adjacency rules and tile definitions.

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
init(adjacency: SKTileAdjacencyMask, tileDefinitions: [SKTileDefinition])
```

```objc
- (instancetype) initWithAdjacency:(SKTileAdjacencyMask) adjacency tileDefinitions:(NSArray<SKTileDefinition *> *) tileDefinitions;
```

## Return Value

A new tile group rule.

## Parameters

- `adjacency`: The adjacency requirements for this rule.
- `tileDefinitions`: The tile definitions used for this rule.

## See Also

### Creating a Tile Group Rule
- [+ tileGroupRuleWithAdjacency:tileDefinitions:](./tilegrouprulewithadjacency_tiledefinitions_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilegrouprule/init(adjacency:tiledefinitions:))*