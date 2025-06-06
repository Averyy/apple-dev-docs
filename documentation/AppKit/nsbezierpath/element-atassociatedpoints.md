# element(at:associatedPoints:)

**Framework**: AppKit  
**Kind**: method

Gets the element type and (and optionally) the associated points for the path element at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
func element(at index: Int, associatedPoints points: NSPointArray?) -> NSBezierPath.ElementType
```

#### Return Value

The type of the path element. For a list of constants, see [`NSBezierPath.ElementType`](nsbezierpath/elementtype.md).

#### Discussion

If you specify a value for the points parameter, your array must be large enough to hold the number of points for the given path element. Move, close path, and line segment commands return one point. Curve operations return three points.

For curve operations, the order of the points is controlPoint1 (`points`[0]), controlPoint2 (`points`[1]), endPoint (`points`[2]).

## Parameters

- `index`: The index of the desired path element.
- `points`: On input, a C-style array containing up to three   data types, or   if you do not want the points. On output, the data points associated with the specified path element.

## See Also

- [var cgPath: CGPath](nsbezierpath/cgpath.md)
- [var elementCount: Int](nsbezierpath/elementcount.md)
  The total number of path elements in the path.
- [func element(at: Int) -> NSBezierPath.ElementType](nsbezierpath/element(at:).md)
  Returns the type of path element at the specified index.
- [func removeAllPoints()](nsbezierpath/removeallpoints.md)
  Removes all path elements from the path, effectively clearing the path.
- [func setAssociatedPoints(NSPointArray?, at: Int)](nsbezierpath/setassociatedpoints(_:at:).md)
  Changes the points associated with the specified path element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/element(at:associatedpoints:))*