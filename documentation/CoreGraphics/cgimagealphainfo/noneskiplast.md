# CGImageAlphaInfo.noneSkipLast

**Framework**: Core Graphics  
**Kind**: case

There is no alpha channel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case noneSkipLast
```

## See Also

- [CGImageAlphaInfo.first](cgimagealphainfo/first.md)
  The alpha component is stored in the most significant bits of each pixel. For example, non-premultiplied ARGB.
- [CGImageAlphaInfo.last](cgimagealphainfo/last.md)
  The alpha component is stored in the least significant bits of each pixel. For example, non-premultiplied RGBA.
- [CGImageAlphaInfo.none](cgimagealphainfo/none.md)
  There is no alpha channel.
- [CGImageAlphaInfo.noneSkipFirst](cgimagealphainfo/noneskipfirst.md)
  There is no alpha channel. If the total size of the pixel is greater than the space required for the number of color components in the color space, the most significant bits are ignored.
- [CGImageAlphaInfo.alphaOnly](cgimagealphainfo/alphaonly.md)
  There is no color data, only an alpha channel.
- [CGImageAlphaInfo.premultipliedFirst](cgimagealphainfo/premultipliedfirst.md)
  The alpha component is stored in the most significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied ARGB.
- [CGImageAlphaInfo.premultipliedLast](cgimagealphainfo/premultipliedlast.md)
  The alpha component is stored in the least significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied RGBA.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/noneskiplast)*