# createPortal(style:enableClipping:enableCrossing:)

**Framework**: RealityKit  
**Kind**: method

Creates a complete portal setup with new entities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func createPortal(style: PortalFactory.Style, enableClipping: Bool = true, enableCrossing: Bool = false) -> PortalFactory.PortalSetup
```

#### Return Value

A `PortalSetup` containing the root entity with configured portal and world.

#### Discussion

This method creates a root entity containing a portal entity and a world entity. The portal entity has a `ModelComponent` with generated mesh and `PortalMaterial`, plus a `PortalComponent` with specified clipping and crossing modes. The world entity has a `WorldComponent` and is set as the portal’s target.

#### Example

```swift
// Create a flat portal with default settings
let setup = PortalFactory.createPortal(
    style: .plane(width: 2.0, height: 1.5)
)

// Add the portal to your scene
content.add(setup.rootEntity)

// Add content to the portal world
let sphere = ModelEntity(mesh: .generateSphere(radius: 0.3), materials: [SimpleMaterial()])
setup.worldEntity.addChild(sphere)
```

## Parameters

- `style`: The visual style and geometry of the portal.
- `enableClipping`: When `true`, content is clipped at the portal boundary. Prevents content from rendering outside the portal bounds. Default is `true`.
- `enableCrossing`: When `true`, enables portal crossing for entities with `PortalCrossingComponent`. Allows entities to move between the portal world and the outside world. Default is `false`.

## See Also

- [static func createPortal(world: Entity, portalEntity: Entity?, style: PortalFactory.Style, enableClipping: Bool, enableCrossing: Bool) -> PortalFactory.PortalSetup](portalfactory/createportal(world:portalentity:style:enableclipping:enablecrossing:).md)
  Creates a portal targeting an existing world entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalfactory/createportal(style:enableclipping:enablecrossing:))*