# UIRegion

**Framework**: UIKit  
**Kind**: class

A shape for use in UIKit Dynamics.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIRegion
```

#### Overview

When creating animations, you use regions to define the effective area of a field behavior such as a magnetic or gravitational force. Most regions are rectangular or elliptical in shape, but you can use the methods of this class to create more complex shapes by adding, subtracting, and intersecting other regions.

When creating a new region, you specify only the size of the corresponding rectangle or circle. The origin of a newly created region is at the center of the specified area, and any mathematical manipulations you make to the region occur relative to that origin point.

## Topics

### Creating and initializing regions
- [class var infinite: UIRegion](uiregion/infinite.md)
  Returns the region that encloses all points.
- [init(size: CGSize)](uiregion/init(size:).md)
  Initializes and returns a rectangular region of the specified size.
- [init(radius: CGFloat)](uiregion/init(radius:).md)
  Initializes and returns a region with a circular shape of the specified radius.
### Creating complex regions
- [func inverse() -> Self](uiregion/inverse.md)
  Returns a new region that’s the mathematical inverse of the current region.
- [func byDifference(from: UIRegion) -> Self](uiregion/bydifference(from:).md)
  Returns a new region created by subtracting the specified region from the current region.
- [func byIntersection(with: UIRegion) -> Self](uiregion/byintersection(with:).md)
  Returns a new region containing only the area occupied by both the specified region and current region.
- [func byUnion(with: UIRegion) -> Self](uiregion/byunion(with:).md)
  Returns a new region containing the combined areas of the specified region and the current region.
### Interacting with a region
- [func contains(CGPoint) -> Bool](uiregion/contains(_:).md)
  Returns a Boolean indicating whether the specified point is inside of the current region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion)*