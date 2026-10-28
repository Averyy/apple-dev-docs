# NSImage.DynamicRange.unspecified

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Indicates that the dynamic range treatment of the image is unknown or otherwise unspecified.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case unspecified
```

```c
NSImageDynamicRangeUnspecified
```

## Discussion

The [`imageDynamicRange`](../../nsimageview/imagedynamicrange.md) property can return this type when the system can’t determine the High Dynamic Range (HDR) of the image. Otherwise, the use of this value isn’t encouraged and results in undefined behavior.

## See Also

### Setting the dynamic range
- [NSImage.DynamicRange.standard](./standard.md)
  Restricts the image content dynamic range to the standard range regardless of the actual range of the image content.
- [NSImage.DynamicRange.constrainedHigh](./constrainedhigh.md)
  Allows for constrained High Dynamic Range (HDR) image content which is useful for mixing HDR and Standard Dynamic Range (SDR) content.
- [NSImage.DynamicRange.high](./high.md)
  Allows image content to use extended dynamic range if it has dynamic range content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/dynamicrange/unspecified)*