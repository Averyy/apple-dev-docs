# cgPointValue

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

Returns the values in the vector as a `CGPoint` structure.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var cgPointValue: CGPoint { get }
```

```objc
@property (readonly) CGPoint CGPointValue;
```

#### Return Value

 Reading this property returns a `CGPoint` structure from the `X` and `Y` values from the vector.

## See Also

### Getting Values From a Vector
- [func value(at: Int) -> CGFloat](./value%28at%29.md)
  Returns a value from a specific position in the vector.
- [var count: Int](./count.md)
  The number of items in the vector.
- [var x: CGFloat](./x.md)
  The value located in the first position in the vector.
- [var y: CGFloat](./y.md)
  The value located in the second position in the vector.
- [var z: CGFloat](./z.md)
  The value located in the third position in the vector.
- [var w: CGFloat](./w.md)
  The value located in the forth position in the vector.
- [var stringRepresentation: String](./stringrepresentation.md)
  Returns a formatted string with all the values of a `CIVector`.
- [var cgAffineTransformValue: CGAffineTransform](./cgaffinetransformvalue.md)
  Returns the values in the vector as a `CGAffineTransformValue` structure.
- [var cgRectValue: CGRect](./cgrectvalue.md)
  Returns the values in the vector as a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/cgpointvalue)*