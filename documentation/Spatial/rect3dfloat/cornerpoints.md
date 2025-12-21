# cornerPoints

**Framework**: Spatial  
**Kind**: property

Returns the corner points of the rectangle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var cornerPoints: [Point3DFloat] { get }
```

#### Discussion

This function returns the vertices in a clockwise direction, starting from the origin:

```None
           5-----6
           |     |
        1-----2  |
        |  |  |  |        y  z
        |  4--|--7        | /
        |     |           |/
        0-----3           +-- x
```

For example, `points[0]` equals `rect.origin`, and `points[6]` is at  `rect.origin` offset by `rect.size`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/cornerpoints)*