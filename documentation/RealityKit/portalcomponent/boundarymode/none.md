# PortalComponent.BoundaryMode.none

**Framework**: RealityKit  
**Kind**: case

The portal renders without clipping or crossing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case none
```

#### Discussion

Portal world content is bounded only by the [`PortalMaterial`](portalmaterial.md) mesh. Entities with [`PortalCrossingComponent`](portalcrossingcomponent.md) don’t cross the portal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarymode/none)*