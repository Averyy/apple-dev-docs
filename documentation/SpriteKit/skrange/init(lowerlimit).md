# init(lowerLimit:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates and initializes a new range object that specifies only a minimum value.

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
convenience init(lowerLimit lower: CGFloat)
```

```objc
+ (instancetype) rangeWithLowerLimit:(CGFloat) lower;
```

## Return Value

A newly initialized range object whose minimum value is `lower` and whose maximum value is `+Inf`.

## Parameters

- `lower`: The minimum value for the range.

## See Also

### Creating a Range Object
- [convenience init(value: CGFloat, variance: CGFloat)](./init%28value,variance%29.md)
  Creates and initializes a new range object using a value and a maximum distance from that value.
- [class func withNoLimits() -> Self](./withnolimits%28%29.md)
  Creates and initializes a new range object that encompasses all possible values.
- [convenience init(upperLimit: CGFloat)](./init%28upperlimit%29.md)
  Creates and initializes a new range object that specifies only a maximum value.
- [convenience init(constantValue: CGFloat)](./init%28constantvalue%29.md)
  Creates and initializes a new range object that specifies a constant value.
- [init(lowerLimit: CGFloat, upperLimit: CGFloat)](./init%28lowerlimit,upperlimit%29.md)
  Initializes a new range object.
- [+ rangeWithLowerLimit:upperLimit:](./rangewithlowerlimit_upperlimit_.md)
  Creates and initializes a new range object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrange/init(lowerlimit:))*