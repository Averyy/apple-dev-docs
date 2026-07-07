# init(cgRect:)

**Framework**: Core Image  
**Kind**: init

Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(cgRect r: CGRect)
```

#### Return Value

 An autoreleased [`CIVector`](civector.md) object of length 4.

#### Discussion

The `CGRect` structure’s `x`, `y`, `height` and `width` values are stored in the vector’s four values.

## Parameters

- `r`: The `CGRect` structure.

## See Also

- [convenience init(cgAffineTransform: CGAffineTransform)](civector/init(cgaffinetransform:)-59e4k.md)
  Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [convenience init(cgPoint: CGPoint)](civector/init(cgpoint:)-3mobm.md)
  Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(cgrect:)-3undj)*