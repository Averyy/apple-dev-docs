# hostPresentCount

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The number of unique frames that the host has encoded since object creation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var hostPresentCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger hostPresentCount;
```

## Discussion

The value of this property can be smaller than the number of times you’ve called the [`encodeCurrentFrame(to:texture:region:)`](./encodecurrentframe%28to,texture,region%29.md) method if you encode the same frame multiple times.

## See Also

### Handling Frame Updates
- [var guestPresentCount: Int](./guestpresentcount.md)
  The number of frame presents that the guest has generated since object creation.
- [var minimumTextureUsage: MTLTextureUsage](./minimumtextureusage.md)
  The Metal texture usage flags necessary for any texture that can be a destination for frame data.
- [func encodeCurrentFrame(to: any MTLCommandBuffer, texture: any MTLTexture, region: MTLRegion) -> Bool](./encodecurrentframe%28to,texture,region%29.md)
  Encodes Metal commands to process the current frame and write it to a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/hostpresentcount)*