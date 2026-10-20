# init(cgPoint:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(cgPoint p: CGPoint)
```

```objc
+ (instancetype) vectorWithCGPoint:(CGPoint) p;
```

#### Return Value

 An autoreleased [`CIVector`](../civector.md) object of length 2.

#### Discussion

The `CGRect` structure’s `y` and `y` values are stored in the vector’s two values.

## Parameters

- `p`: The `CGPoint` structure.

## See Also

### Creating a Vector
- [convenience init(cgAffineTransform: CGAffineTransform)](./init%28cgaffinetransform%29-59e4k.md)
  Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgRect: CGRect)](./init%28cgrect%29-3undj.md)
  Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(cgpoint:)-3mobm)*