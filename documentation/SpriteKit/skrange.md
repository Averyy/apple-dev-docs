# SKRange

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A definition of a range of floating-point values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class SKRange
```

```objc
@interface SKRange : NSObject
```

#### Overview

You typically use a [`SKRange`](./skrange.md) to clamp a value so that it is within the specified range.

## Topics

### Creating a Range Object
- [convenience init(value: CGFloat, variance: CGFloat)](./skrange/init%28value,variance%29.md)
  Creates and initializes a new range object using a value and a maximum distance from that value.
- [class func withNoLimits() -> Self](./skrange/withnolimits%28%29.md)
  Creates and initializes a new range object that encompasses all possible values.
- [convenience init(lowerLimit: CGFloat)](./skrange/init%28lowerlimit%29.md)
  Creates and initializes a new range object that specifies only a minimum value.
- [convenience init(upperLimit: CGFloat)](./skrange/init%28upperlimit%29.md)
  Creates and initializes a new range object that specifies only a maximum value.
- [convenience init(constantValue: CGFloat)](./skrange/init%28constantvalue%29.md)
  Creates and initializes a new range object that specifies a constant value.
- [init(lowerLimit: CGFloat, upperLimit: CGFloat)](./skrange/init%28lowerlimit,upperlimit%29.md)
  Initializes a new range object.
- [+ rangeWithLowerLimit:upperLimit:](./skrange/rangewithlowerlimit_upperlimit_.md)
  Creates and initializes a new range object.
### Inspecting a Range Object’s Limits
- [var lowerLimit: CGFloat](./skrange/lowerlimit.md)
  The minimum possible value.
- [var upperLimit: CGFloat](./skrange/upperlimit.md)
  The maximum possible value.
### Initializers
- [init?(coder: NSCoder)](./skrange/init%28coder%29.md)

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
- [class SKRegion](./skregion.md)
  The definition of an arbitrary area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrange)*