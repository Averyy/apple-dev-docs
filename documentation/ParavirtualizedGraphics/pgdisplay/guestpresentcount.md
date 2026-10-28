# guestPresentCount

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The number of frame presents that the guest has generated since object creation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var guestPresentCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger guestPresentCount;
```

## Discussion

This value can exceed the number of times that the framework invokes the [`newFrameEventHandler`](../pgdisplaydescriptor/newframeeventhandler.md) block if the host isn’t encoding frames fast enough to keep up.

## See Also

### Handling Frame Updates
- [var hostPresentCount: Int](./hostpresentcount.md)
  The number of unique frames that the host has encoded since object creation.
- [var minimumTextureUsage: MTLTextureUsage](./minimumtextureusage.md)
  The Metal texture usage flags necessary for any texture that can be a destination for frame data.
- [func encodeCurrentFrame(to: any MTLCommandBuffer, texture: any MTLTexture, region: MTLRegion) -> Bool](./encodecurrentframe%28to,texture,region%29.md)
  Encodes Metal commands to process the current frame and write it to a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/guestpresentcount)*