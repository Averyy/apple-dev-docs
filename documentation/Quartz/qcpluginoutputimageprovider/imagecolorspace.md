# imageColorSpace()

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the color space of the image or `NULL` if the image should not be color matched.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func imageColorSpace() -> Unmanaged<CGColorSpace>!
```

#### Return Value

The color space of the image or `NULL`.

## See Also

- [func imageBounds() -> NSRect](qcpluginoutputimageprovider/imagebounds.md)
  Returns the bounds of the image expressed in pixels and aligned to integer boundaries.
- [func shouldColorMatch() -> Bool](qcpluginoutputimageprovider/shouldcolormatch.md)
  Returns whether the image should be color matched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/imagecolorspace())*