# zOffset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A value that represents the normalized distance between the screen and Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 26.2+

## Declaration

```swift
var zOffset: CGFloat { get }
```

```objc
@property (nonatomic, assign, readonly) CGFloat zOffset;
```

## See Also

### Getting the hover characteristics
- [var location: CGPoint](./location.md)
  The location of an Apple Pencil above the view’s bounds, in view’s coordinate space.
- [var altitudeAngle: CGFloat](./altitudeangle.md)
  A value that represents the altitude angle of Apple Pencil.
- [var azimuthAngle: CGFloat](./azimuthangle.md)
  A value that represents the azimuth angle of Apple Pencil.
- [var azimuthUnitVector: CGVector](./azimuthunitvector.md)
  A value that represents the azimuth unit vector of Apple Pencil in the specified view.
- [var rollAngle: CGFloat](./rollangle.md)
  A value that represents the barrel-roll angle of Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilhoverpose/zoffset)*