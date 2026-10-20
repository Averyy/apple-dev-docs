# init(x:y:z:w:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initialize a Core Image vector object with four values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)
```

```objc
- (instancetype) initWithX:(CGFloat) x Y:(CGFloat) y Z:(CGFloat) z W:(CGFloat) w;
```

#### Return Value

 An initialized [`CIVector`](../civector.md) object of length 4.

## Parameters

- `x`: The value for the first position in the vector.
- `y`: The value for the second position in the vector.
- `z`: The value for the third position in the vector.
- `w`: The value for the forth position in the vector.

## See Also

### Initializing a Vector
- [init(values: UnsafePointer<CGFloat>, count: Int)](./init%28values,count%29.md)
  Initialize a Core Image vector object with the specified the values.
- [convenience init(x: CGFloat)](./init%28x%29.md)
  Initialize a Core Image vector object with one value.
- [convenience init(x: CGFloat, y: CGFloat)](./init%28x,y%29-4grr.md)
  Initialize a Core Image vector object with two values.
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat)](./init%28x,y,z%29-zais.md)
  Initialize a Core Image vector object with three values.
- [convenience init(string: String)](./init%28string%29.md)
  Initialize a Core Image vector object with values provided in a string representation.
- [convenience init(cgAffineTransform: CGAffineTransform)](./init%28cgaffinetransform%29-6o8gl.md)
  Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](./init%28cgpoint%29-8cf9j.md)
  Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](./init%28cgrect%29-6bolw.md)
  Initialize a Core Image vector object with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(x:y:z:w:)-75emo)*