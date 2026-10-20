# width

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The extent of the floor along its x-axis. Animatable.

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
var width: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat width;
```

#### Discussion

The floor is centered in its local coordinate system. For example, a floor of width `10.0` extends from `-5.0` to `5.0` along the x-axis. The default width is zero, indicating that the floor’s width is infinite.

You can animate changes to this property’s value. See `Animating SceneKit Content`.

## See Also

### Adjusting a Floor’s Size
- [var length: CGFloat](./length.md)
  The extent of the floor along its z-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfloor/width)*