# SPRect3DFloatTranslate

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
static SPRect3DFloat SPRect3DFloatTranslate(SPRect3DFloat rect, SPVector3DFloat offset);
```

#### Return Value

A rectangle that’s offset by the @p x, @p y, and @p z of the vector.

#### Discussion

Returns a rectangle with an origin that is offset from that of the source rectangle.

## Parameters

- `rect`: The source rectangle.
- `offset`: A vector that defines the offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dfloattranslate)*