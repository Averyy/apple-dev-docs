# height

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The extent of the box along its y-axis. Animatable.

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

The box is centered in its local coordinate system. For example, a box of height `10.0` extends from `-5.0` to `5.0` along the y-axis. The default width is `1.0`. A height of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting a Box’s Dimensions
- [var width: CGFloat](./width.md)
  The extent of the box along its x-axis. Animatable.
- [var length: CGFloat](./length.md)
  The extent of the box along its z-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbox/height)*