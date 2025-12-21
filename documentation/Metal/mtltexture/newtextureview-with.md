# newTextureView(with:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func newTextureView(with descriptor: MTLTextureViewDescriptor) -> (any MTLTexture)?
```

#### Discussion

Create a new texture which shares the same storage as the source texture, but with different (but compatible) properties specified by the descriptor


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/newtextureview(with:))*