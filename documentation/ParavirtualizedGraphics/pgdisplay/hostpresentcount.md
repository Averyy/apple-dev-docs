# hostPresentCount

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Required**: Yes

The number of unique frames that the host has encoded since object creation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var hostPresentCount: Int { get }
```

#### Discussion

The value of this property can be smaller than the number of times you’ve called the [`encodeCurrentFrame(to:texture:region:)`](pgdisplay/encodecurrentframe(to:texture:region:).md) method if you encode the same frame multiple times.

## See Also

- [var guestPresentCount: Int](pgdisplay/guestpresentcount.md)
  The number of frame presents that the guest has generated since object creation.
- [var minimumTextureUsage: MTLTextureUsage](pgdisplay/minimumtextureusage.md)
  The Metal texture usage flags necessary for any texture that can be a destination for frame data.
- [func encodeCurrentFrame(to: any MTLCommandBuffer, texture: any MTLTexture, region: MTLRegion) -> Bool](pgdisplay/encodecurrentframe(to:texture:region:).md)
  Encodes Metal commands to process the current frame and write it to a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/hostpresentcount)*