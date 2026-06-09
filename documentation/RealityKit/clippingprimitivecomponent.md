# ClippingPrimitiveComponent

**Framework**: RealityKit  
**Kind**: struct

Use ClippingComponent instead

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ClippingPrimitiveComponent
```

## Topics

### Configuring clipping behavior
- [var shouldClipSelf: Bool](clippingprimitivecomponent/shouldclipself.md)
  Controls whether the entity itself is clipped by this component’s bounds.
- [var shouldClipChildren: Bool](clippingprimitivecomponent/shouldclipchildren.md)
  Controls whether child entities are clipped by this component’s bounds.
### Feathering clipped edges
- [var feather: ClippingPrimitiveComponent.Feather](clippingprimitivecomponent/feather-swift.property.md)
  The feathering configuration for the clipping boundaries.
- [ClippingPrimitiveComponent.Feather](clippingprimitivecomponent/feather-swift.struct.md)
  Configuration for feathering the clipping boundaries.
### Initializers
- [init()](clippingprimitivecomponent/init.md)
  Creates a Clipping Primitive Component with default settings.
### Instance Properties
- [var bounds: BoundingBox](clippingprimitivecomponent/bounds.md)
  The bounding box that defines the clipping region in the entity’s local coordinate space.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct RenderLayerComponent](renderlayercomponent.md)
  A component that defines which layers an entity participates in.
- [struct RenderLayer](renderlayer.md)
  A structured representation of render layers that provides type safety and clear semantics.
- [enum PortalFactory](portalfactory.md)
  A factory for creating portal entities with simplified configuration.
- [struct ClippingComponent](clippingcomponent.md)
  A component that clips entities and their children to a customizable bounding box volume with feathered edges.
- [struct OcclusionCullingComponent](occlusioncullingcomponent.md)
  A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clippingprimitivecomponent)*