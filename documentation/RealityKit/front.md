# front

**Framework**: RealityKit

A vector that’s perpendicular to, and points outward from, the object’s face.

#### Overview

From the value of this property, the runtime calculates how much to spin the target object about the [`upVector`](upvector.md). This property is in local space, and so it’s relative to the target object’s coordinate space. The default value faces positively in the x-direction.

##### Declaration

```other
uniform vector3d front = (1.0, 0.0, 0.0)
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [upVector](upvector.md)
  A vector around which the runtime rotates the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/front)*