# init(center:size:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a rectangle at the specified center with the specified size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(center: Point3DFloat, size: Size3DFloat)
```

```c
static SPRect3DFloat SPRect3DFloatMakeAtCenter(SPPoint3DFloat center, SPSize3DFloat size);
```

## Return Value

A new rectangle stucture.

## Discussion

Returns a rectangle at the specified center.

## Parameters

- `center`: A point structure that specifies the center of the rectangle.
- `size`: A size structure that specifies the sie of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/init(center:size:)-e8la)*