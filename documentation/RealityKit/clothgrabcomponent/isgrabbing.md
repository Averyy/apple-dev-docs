# isGrabbing

**Framework**: RealityKit  
**Kind**: property

Indicates whether particles are currently being grabbed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isGrabbing: Bool
```

#### Discussion

When first set to `true`, a selection of particles is made using the ray or volume. In the following frames, all selected particles will be dragged around until this value is set back to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothgrabcomponent/isgrabbing)*