# shouldColorMatch()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns whether the image should be color matched.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
optional func shouldColorMatch() -> Bool
```

```objc
- (BOOL) shouldColorMatch;
```

## Return Value

[`false`](../../Swift/false.md) if the image is a mask or gradient; otherwise [`true`](../../Swift/true.md), which is the default.

## See Also

### Providing Information About the Image
- [func imageBounds() -> NSRect](./imagebounds%28%29.md)
  Returns the bounds of the image expressed in pixels and aligned to integer boundaries.
- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](./imagecolorspace%28%29.md)
  Returns the color space of the image or `NULL` if the image should not be color matched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/shouldcolormatch())*