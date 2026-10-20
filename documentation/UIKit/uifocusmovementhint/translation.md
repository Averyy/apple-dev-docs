# translation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A vector to apply to a transform to match system interaction hinting.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var translation: CGVector { get }
```

```objc
@property (nonatomic, readonly) CGVector translation;
```

#### Discussion

This property represents an X,Y-axis translation expressed in points.

## See Also

### Transforming a hint
- [var interactionTransform: CATransform3D](./interactiontransform.md)
  A 3D transform that contains the combined transformations of perspective, rotation, and translation.
- [var perspectiveTransform: CATransform3D](./perspectivetransform.md)
  A 3D transform that represents a perspective matrix to be applied to match UIKit interaction hinting.
- [var rotation: CGVector](./rotation.md)
  A vector to apply to a transform to match system interaction hinting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusmovementhint/translation)*