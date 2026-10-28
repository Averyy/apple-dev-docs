# SCNCameraProjectionDirection.vertical

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

The camera’s field of view or orthographic scale are measured vertically.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
case vertical
```

```c
SCNCameraProjectionDirectionVertical
```

## Discussion

If a camera’s [`projectionDirection`](../scncamera/projectiondirection.md) property has this value:

- The [`fieldOfView`](../scncamera/fieldofview.md) property measures the vertical viewing angle, and SceneKit automatically calculates the horizontal angle according to the aspect ratio of the view presenting the scene.
- Or, if the camera uses an orthographic projection, the [`orthographicScale`](../scncamera/orthographicscale.md) property measures the vertical scale factor, and SceneKit automatically calculates the horizontal factor according to  aspect ratio.

## See Also

### Projection Directions
- [SCNCameraProjectionDirection.horizontal](./horizontal.md)
  The camera’s field of view or orthographic scale are measured horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncameraprojectiondirection/vertical)*