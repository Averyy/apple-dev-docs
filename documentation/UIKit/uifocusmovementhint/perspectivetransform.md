# perspectiveTransform

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A 3D transform that represents a perspective matrix to be applied to match UIKit interaction hinting.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var perspectiveTransform: CATransform3D { get }
```

```objc
@property (nonatomic, readonly) CATransform3D perspectiveTransform;
```

## See Also

### Transforming a hint
- [var interactionTransform: CATransform3D](./interactiontransform.md)
  A 3D transform that contains the combined transformations of perspective, rotation, and translation.
- [var rotation: CGVector](./rotation.md)
  A vector to apply to a transform to match system interaction hinting.
- [var translation: CGVector](./translation.md)
  A vector to apply to a transform to match system interaction hinting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusmovementhint/perspectivetransform)*