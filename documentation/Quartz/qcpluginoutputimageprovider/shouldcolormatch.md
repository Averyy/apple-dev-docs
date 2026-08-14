# shouldColorMatch()

**Framework**: Quartz  
**Kind**: method

Returns whether the image should be color matched.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func shouldColorMatch() -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/swift/false) if the image is a mask or gradient; otherwise [`true`](https://developer.apple.com/documentation/swift/true), which is the default.

## See Also

- [func imageBounds() -> NSRect](qcpluginoutputimageprovider/imagebounds.md)
  Returns the bounds of the image expressed in pixels and aligned to integer boundaries.
- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](qcpluginoutputimageprovider/imagecolorspace.md)
  Returns the color space of the image or `NULL` if the image should not be color matched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/shouldcolormatch())*