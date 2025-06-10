# setViewports(_:)

**Framework**: Metal  
**Kind**: method

Sets an array of viewports to transform vertices from normalized device coordinates to window coordinates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setViewports(_ viewports: [MTLViewport])
```

#### Discussion

Metal clips fragments that lie outside of the viewport, and optionally clamps fragments outside of z-near/z-far range, depending on the value you assign to [`setDepthClipMode(_:)`](mtl4rendercommandencoder/setdepthclipmode(_:).md).

Metal selects the viewport to use from the `[[ viewport_array_index ]]` attribute you specify in the pipeline state’s vertex shader function in the Metal Shading Language.

## Parameters

- `viewports`: A Swift array of   elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setviewports(_:))*