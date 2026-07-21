# viewLayer

**Framework**: ARKit  
**Kind**: property

The layer that displays the `ARFrame`, required before `viewRotationAngle` becomes available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
weak var viewLayer: CALayer? { get set }
```

#### Discussion

Assign the layer that presents the camera image. Renderers such as `ARSCNView`, `ARSKView`, `ARView`, and `RealityView` set this for you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/viewlayer)*