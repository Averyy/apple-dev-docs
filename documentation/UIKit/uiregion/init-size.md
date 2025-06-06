# init(size:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a rectangular region of the specified size.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(size: CGSize)
```

#### Return Value

A rectangular region of the specified size.

#### Discussion

The center of the rectangle is the origin of the region’s coordinate system.

## Parameters

- `size`: The size of the region, specified in points.

## See Also

- [class var infinite: UIRegion](uiregion/infinite.md)
  Returns the region that encloses all points.
- [init(radius: CGFloat)](uiregion/init(radius:).md)
  Initializes and returns a region with a circular shape of the specified radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/init(size:))*