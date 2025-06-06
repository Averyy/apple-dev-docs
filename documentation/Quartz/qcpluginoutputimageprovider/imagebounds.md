# imageBounds()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the bounds of the image expressed in pixels and aligned to integer boundaries.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func imageBounds() -> NSRect
```

#### Return Value

The bounds of the image. Note that the `QCPlugIn` class does not support images that have infinite bounds.

## See Also

- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](qcpluginoutputimageprovider/imagecolorspace.md)
  Returns the color space of the image or `NULL` if the image should not be color matched.
- [func shouldColorMatch() -> Bool](qcpluginoutputimageprovider/shouldcolormatch.md)
  Returns whether the image should be color matched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/imagebounds())*