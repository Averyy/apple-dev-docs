# init(rules:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates and initializes a tile group with the specified tile group rules.

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
init(rules: [SKTileGroupRule])
```

```objc
- (instancetype) initWithRules:(NSArray<SKTileGroupRule *> *) rules;
```

## Mentions

- [Creating Tile Groups Programmatically](../creating-tile-groups-programmatically.md)

#### Return Value

A new tile group.

## Parameters

- `rules`: The tile group rules to determine tile placement.

## See Also

### Creating Tile Groups
- [Creating Tile Groups Programmatically](../creating-tile-groups-programmatically.md)
  Paint tiles on a map by putting tile definitions in a group that you create in code.
- [init(tileDefinition: SKTileDefinition)](./init%28tiledefinition%29.md)
  Creates and initializes a simple tile group with a single tile definition.
- [+ tileGroupWithTileDefinition:](./tilegroupwithtiledefinition_.md)
- [+ tileGroupWithRules:](./tilegroupwithrules_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktilegroup/init(rules:))*