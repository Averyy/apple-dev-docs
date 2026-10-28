# SKRegion

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface SKRegion : NSObject
```

## Overview

An [`SKRegion`](./skregion.md) object defines a mathematical shape and is typically used to determine whether a particular point lies inside this area. For example, regions are used to define the area that a physics field can affect. Regions are defined using paths and mathematical shapes and can also be combined using constructive solid geometry.

## Topics

### Creating and Initializing Region Objects
- [class func infinite() -> Self](./skregion/infinite%28%29.md)
  Returns a region that defines a region that includes all points.
- [init(size: CGSize)](./skregion/init%28size%29.md)
  Initializes a new region with a rectangular area.
- [init(radius: Float)](./skregion/init%28radius%29.md)
  Initializes a new region with a circular area.
- [init(path: CGPath)](./skregion/init%28path%29.md)
  Initializes a new region using a Core Graphics path.
- [func inverse() -> Self](./skregion/inverse%28%29.md)
  Returns a new region that is the mathematical inverse of an existing region.
- [func byDifference(from: SKRegion) -> Self](./skregion/bydifference%28from%29.md)
  Returns a new region created by subtracting the contents of another region from this region.
- [func byIntersection(with: SKRegion) -> Self](./skregion/byintersection%28with%29.md)
  Returns a new region created by intersecting the contents of this region with another region.
- [func byUnion(with: SKRegion) -> Self](./skregion/byunion%28with%29.md)
  Returns a new region created by combining the contents of this region with another region.
### Interacting with a Region
- [var path: CGPath?](./skregion/path.md)
  Returns a Core Graphics path that defines the region.
- [func contains(CGPoint) -> Bool](./skregion/contains%28_%29.md)
  Returns a Boolean value that indicates whether a particular point is contained in the region.
### Initializers
- [init?(coder: NSCoder)](./skregion/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Mathematical Tools
- [class SKKeyframeSequence](./skkeyframesequence.md)
  An object that performs interpolation between values specified at different times (keyframes).
- [class SKRange](./skrange.md)
  A definition of a range of floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skregion)*