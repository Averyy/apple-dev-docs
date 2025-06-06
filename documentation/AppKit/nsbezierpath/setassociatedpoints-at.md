# setAssociatedPoints(_:at:)

**Framework**: Appkit  
**Kind**: method

Changes the points associated with the specified path element.

**Availability**:
- macOS ?+

## Declaration

```swift
func setAssociatedPoints(_ points: NSPointArray?, at index: Int)
```

#### Discussion

You can use this method to change the points associated with a path quickly and without recreating the path. You cannot use this method to change the type of the path element.

The following example shows you how you would modify the point associated with a line path element. The path created by this example results in a path with two elements. The first path element specifies a move to point (0, 0) while the second creates a line to point (100, 100). It then changes the line to go only to the point (50,50) using this method:

```objc
NSBezierPath *bezierPath = [NSBezierPath bezierPath];
NSPoint newPoint = NSMakePoint(50.0, 50.0);
 
[bezierPath moveToPoint: NSMakePoint(0.0, 0.0)];
[bezierPath lineToPoint: NSMakePoint(100.0, 100.0)];
 
// Modifies the point added by lineToPoint: method (100.0, 100.0)
// to the new point (50.0, 50.0)
[bezierPath setAssociatedPoints: &newPoint atIndex: 1];
```

> **Note**:  If you specify too few points for a path element of type [`NSCurveToBezierPathElement`](nscurvetobezierpathelement.md), the behavior of this method is undefined.

## Parameters

- `points`: A C-style array containing up to three   data types. This parameter must contain the correct number of points for the path element at the specified index. Move, close path, and line segment commands require one point. Curve operations require three points.
- `index`: The index of the path element you want to modify.

## See Also

- [var cgPath: CGPath](nsbezierpath/cgpath.md)
- [var elementCount: Int](nsbezierpath/elementcount.md)
  The total number of path elements in the path.
- [func element(at: Int) -> NSBezierPath.ElementType](nsbezierpath/element(at:).md)
  Returns the type of path element at the specified index.
- [func element(at: Int, associatedPoints: NSPointArray?) -> NSBezierPath.ElementType](nsbezierpath/element(at:associatedpoints:).md)
  Gets the element type and (and optionally) the associated points for the path element at the specified index.
- [func removeAllPoints()](nsbezierpath/removeallpoints.md)
  Removes all path elements from the path, effectively clearing the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/setassociatedpoints(_:at:))*