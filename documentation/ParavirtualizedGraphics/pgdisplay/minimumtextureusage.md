# minimumTextureUsage

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Required**: Yes

The Metal texture usage flags necessary for any texture that can be a destination for frame data.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var minimumTextureUsage: MTLTextureUsage { get }
```

## See Also

- [var guestPresentCount: Int](pgdisplay/guestpresentcount.md)
  The number of frame presents that the guest has generated since object creation.
- [var hostPresentCount: Int](pgdisplay/hostpresentcount.md)
  The number of unique frames that the host has encoded since object creation.
- [func encodeCurrentFrame(to: any MTLCommandBuffer, texture: any MTLTexture, region: MTLRegion) -> Bool](pgdisplay/encodecurrentframe(to:texture:region:).md)
  Encodes Metal commands to process the current frame and write it to a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/minimumtextureusage)*