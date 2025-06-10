# setTextureView(texture:descriptor:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new lightweight texture view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setTextureView(texture: any MTLTexture, descriptor: MTLTextureViewDescriptor, index: Int) -> MTLResourceID
```

#### Return Value

The [`MTLResourceID`](mtlresourceid.md) of a newly created texture view in this pool.

#### Discussion

This method creates a lightweight texture view over a texture according to a descriptor you provide. It then associates the texture view with a slot in this texture view pool at the index you specify.

## Parameters

- `texture`: An   instance for which to create a new lightweight texture view.
- `descriptor`: A descriptor specifying properties of the texture view to create.
- `index`: An index of a slot in the texture pool into which this method writes the new texture view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureviewpool/settextureview(texture:descriptor:index:))*