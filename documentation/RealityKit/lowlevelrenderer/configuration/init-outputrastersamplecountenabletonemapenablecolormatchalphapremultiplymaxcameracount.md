# init(output:rasterSampleCount:enableTonemap:enableColorMatch:alphaPremultiply:maxCameraCount:)

**Framework**: RealityKit  
**Kind**: init

Creates a configuration with the given output format, MSAA sample count, and flags.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(output: LowLevelRenderer.Configuration.Output, rasterSampleCount: Int, enableTonemap: Bool = true, enableColorMatch: Bool = false, alphaPremultiply: Bool = true, maxCameraCount: Int = 1)
```

## Parameters

- `output`: The pixel format configuration for the renderer’s output attachments.
- `rasterSampleCount`: The number of samples per pixel for MSAA.
- `enableTonemap`: When `true`, HDR output values are tone-mapped before writing to the output texture. Defaults to `true`.
- `enableColorMatch`: When `true`, a gamut conversion matrix from `renderer.colorMatch` is applied during resolve. Defaults to `false`.
- `alphaPremultiply`: When `true`, the renderer divides content by alpha before applying tonemap and color match, then multiplies by alpha before final texture output. Defaults to `true`.
- `maxCameraCount`: The maximum number of simultaneous cameras supported. Defaults to `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/configuration/init(output:rastersamplecount:enabletonemap:enablecolormatch:alphapremultiply:maxcameracount:))*