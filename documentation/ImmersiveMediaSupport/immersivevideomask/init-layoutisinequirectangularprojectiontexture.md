# init(layout:isInEquirectangularProjection:texture:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an immersive video mask object.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(layout: ImmersiveVideoMask.Layout, isInEquirectangularProjection: Bool, texture: any MTLTexture)
```

## Parameters

- `layout`: How the left and right sides of the mask are represented within the texture. See   for valid options.
- `isInEquirectangularProjection`: Boolean value that indicates whether the generated mask texture is in equirectangular projection space or not.
- `texture`: The MTLTexture containing the mask ready for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask/init(layout:isinequirectangularprojection:texture:))*