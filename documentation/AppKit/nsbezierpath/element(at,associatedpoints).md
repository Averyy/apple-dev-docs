# element(at:associatedPoints:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Gets the element type and (and optionally) the associated points for the path element at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func element(at index: Int, associatedPoints points: NSPointArray?) -> NSBezierPath.ElementType
```

```objc
- (NSBezierPathElement) elementAtIndex:(NSInteger) index associatedPoints:(NSPointArray) points;
```

#### Return Value

The type of the path element. For a list of constants, see [`NSBezierPath.ElementType`](./elementtype.md).

#### Discussion

If you specify a value for the points parameter, your array must be large enough to hold the number of points for the given path element. Move, close path, and line segment commands return one point. Curve operations return three points.

For curve operations, the order of the points is controlPoint1 (`points`[0]), controlPoint2 (`points`[1]), endPoint (`points`[2]).

## Parameters

- `index`: The index of the desired path element.
- `points`: On input, a C-style array containing up to three `NSPoint` data types, or `NULL` if you do not want the points. On output, the data points associated with the specified path element.

## See Also

### Accessing Elements of a Path
- [var cgPath: CGPath](./cgpath.md)
- [var elementCount: Int](./elementcount.md)
  The total number of path elements in the path.
- [func element(at: Int) -> NSBezierPath.ElementType](./element%28at%29.md)
  Returns the type of path element at the specified index.
- [func removeAllPoints()](./removeallpoints%28%29.md)
  Removes all path elements from the path, effectively clearing the path.
- [func setAssociatedPoints(NSPointArray?, at: Int)](./setassociatedpoints%28_,at%29.md)
  Changes the points associated with the specified path element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/element(at:associatedpoints:))*