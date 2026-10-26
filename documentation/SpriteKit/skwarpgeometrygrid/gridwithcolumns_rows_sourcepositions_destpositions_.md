# gridWithColumns:rows:sourcePositions:destPositions:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
+ (instancetype) gridWithColumns:(NSInteger) cols rows:(NSInteger) rows sourcePositions:(const vector_float2 *) sourcePositions destPositions:(const vector_float2 *) destPositions;
```

## See Also

### Creating a Warp Geometry Grid
- [convenience init(columns: Int, rows: Int)](./init%28columns,rows%29.md)
  Creates a warp geometry grid of a specified size.
- [- initWithColumns:rows:sourcePositions:destPositions:](./initwithcolumns_rows_sourcepositions_destpositions_.md)
  Creates a warp geometry grid of a specific size and warp translation, in pointers to point arrays.
- [+ grid](./grid.md)
  Initializes a new empty grid.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Tells you when to intialize a grid that was loaded from an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/gridwithcolumns:rows:sourcepositions:destpositions:)*