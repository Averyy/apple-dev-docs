# init(cgRect:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(cgRect r: CGRect)
```

```objc
+ (instancetype) vectorWithCGRect:(CGRect) r;
```

## Return Value

 An autoreleased [`CIVector`](../civector.md) object of length 4.

## Discussion

The `CGRect` structure’s `x`, `y`, `height` and `width` values are stored in the vector’s four values.

## Parameters

- `r`: The `CGRect` structure.

## See Also

### Creating a Vector
- [convenience init(cgAffineTransform: CGAffineTransform)](./init%28cgaffinetransform%29-59e4k.md)
  Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](./init%28cgpoint%29-3mobm.md)
  Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [+ vectorWithValues:count:](./vectorwithvalues_count_.md)
  Create a Core Image vector object that is initialized with the specified values.
- [+ vectorWithX:](./vectorwithx_.md)
  Create a Core Image vector object that is initialized with one value.
- [+ vectorWithX:Y:](./vectorwithx_y_.md)
  Create a Core Image vector object that is initialized with two values.
- [+ vectorWithX:Y:Z:](./vectorwithx_y_z_.md)
  Create a Core Image vector object that is initialized with three values.
- [+ vectorWithX:Y:Z:W:](./vectorwithx_y_z_w_.md)
  Create a Core Image vector object that is initialized with four values.
- [+ vectorWithString:](./vectorwithstring_.md)
  Create a Core Image vector object with values provided in a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(cgrect:)-3undj)*