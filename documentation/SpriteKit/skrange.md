# SKRange

**Framework**: SpriteKit  
**Kind**: class

A definition of a range of floating-point values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SKRange
```

#### Overview

You typically use a [`SKRange`](skrange.md) to clamp a value so that it is within the specified range.

## Topics

### Creating a Range Object
- [convenience init(value: CGFloat, variance: CGFloat)](skrange/init(value:variance:).md)
  Creates and initializes a new range object using a value and a maximum distance from that value.
- [class func withNoLimits() -> Self](skrange/withnolimits.md)
  Creates and initializes a new range object that encompasses all possible values.
- [convenience init(lowerLimit: CGFloat)](skrange/init(lowerlimit:).md)
  Creates and initializes a new range object that specifies only a minimum value.
- [convenience init(upperLimit: CGFloat)](skrange/init(upperlimit:).md)
  Creates and initializes a new range object that specifies only a maximum value.
- [convenience init(constantValue: CGFloat)](skrange/init(constantvalue:).md)
  Creates and initializes a new range object that specifies a constant value.
- [init(lowerLimit: CGFloat, upperLimit: CGFloat)](skrange/init(lowerlimit:upperlimit:).md)
  Initializes a new range object.
### Inspecting a Range Object’s Limits
- [var lowerLimit: CGFloat](skrange/lowerlimit.md)
  The minimum possible value.
- [var upperLimit: CGFloat](skrange/upperlimit.md)
  The maximum possible value.

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
- [class SKRegion](skregion.md)
  The definition of an arbitrary area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrange)*