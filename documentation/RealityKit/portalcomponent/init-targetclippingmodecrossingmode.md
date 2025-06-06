# init(target:clippingMode:crossingMode:)

**Framework**: RealityKit  
**Kind**: init

Creates a portal component with a target entity, clipping mode, and crossing mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(target: Entity, clippingMode: PortalComponent.ClippingMode, crossingMode: PortalComponent.CrossingMode)
```

#### Discussion

To render a portal, an entity needs a [`PortalComponent`](portalcomponent.md) and a [`ModelComponent`](modelcomponent.md), using one or more [`PortalMaterial`](portalmaterial.md) instances.

The target entity needs to have a [`WorldComponent`](worldcomponent.md) or the portal does not render.

Provide [`PortalComponent.ClippingMode`](portalcomponent/clippingmode-swift.enum.md) and [`PortalComponent.CrossingMode`](portalcomponent/crossingmode-swift.enum.md) to configure the corresponding clipping and crossing features.

Using this initializer is equivalent to setting [`targetEntity`](portalcomponent/targetentity.md), [`clippingMode`](portalcomponent/clippingmode-swift.property.md) and [`crossingMode`](portalcomponent/crossingmode-swift.property.md) properties directly.

See [`PortalComponent`](portalcomponent.md) for example usage.

## Parameters

- `target`: A target world entity the portal is looking into.
- `clippingMode`: A configuration for the portal’s clipping feature.
- `crossingMode`: A configuration for the portal’s crossing feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/init(target:clippingmode:crossingmode:))*