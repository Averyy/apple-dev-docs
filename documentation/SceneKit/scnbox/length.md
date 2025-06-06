# length

**Framework**: SceneKit  
**Kind**: property

The extent of the box along its z-axis. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var length: CGFloat { get set }
```

#### Discussion

The box is centered in its local coordinate system. For example, a box of length `10.0` extends from `-5.0` to `5.0` along the z-axis. The default width is `1.0`. A length of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var width: CGFloat](scnbox/width.md)
  The extent of the box along its x-axis. Animatable.
- [var height: CGFloat](scnbox/height.md)
  The extent of the box along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbox/length)*