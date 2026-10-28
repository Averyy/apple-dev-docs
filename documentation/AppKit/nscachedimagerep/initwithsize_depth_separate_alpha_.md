# initWithSize:depth:separate:alpha:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a cached image representation initialized with the specified image characteristics.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (id) initWithSize:(NSSize) size depth:(NSWindowDepth) depth separate:(BOOL) flag alpha:(BOOL) alpha;
```

## Return Value

The initialized `NSCachedImageRep` object or `nil` if the object could not be initialized.

## Parameters

- `size`: The size of the image, measured in points.
- `depth`: The bit depth of the image. Specify 0 if you want the image to be the same depth as the deepest screen on the current system.
- `flag`: [`true`](../../Swift/true.md) if the receiver should use a separate offscreen window to store the image; otherwise, [`false`](../../Swift/false.md) if the receiver should use a shared window.
- `alpha`: [`true`](../../Swift/true.md) if the image includes transparency information; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [- setCacheDepthMatchesImageDepth:](../nsimage/setcachedepthmatchesimagedepth_.md)
  Sets whether the image’s offscreen window caches use the same bit depth as the image data itself.
- [var hasAlpha: Bool](../nsimagerep/hasalpha.md)
  A Boolean value that indicates whether the image data has an alpha channel.
- [- setCachedSeparately:](../nsimage/setcachedseparately_.md)
  Sets whether each image representation uses a separate offscreen window to cache its contents.
- [var bitsPerSample: Int](../nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
### Initializing Cached Representations of Images
- [- initWithWindow:rect:](./initwithwindow_rect_.md)
  Returns a cached image representation initialized for drawing in the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscachedimagerep/initwithsize:depth:separate:alpha:)*