# isEmpty

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether two or three of the dimensions are zero.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

```c
static bool SPRect3DIsEmpty(SPRect3D rect);
```

## See Also

### Checking characteristics
- [func contains(anyOf: [Point3D]) -> Bool](./contains%28anyof%29.md)
  Returns a Boolean value that indicates whether the rectangle contains any of the specified points.
- [func intersects(Rect3D) -> Bool](./intersects%28_%29.md)
  Returns a Boolean value that indicates whether two rectangles intersect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/isempty)*