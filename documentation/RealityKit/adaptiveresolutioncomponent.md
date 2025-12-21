# AdaptiveResolutionComponent

**Framework**: RealityKit  
**Kind**: struct

A component that provides the suggested pixels per meter necessary to render an object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct AdaptiveResolutionComponent
```

#### Overview

Use the [`pixelsPerMeter`](adaptiveresolutioncomponent/pixelspermeter.md) property to proactively update your scene to disable expensive systems and high-resolution content that is far away.

> **Note**: `pixelsPerMeter` is binned to protect user privacy.

## Topics

### Initializers
- [init()](adaptiveresolutioncomponent/init.md)
  Creates a new instance of the adaptive resolution component.
### Instance Properties
- [var pixelsPerMeter: Float](adaptiveresolutioncomponent/pixelspermeter.md)
  A read-only value representing the suggested pixels per meter necessary to render an object.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct ModelSortGroupComponent](modelsortgroupcomponent.md)
  A component that configures the rendering order for an entity’s model.
- [struct ModelSortGroup](modelsortgroup.md)
  A group that you assign to multiple entities to tell the renderer what order and how to render the entities in the group.
- [struct OpacityComponent](opacitycomponent.md)
  A component that controls the opacity of an entity and its descendants.
- [struct ModelDebugOptionsComponent](modeldebugoptionscomponent.md)
  A component that changes how RealityKit renders its entity to help with debugging.
- [struct MeshInstancesComponent](meshinstancescomponent.md)
  A component that performs GPU instancing on the model of the same entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/adaptiveresolutioncomponent)*