# setViewport(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets the viewport which that transforms vertices from normalized device coordinates to window coordinates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setViewport(_ viewport: MTLViewport)
```

#### Discussion

Metal clips fragments that lie outside this viewport, and optionally clamps fragments outside of z-near/z-far range depending on the value you assign to [`setDepthClipMode(_:)`](mtl4rendercommandencoder/setdepthclipmode(_:).md).

## Parameters

- `viewport`:   to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setviewport(_:))*