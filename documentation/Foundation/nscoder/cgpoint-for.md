# cgPoint(for:)

**Framework**: Foundation  
**Kind**: method

Returns a Core Graphics point structure corresponding to the data in a given string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func cgPoint(for string: String) -> CGPoint
```

#### Return Value

A Core Graphics structure that represents a point. If the string is not well-formed, the function returns [`CGPointZero`](https://developer.apple.com/documentation/CoreGraphics/CGPointZero).

#### Discussion

In general, you should use this function only to convert strings that were previously created using the [`string(for:)`](nscoder/string(for:)-6ix86.md) function.

## Parameters

- `string`: A string whose contents are of the form “{ , }”, where   is the x coordinate and   is the y coordinate. The   and   values can represent integer or float values. An example of a valid string is @”{3.0,2.5}”. The string is not localized, so items are always separated with a comma.

## See Also

- [class func cgAffineTransform(for: String) -> CGAffineTransform](nscoder/cgaffinetransform(for:).md)
  Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [class func cgRect(for: String) -> CGRect](nscoder/cgrect(for:).md)
  Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [class func cgSize(for: String) -> CGSize](nscoder/cgsize(for:).md)
  Returns a Core Graphics size structure corresponding to the data in a given string.
- [class func cgVector(for: String) -> CGVector](nscoder/cgvector(for:).md)
  Returns a Core Graphics vector corresponding to the data in a given string.
- [class func nsDirectionalEdgeInsets(for: String) -> NSDirectionalEdgeInsets](nscoder/nsdirectionaledgeinsets(for:).md)
  Returns a directional edge insets structure based on data in the specified string.
- [class func uiEdgeInsets(for: String) -> UIEdgeInsets](nscoder/uiedgeinsets(for:).md)
  Returns a UIKit edge insets structure based on the data in the specified string.
- [class func uiOffset(for: String) -> UIOffset](nscoder/uioffset(for:).md)
  Returns a UIKit offset structure corresponding to the data in a given string.
- [class func string(for: CGRect) -> String](nscoder/string(for:)-4qz0a.md)
  Returns a string formatted to contain the data from a rectangle.
- [class func string(for: CGVector) -> String](nscoder/string(for:)-4omzv.md)
  Returns a string formatted to contain the data from a vector data structure.
- [class func string(for: CGAffineTransform) -> String](nscoder/string(for:)-6yx6n.md)
  Returns a string formatted to contain the data from an affine transform.
- [class func string(for: CGPoint) -> String](nscoder/string(for:)-6ix86.md)
  Returns a string formatted to contain the data from a point.
- [class func string(for: CGSize) -> String](nscoder/string(for:)-2f1xb.md)
  Returns a string formatted to contain the data from a size data structure.
- [class func string(for: NSDirectionalEdgeInsets) -> String](nscoder/string(for:)-hp8b.md)
  Returns a string formatted to contain the data from a directional edge insets structure.
- [class func string(for: UIEdgeInsets) -> String](nscoder/string(for:)-26b4z.md)
  Returns a string formatted to contain the data from an edge insets structure.
- [class func string(for: UIOffset) -> String](nscoder/string(for:)-454dj.md)
  Returns a string formatted to contain the data from an offset structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/cgpoint(for:))*