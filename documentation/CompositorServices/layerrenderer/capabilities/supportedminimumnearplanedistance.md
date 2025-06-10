# supportedMinimumNearPlaneDistance

**Framework**: Compositor Services  
**Kind**: property

The minimum distance in meters to the layer’s near projection plane.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var supportedMinimumNearPlaneDistance: Float { get }
```

#### Discussion

Compositor Services uses the near and far projection planes to compute the perspective projection matrix and to clip content that’s too close to the camera, or too far from it. This property stores the minimum distance to the near plane that the layer allows. When you configure your layer, you can specify a different near-plane distance, but that value must be greater than or equal to the minimum distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/supportedminimumnearplanedistance)*