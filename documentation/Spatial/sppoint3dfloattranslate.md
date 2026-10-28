# SPPoint3DFloatTranslate

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
static SPPoint3DFloat SPPoint3DFloatTranslate(SPPoint3DFloat point, SPVector3DFloat offset);
```

## Return Value

A point that’s offset by the @p x, @p y, and @p z of the vector.

## Discussion

Returns a point with an origin that is offset from that of the source point.

## Parameters

- `point`: The source point.
- `offset`: A vector that defines the offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloattranslate)*