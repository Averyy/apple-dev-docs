# lightingBlendDistance

**Framework**: RealityKit  
**Kind**: property

The distance over which crossing-entity lighting blends between the host scene and the portal world.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.0+
- macOS 27.0+ (Beta)
- tvOS 26.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
var lightingBlendDistance: Float { get set }
```

#### Discussion

As an entity with [`PortalCrossingComponent`](portalcrossingcomponent.md) crosses the portal boundary, RealityKit transitions its lighting from the host scene’s environment to the portal world’s environment. This property controls the width, in meters, of that transition:

- A value of `0` produces a sharp lighting boundary, with the entity fully lit by the portal world on the inside and the host scene on the outside.
- A positive value produces a smooth gradient that spans the given distance into the portal world, portal crossing entities are unaffected by this value.

The boundary used for the distance calculation is the geometry you configure with [`crossingMode`](portalcomponent/crossingmode-swift.property.md): a plane for [`PortalComponent.CrossingMode.plane(_:)`](portalcomponent/crossingmode-swift.enum/plane(_:).md), or a box for [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md).

> **Note**: This property only affects rendering when [`crossingMode`](portalcomponent/crossingmode-swift.property.md) is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/lightingblenddistance)*