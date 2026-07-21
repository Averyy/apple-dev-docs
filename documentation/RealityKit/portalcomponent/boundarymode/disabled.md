# PortalComponent.BoundaryMode.disabled

**Framework**: RealityKit  
**Kind**: case

The portal renders without clipping or crossing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case disabled
```

#### Discussion

Portal world content is bounded only by the [`PortalMaterial`](portalmaterial.md) mesh. Entities with [`PortalCrossingComponent`](portalcrossingcomponent.md) don’t cross the portal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarymode/disabled)*