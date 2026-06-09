# fixed(_:bias:)

**Framework**: RealityKit  
**Kind**: method

Specify a fixed number of shadow cascades to use.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func fixed(_ count: Int, bias: Float = 0.0) -> DirectionalLightComponent.Shadow.Cascades
```

#### Discussion

Accepted values are 1, 2, 3, and 4.

The optional `bias` parameter can be used to shift the cascade splits (where one cascade ends and the next begins) closer to or farther from the camera, useful in viewing configurations where more shadow resolution is desired near to or far from the viewer. The valid range of this parameter is `(-1.0, 1.0)`, where `-1.0` maps the first cascade split onto the near plane and `1.0` moves the last cascade split to the far plane. The default value is `0.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/cascades-swift.struct/fixed(_:bias:))*