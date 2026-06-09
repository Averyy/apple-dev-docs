# createPortal(world:portalEntity:style:enableClipping:enableCrossing:)

**Framework**: RealityKit  
**Kind**: method

Creates a portal targeting an existing world entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func createPortal(world: Entity, portalEntity: Entity? = nil, style: PortalFactory.Style, enableClipping: Bool = true, enableCrossing: Bool = false) -> PortalFactory.PortalSetup
```

#### Return Value

A `PortalSetup` containing the root entity with configured portal and world.

#### Discussion

Use this method when you want multiple portals to view the same world, or when you need to configure the world entity before creating the portal.

> **Note**: The `world` entity must have a `WorldComponent`.

#### Example

```swift
// Create a shared world
let sharedWorld = Entity()
sharedWorld.components.set(WorldComponent())

// Create two portals viewing the same world
let portal1 = PortalFactory.createPortal(
    world: sharedWorld,
    style: .plane(width: 1.0, height: 1.0)
)

let portal2 = PortalFactory.createPortal(
    world: sharedWorld,
    style: .plane(width: 1.5, height: 1.5)
)

// Add both portals to scene
content.add(portal1.rootEntity)
content.add(portal2.rootEntity)
```

## Parameters

- `world`: An entity with `WorldComponent`. This entity must already have a `WorldComponent` attached, or the method will fail with a precondition.
- `portalEntity`: An optional entity to configure as the portal. If `nil`, a new entity is created. If provided, any existing `ModelComponent` and `PortalComponent` will be replaced. Default is `nil`.
- `style`: The visual style and geometry of the portal.
- `enableClipping`: When `true`, content is clipped at the portal boundary. Default is `true`.
- `enableCrossing`: When `true`, enables portal crossing for entities with `PortalCrossingComponent`. Default is `false`.

## See Also

- [static func createPortal(style: PortalFactory.Style, enableClipping: Bool, enableCrossing: Bool) -> PortalFactory.PortalSetup](portalfactory/createportal(style:enableclipping:enablecrossing:).md)
  Creates a complete portal setup with new entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalfactory/createportal(world:portalentity:style:enableclipping:enablecrossing:))*