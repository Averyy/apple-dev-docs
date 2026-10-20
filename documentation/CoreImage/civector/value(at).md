# value(at:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Returns a value from a specific position in the vector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func value(at index: Int) -> CGFloat
```

```objc
- (CGFloat) valueAtIndex:(size_t) index;
```

#### Return Value

 The value retrieved from the vector or `0` if the position is undefined.

#### Discussion

The numbering of elements in a vector begins with zero.

## Parameters

- `index`: The position in the vector of the value that you want to retrieve.

## See Also

### Getting Values From a Vector
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
- [var cgPointValue: CGPoint](./cgpointvalue.md)
  Returns the values in the vector as a `CGPoint` structure.
- [var cgRectValue: CGRect](./cgrectvalue.md)
  Returns the values in the vector as a `CGRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civector/value(at:))*