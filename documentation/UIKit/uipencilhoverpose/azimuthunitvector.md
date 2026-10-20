# azimuthUnitVector

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A value that represents the azimuth unit vector of Apple Pencil in the specified view.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 26.2+

## Declaration

```swift
var azimuthUnitVector: CGVector { get }
```

```objc
@property (nonatomic, assign, readonly) CGVector azimuthUnitVector;
```

## See Also

### Getting the hover characteristics
- [var location: CGPoint](./location.md)
  The location of an Apple Pencil above the view’s bounds, in view’s coordinate space.
- [var altitudeAngle: CGFloat](./altitudeangle.md)
  A value that represents the altitude angle of Apple Pencil.
- [var azimuthAngle: CGFloat](./azimuthangle.md)
  A value that represents the azimuth angle of Apple Pencil.
- [var rollAngle: CGFloat](./rollangle.md)
  A value that represents the barrel-roll angle of Apple Pencil.
- [var zOffset: CGFloat](./zoffset.md)
  A value that represents the normalized distance between the screen and Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilhoverpose/azimuthunitvector)*