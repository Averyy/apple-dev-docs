# withNoLimits()

**Framework**: SpriteKit  
**Kind**: method

Creates and initializes a new range object that encompasses all possible values.

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
class func withNoLimits() -> Self
```

#### Return Value

A newly initialized range object whose minimum value is `—Inf` and whose maximum value is `+Inf`.

## See Also

- [convenience init(value: CGFloat, variance: CGFloat)](skrange/init(value:variance:).md)
  Creates and initializes a new range object using a value and a maximum distance from that value.
- [convenience init(lowerLimit: CGFloat)](skrange/init(lowerlimit:).md)
  Creates and initializes a new range object that specifies only a minimum value.
- [convenience init(upperLimit: CGFloat)](skrange/init(upperlimit:).md)
  Creates and initializes a new range object that specifies only a maximum value.
- [convenience init(constantValue: CGFloat)](skrange/init(constantvalue:).md)
  Creates and initializes a new range object that specifies a constant value.
- [init(lowerLimit: CGFloat, upperLimit: CGFloat)](skrange/init(lowerlimit:upperlimit:).md)
  Initializes a new range object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrange/withnolimits())*