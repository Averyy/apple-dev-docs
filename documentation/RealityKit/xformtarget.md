# xformTarget

**Framework**: RealityKit

A prim that provides the transform to which this action animates.

#### Overview

To provide a transform, assign an [`Xformable`](https://developer.apple.comhttps://graphics.pixar.com/usd/docs/api/class_usd_geom_xformable.html) prim to this property.

The prims in the list of [`affectedObjects`](affectedobjects.md) animate from their current transform to the transform that this prim specifies. Include in the prim the transformational operations that implement the transform animation. For more information, see [`xformOp`](https://developer.apple.comhttps://graphics.pixar.com/usd/docs/api/class_usd_geom_xform_op.html).

##### Declaration

```other
rel xformTarget
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [type](type.md)
  An option that controls the order in which the actions execute.
- [easeType](easetype.md)
  An option that describes the animation’s change in pace over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/xformtarget)*