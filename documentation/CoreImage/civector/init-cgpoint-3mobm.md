# init(cgPoint:)

**Framework**: Core Image  
**Kind**: init

Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(cgPoint p: CGPoint)
```

#### Return Value

 An autoreleased [`CIVector`](civector.md) object of length 2.

#### Discussion

The `CGRect` structure’s `y` and `y` values are stored in the vector’s two values.

## Parameters

- `p`: The `CGPoint` structure.

## See Also

- [convenience init(cgAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:)-59e4k.md)
  Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgRect: CGRect)](civector/init(cgrect:)-3undj.md)
  Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(cgpoint:)-3mobm)*