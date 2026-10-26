# SPPoint3DAlmostEqualToPoint

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
static bool SPPoint3DAlmostEqualToPoint(SPPoint3D p1, SPPoint3D p2);
```

#### Return Value

A Boolean value that indicates whether the two points are equal within the specified default absolute tolerance.

#### Discussion

Returns a Boolean value that indicates whether the two points are equal within the specified default absolute tolerance.

> **Note**: The Spatial default tolerance is @p sqrt(**DBL_EPSILON**) .

## Parameters

- `p1`: The first point.
- `p2`: The first point.

## See Also

### Comparing values
- [SPPoint3DAlmostEqualToPoint](./sppoint3dalmostequaltopoint-9vk02.md)
  Returns a Boolean value that indicates whether the two points are equal within the specified default absolute tolerance.
- [SPPoint3DEqualToPoint](./sppoint3dequaltopoint.md)
  Returns a Boolean value that indicates whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dalmostequaltopoint-8qyca)*