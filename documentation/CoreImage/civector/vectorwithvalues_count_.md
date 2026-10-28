# vectorWithValues:count:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Create a Core Image vector object that is initialized with the specified values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) vectorWithValues:(const CGFloat *) values count:(size_t) count;
```

## Return Value

 An autoreleased [`CIVector`](../civector.md) object of length `count`.

## Parameters

- `values`: The pointer `CGFloat` values to initialize the vector with.
- `count`: The number of `CGFloats` specified by the `values` parameter.

## See Also

### Creating a Vector
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
- [convenience init(cgAffineTransform: CGAffineTransform)](./init%28cgaffinetransform%29-59e4k.md)
  Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](./init%28cgpoint%29-3mobm.md)
  Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](./init%28cgrect%29-3undj.md)
  Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/vectorwithvalues:count:)*