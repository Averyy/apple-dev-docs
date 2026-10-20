# length

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The extent of the pyramid along its z-axis. Animatable.

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
var length: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat length;
```

#### Discussion

The pyramid is centered in its local coordinate system, and the width and length of the pyramid are the dimensions of its rectangular base. For example, a pyramid of length `10.0` extends from `-5.0` to `5.0` along the z-axis. The default length is `1.0`. A length of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting a Pyramid’s Dimensions
- [var width: CGFloat](./width.md)
  The extent of the pyramid along its x-axis. Animatable.
- [var height: CGFloat](./height.md)
  The extent of the pyramid along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnpyramid/length)*