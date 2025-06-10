# width

**Framework**: SceneKit  
**Kind**: property

The extent of the box along its x-axis. Animatable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var width: CGFloat { get set }
```

#### Discussion

The box is centered in its local coordinate system. For example, a box of width `10.0` extends from `-5.0` to `5.0` along the x-axis. The default width is `1.0`. A width of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var height: CGFloat](scnbox/height.md)
  The extent of the box along its y-axis. Animatable.
- [var length: CGFloat](scnbox/length.md)
  The extent of the box along its z-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbox/width)*