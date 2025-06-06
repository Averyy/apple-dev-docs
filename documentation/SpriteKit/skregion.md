# SKRegion

**Framework**: SpriteKit  
**Kind**: class

The definition of an arbitrary area.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class SKRegion
```

#### Overview

An [`SKRegion`](skregion.md) object defines a mathematical shape and is typically used to determine whether a particular point lies inside this area. For example, regions are used to define the area that a physics field can affect. Regions are defined using paths and mathematical shapes and can also be combined using constructive solid geometry.

## Topics

### Creating and Initializing Region Objects
- [class func infinite() -> Self](skregion/infinite.md)
  Returns a region that defines a region that includes all points.
- [init(size: CGSize)](skregion/init(size:).md)
  Initializes a new region with a rectangular area.
- [init(radius: Float)](skregion/init(radius:).md)
  Initializes a new region with a circular area.
- [init(path: CGPath)](skregion/init(path:).md)
  Initializes a new region using a Core Graphics path.
- [func inverse() -> Self](skregion/inverse.md)
  Returns a new region that is the mathematical inverse of an existing region.
- [func byDifference(from: SKRegion) -> Self](skregion/bydifference(from:).md)
  Returns a new region created by subtracting the contents of another region from this region.
- [func byIntersection(with: SKRegion) -> Self](skregion/byintersection(with:).md)
  Returns a new region created by intersecting the contents of this region with another region.
- [func byUnion(with: SKRegion) -> Self](skregion/byunion(with:).md)
  Returns a new region created by combining the contents of this region with another region.
### Interacting with a Region
- [var path: CGPath?](skregion/path.md)
  Returns a Core Graphics path that defines the region.
- [func contains(CGPoint) -> Bool](skregion/contains(_:).md)
  Returns a Boolean value that indicates whether a particular point is contained in the region.

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
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SKKeyframeSequence](skkeyframesequence.md)
  An object that performs interpolation between values specified at different times (keyframes).
- [class SKRange](skrange.md)
  A definition of a range of floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skregion)*