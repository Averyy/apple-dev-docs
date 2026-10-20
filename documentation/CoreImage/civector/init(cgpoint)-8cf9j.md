# init(cgPoint:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initialize a Core Image vector object with two values provided by a `CGPoint` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS

## Declaration

```swift
convenience init(cgPoint p: CGPoint)
```

```objc
- (instancetype) initWithCGPoint:(CGPoint) p;
```

#### Return Value

 An initialized [`CIVector`](../civector.md) object of length 2.

#### Discussion

The `CGRect` structure’s `y` and `y` values are stored in the vector’s two values.

## Parameters

- `p`: The `CGPoint` structure.

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
- [convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](./init%28x,y,z,w%29-75emo.md)
  Initialize a Core Image vector object with four values.
- [convenience init(string: String)](./init%28string%29.md)
  Initialize a Core Image vector object with values provided in a string representation.
- [convenience init(cgAffineTransform: CGAffineTransform)](./init%28cgaffinetransform%29-6o8gl.md)
  Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgRect: CGRect)](./init%28cgrect%29-6bolw.md)
  Initialize a Core Image vector object with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(cgpoint:)-8cf9j)*