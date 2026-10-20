# height

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The extent of the pyramid along its y-axis. Animatable.

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
var height: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat height;
```

#### Discussion

The pyramid’s base is centered in its local coordinate system. For example, if you create a pyramid of height `10.0`, the y-coordinate of every point in its rectangular base is `0.0` and the y-coordinate of its apex is `10.0`. The default height is `1.0`. A height of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting a Pyramid’s Dimensions
- [var width: CGFloat](./width.md)
  The extent of the pyramid along its x-axis. Animatable.
- [var length: CGFloat](./length.md)
  The extent of the pyramid along its z-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnpyramid/height)*