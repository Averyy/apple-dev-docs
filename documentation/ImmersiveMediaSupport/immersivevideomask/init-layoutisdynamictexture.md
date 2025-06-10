# init(layout:isDynamic:texture:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an ImmersiveVideoMask.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(layout: ImmersiveVideoMask.Layout, isDynamic: Bool, texture: any MTLTexture)
```

## Parameters

- `layout`: How the left and right sides of the mask are represented within the texture. See   for valid options.
- `isDynamic`: Was this mask created from a dynamic mask definition. This can be useful if the rendering needs to handle dynamic masks differently.
- `texture`: The MTLTexture containing the mask ready for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask/init(layout:isdynamic:texture:))*