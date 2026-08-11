# init(cgAffineTransform:)

**Framework**: Core Image  
**Kind**: init

Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(cgAffineTransform t: CGAffineTransform)
```

#### Return Value

 An autoreleased [`CIVector`](civector.md) object of length 6.

#### Discussion

The `CGAffineTransform` structure’s `a`, `b`, `c`, `d`, `tx` and `ty` values are stored in the vector’s six values.

## Parameters

- `t`: The `CGAffineTransform` structure.

## See Also

- [convenience init(cgPoint: CGPoint)](civector/init(cgpoint:)-3mobm.md)
  Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [convenience init(cgRect: CGRect)](civector/init(cgrect:)-3undj.md)
  Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/init(cgaffinetransform:)-59e4k)*