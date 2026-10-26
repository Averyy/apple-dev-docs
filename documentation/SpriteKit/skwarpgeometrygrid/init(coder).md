# init(coder:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Tells you when to intialize a grid that was loaded from an archive.

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
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## See Also

### Creating a Warp Geometry Grid
- [convenience init(columns: Int, rows: Int)](./init%28columns,rows%29.md)
  Creates a warp geometry grid of a specified size.
- [convenience init(columns: Int, rows: Int, sourcePositions: [SIMD2<Float>], destinationPositions: [SIMD2<Float>])](./init%28columns,rows,sourcepositions,destinationpositions%29.md)
  Creates a warp geometry grid of a specific size and warp translation, in point arrays.
- [- initWithColumns:rows:sourcePositions:destPositions:](./initwithcolumns_rows_sourcepositions_destpositions_.md)
  Creates a warp geometry grid of a specific size and warp translation, in pointers to point arrays.
- [+ gridWithColumns:rows:sourcePositions:destPositions:](./gridwithcolumns_rows_sourcepositions_destpositions_.md)
- [+ grid](./grid.md)
  Initializes a new empty grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/init(coder:))*