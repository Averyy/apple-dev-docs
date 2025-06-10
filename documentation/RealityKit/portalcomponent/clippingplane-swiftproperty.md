# clippingPlane

**Framework**: RealityKit  
**Kind**: property

The clipping plane of the portal, using the entity’s local coordinates.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var clippingPlane: PortalComponent.ClippingPlane? { get set }
```

#### Discussion

When you define this property, the portal clips meshes inside the world, which are in front of the clipping plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/clippingplane-swift.property)*