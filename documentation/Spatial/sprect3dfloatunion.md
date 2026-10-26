# SPRect3DFloatUnion

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPRect3DFloat SPRect3DFloatUnion(SPRect3DFloat rect, SPRect3DFloat other);
```

#### Return Value

A rectangle structure that is the smallest rectangle that contains two sizes.

#### Discussion

Returns the smallest rectangle that contains two rectangles.

## Parameters

- `rect`: The first rectangle.
- `other`: The second rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloatunion)*