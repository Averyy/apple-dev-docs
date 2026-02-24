# init(layout:isInEquirectangularProjection:texture:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an immersive video mask object.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(layout: ImmersiveVideoMask.Layout, isInEquirectangularProjection: Bool, texture: any MTLTexture)
```

## Parameters

- `layout`: The layout of the mask within the texture. See [`ImmersiveVideoMask.Layout`](immersivevideomask/layout-swift.enum.md) for valid options.
- `isInEquirectangularProjection`: A Boolean value that indicates whether the generated mask texture is in equirectangular projection space.
- `texture`: The MTLTexture containing the mask ready for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask/init(layout:isinequirectangularprojection:texture:))*