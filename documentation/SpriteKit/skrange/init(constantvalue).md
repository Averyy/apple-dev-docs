# init(constantValue:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Creates and initializes a new range object that specifies a constant value.

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
convenience init(constantValue value: CGFloat)
```

```objc
+ (instancetype) rangeWithConstantValue:(CGFloat) value;
```

## Return Value

A newly initialized range object whose minimum and maximum value are both equal to `value`.

## Parameters

- `value`: A constant.

## See Also

### Creating a Range Object
- [convenience init(value: CGFloat, variance: CGFloat)](./init%28value,variance%29.md)
  Creates and initializes a new range object using a value and a maximum distance from that value.
- [class func withNoLimits() -> Self](./withnolimits%28%29.md)
  Creates and initializes a new range object that encompasses all possible values.
- [convenience init(lowerLimit: CGFloat)](./init%28lowerlimit%29.md)
  Creates and initializes a new range object that specifies only a minimum value.
- [convenience init(upperLimit: CGFloat)](./init%28upperlimit%29.md)
  Creates and initializes a new range object that specifies only a maximum value.
- [init(lowerLimit: CGFloat, upperLimit: CGFloat)](./init%28lowerlimit,upperlimit%29.md)
  Initializes a new range object.
- [+ rangeWithLowerLimit:upperLimit:](./rangewithlowerlimit_upperlimit_.md)
  Creates and initializes a new range object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skrange/init(constantvalue:))*