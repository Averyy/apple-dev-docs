# init(size:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a rectangular region of the specified size.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(size: CGSize)
```

```objc
- (instancetype) initWithSize:(CGSize) size;
```

## Return Value

A rectangular region of the specified size.

## Discussion

The center of the rectangle is the origin of the region’s coordinate system.

## Parameters

- `size`: The size of the region, specified in points.

## See Also

### Creating and initializing regions
- [class var infinite: UIRegion](./infinite.md)
  Returns the region that encloses all points.
- [init(radius: CGFloat)](./init%28radius%29.md)
  Initializes and returns a region with a circular shape of the specified radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/init(size:))*