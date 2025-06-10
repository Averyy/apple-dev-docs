# setTextureView(texture:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies a default texture view to a slot in this texture view pool at an index provided.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setTextureView(texture: any MTLTexture, index: Int) -> MTLResourceID
```

#### Return Value

The [`MTLResourceID`](mtlresourceid.md) of a newly created texture view in this pool.

## Parameters

- `texture`: An   instance for which to copy its texture view.
- `index`: An index of a slot in this texture pool into which this method copies the texture view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureviewpool/settextureview(texture:index:))*