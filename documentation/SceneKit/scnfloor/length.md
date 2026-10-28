# length

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The extent of the floor along its z-axis. Animatable.

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

## Discussion

The floor is centered in its local coordinate system. For example, a floor of length `10.0` extends from `-5.0` to `5.0` along the z-axis. The default width is zero, indicating that the floor’s length is infinite.

You can animate changes to this property’s value. See `Animating SceneKit Content`.

## See Also

### Adjusting a Floor’s Size
- [var width: CGFloat](./width.md)
  The extent of the floor along its x-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfloor/length)*