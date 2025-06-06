# init(radius:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a region with a circular shape of the specified radius.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(radius: CGFloat)
```

#### Return Value

A circular region with the specified radius.

#### Discussion

The center of the circle is the origin of the region’s coordinate system.

## Parameters

- `radius`: The radius of the circular area, specified in points.

## See Also

- [class var infinite: UIRegion](uiregion/infinite.md)
  Returns the region that encloses all points.
- [init(size: CGSize)](uiregion/init(size:).md)
  Initializes and returns a rectangular region of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/init(radius:))*