# cgAffineTransform(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a Core Graphics affine transform structure corresponding to the data in a given string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func cgAffineTransform(for string: String) -> CGAffineTransform
```

#### Return Value

A Core Graphics affine transform structure. If the string is not well-formed, the function returns the identity transform.

#### Discussion

In general, you should use this function only to convert strings that were previously created using the [`string(for:)`](./string%28for%29-6yx6n.md) function.

## Parameters

- `string`: A string whose contents are of the form “{*a*, *b*, *c*, *d*, *tx*, *ty*}”, where *a*, *b*, *c*, *d*, *tx*, and *ty* are the floating-point component values of the [CGAffineTransform](../../CoreGraphics/cgaffinetransform.md) data structure. An example of a valid string is @”{1,0,0,1,2.5,3.0}”. The string is not localized, so items are always separated with a comma. For information about the position of each value in the transform array, see [CGAffineTransform](../../CoreGraphics/cgaffinetransform.md).

## See Also

### Representing Geometric Types as Strings
- [class func cgPoint(for: String) -> CGPoint](./cgpoint%28for%29.md)
  Returns a Core Graphics point structure corresponding to the data in a given string.
- [class func cgRect(for: String) -> CGRect](./cgrect%28for%29.md)
  Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [class func cgSize(for: String) -> CGSize](./cgsize%28for%29.md)
  Returns a Core Graphics size structure corresponding to the data in a given string.
- [class func cgVector(for: String) -> CGVector](./cgvector%28for%29.md)
  Returns a Core Graphics vector corresponding to the data in a given string.
- [class func nsDirectionalEdgeInsets(for: String) -> NSDirectionalEdgeInsets](./nsdirectionaledgeinsets%28for%29.md)
  Returns a directional edge insets structure based on data in the specified string.
- [class func uiEdgeInsets(for: String) -> UIEdgeInsets](./uiedgeinsets%28for%29.md)
  Returns a UIKit edge insets structure based on the data in the specified string.
- [class func uiOffset(for: String) -> UIOffset](./uioffset%28for%29.md)
  Returns a UIKit offset structure corresponding to the data in a given string.
- [class func string(for: CGRect) -> String](./string%28for%29-4qz0a.md)
  Returns a string formatted to contain the data from a rectangle.
- [class func string(for: CGVector) -> String](./string%28for%29-4omzv.md)
  Returns a string formatted to contain the data from a vector data structure.
- [class func string(for: CGAffineTransform) -> String](./string%28for%29-6yx6n.md)
  Returns a string formatted to contain the data from an affine transform.
- [class func string(for: CGPoint) -> String](./string%28for%29-6ix86.md)
  Returns a string formatted to contain the data from a point.
- [class func string(for: CGSize) -> String](./string%28for%29-2f1xb.md)
  Returns a string formatted to contain the data from a size data structure.
- [class func string(for: NSDirectionalEdgeInsets) -> String](./string%28for%29-hp8b.md)
  Returns a string formatted to contain the data from a directional edge insets structure.
- [class func string(for: UIEdgeInsets) -> String](./string%28for%29-26b4z.md)
  Returns a string formatted to contain the data from an edge insets structure.
- [class func string(for: UIOffset) -> String](./string%28for%29-454dj.md)
  Returns a string formatted to contain the data from an offset structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/cgaffinetransform(for:))*