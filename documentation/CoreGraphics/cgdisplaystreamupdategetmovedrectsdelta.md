# CGDisplayStreamUpdateGetMovedRectsDelta

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

## Declaration

```c
extern void CGDisplayStreamUpdateGetMovedRectsDelta(CGDisplayStreamUpdateRef updateRef, CGFloat *dx, CGFloat *dy);
```

#### Discussion

Return the movement dx and dy values for a single update

The delta values describe the offset from the moved rectangles back to the source location.

## Parameters

- `updateRef`: The CGDisplayStreamUpdateRef
- `dx`: A pointer to a CGFloat to store the x component of the movement delta
- `dy`: A pointer to a CGFloat to store the y component of the movement delta


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdategetmovedrectsdelta)*