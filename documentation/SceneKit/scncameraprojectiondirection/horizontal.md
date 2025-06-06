# SCNCameraProjectionDirection.horizontal

**Framework**: SceneKit  
**Kind**: case

The camera’s field of view or orthographic scale are measured horizontally.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case horizontal
```

#### Discussion

If a camera’s [`projectionDirection`](scncamera/projectiondirection.md) property has this value:

- The [`fieldOfView`](scncamera/fieldofview.md) property measures the horizontal viewing angle, and SceneKit automatically calculates the vertical angle according to the aspect ratio of the view presenting the scene.
- Or, if the camera uses an orthographic projection, the [`orthographicScale`](scncamera/orthographicscale.md) property measures the horizontal scale factor, and SceneKit automatically calculates the vertical factor according to  aspect ratio.

## See Also

- [SCNCameraProjectionDirection.vertical](scncameraprojectiondirection/vertical.md)
  The camera’s field of view or orthographic scale are measured vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncameraprojectiondirection/horizontal)*