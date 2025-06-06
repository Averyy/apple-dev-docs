# makeSharedTextureHandle()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new texture handle from a shareable texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func makeSharedTextureHandle() -> MTLSharedTextureHandle?
```

#### Discussion

If the texture is not shareable, this method returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/makesharedtexturehandle())*