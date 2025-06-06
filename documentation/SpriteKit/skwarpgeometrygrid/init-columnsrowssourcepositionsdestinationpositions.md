# init(columns:rows:sourcePositions:destinationPositions:)

**Framework**: SpriteKit  
**Kind**: init

Creates a warp geometry grid of a specific size and warp translation, in point arrays.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
convenience init(columns: Int, rows: Int, sourcePositions: [SIMD2<Float>] = [SIMD2<Float>](), destinationPositions: [SIMD2<Float>] = [SIMD2<Float>]())
```

#### Return Value

A new warp geometry grid object.

#### Discussion

You supply the source and destination position as row-major arrays of normalized [`vector_float2`](https://developer.apple.com/documentation/simd/vector_float2) coordinates. The number of horizontal coordinates is the column count plus one and the number of vertical coordinates is the row count plus one. Passing `nil` as either of the position arguments results in an identity warp with vertices distributed evenly throughout the geometry. Passing `nil` to both `sourcePositions` and `destPositions` gives a result identical to [`init(columns:rows:)`](skwarpgeometrygrid/init(columns:rows:).md).

## Parameters

- `columns`: The number of columns in the grid.
- `rows`: The number of rows in the grid.
- `sourcePositions`: Optionally included array of the grid’s source warp positions.
- `destinationPositions`: Optionally included array of the grid’s destination warp positions.

## See Also

- [convenience init(columns: Int, rows: Int)](skwarpgeometrygrid/init(columns:rows:).md)
  Creates a warp geometry grid of a specified size.
- [init?(coder: NSCoder)](skwarpgeometrygrid/init(coder:).md)
  Tells you when to intialize a grid that was loaded from an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/init(columns:rows:sourcepositions:destinationpositions:))*