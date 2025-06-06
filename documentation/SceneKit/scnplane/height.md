# height

**Framework**: SceneKit  
**Kind**: property

The extent of the plane along its vertical axis. Animatable.

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
var height: CGFloat { get set }
```

#### Discussion

The plane is centered in its local coordinate system. For example, a plane of height `10.0` extends from `-5.0` to `5.0` along the y-axis. The default height is `1.0`. A height of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var width: CGFloat](scnplane/width.md)
  The extent of the plane along its horizontal axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnplane/height)*