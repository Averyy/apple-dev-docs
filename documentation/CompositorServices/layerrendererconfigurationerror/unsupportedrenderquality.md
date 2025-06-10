# LayerRendererConfigurationError.unsupportedRenderQuality

**Framework**: Compositor Services  
**Kind**: case

An error that indicates the configuration’s render quality is unsupported. This could be because foveation is disabled or the quality is outside of the valid range of [0, 1], the error `userInfo` will contain additional information.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case unsupportedRenderQuality
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror/unsupportedrenderquality)*