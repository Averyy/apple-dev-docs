# SPRect3DRotationToRect

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns the rotation around the origin from the first rectangle to the second rectangle.

**Availability**:
- iOS 16.0+ - Deprecated in 16.0
- iPadOS 16.0+ - Deprecated in 16.0
- Mac Catalyst 16.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 13.0
- tvOS 16.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 9.0

## Declaration

```c
static SPRotation3D SPRect3DRotationToRect(SPRect3D rect, SPRect3D other);
```

#### Return Value

The rotation between two rectangles.

## Parameters

- `rect`: The rectangle to rotate.
- `other`: The second rectangle that the function computes the rotation to.

## See Also

### Deprecated symbols
- [SPRect3DTranslate](./sprect3dtranslate-8amf1.md)
  Returns a rectangle with an origin that’s offset by the specified size.
- [SPRect3DDistanceBetweenOrigins](./sprect3ddistancebetweenorigins.md)
  Returns the distance between the origins of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3drotationtorect)*