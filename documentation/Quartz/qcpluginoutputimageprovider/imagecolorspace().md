# imageColorSpace()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the color space of the image or `NULL` if the image should not be color matched.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func imageColorSpace() -> Unmanaged<CGColorSpace>!
```

```objc
- (CGColorSpaceRef) imageColorSpace;
```

## Return Value

The color space of the image or `NULL`.

## See Also

### Providing Information About the Image
- [func imageBounds() -> NSRect](./imagebounds%28%29.md)
  Returns the bounds of the image expressed in pixels and aligned to integer boundaries.
- [func shouldColorMatch() -> Bool](./shouldcolormatch%28%29.md)
  Returns whether the image should be color matched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/imagecolorspace())*