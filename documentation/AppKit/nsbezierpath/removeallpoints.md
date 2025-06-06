# removeAllPoints()

**Framework**: AppKit  
**Kind**: method

Removes all path elements from the path, effectively clearing the path.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeAllPoints()
```

## See Also

- [var cgPath: CGPath](nsbezierpath/cgpath.md)
- [var elementCount: Int](nsbezierpath/elementcount.md)
  The total number of path elements in the path.
- [func element(at: Int) -> NSBezierPath.ElementType](nsbezierpath/element(at:).md)
  Returns the type of path element at the specified index.
- [func element(at: Int, associatedPoints: NSPointArray?) -> NSBezierPath.ElementType](nsbezierpath/element(at:associatedpoints:).md)
  Gets the element type and (and optionally) the associated points for the path element at the specified index.
- [func setAssociatedPoints(NSPointArray?, at: Int)](nsbezierpath/setassociatedpoints(_:at:).md)
  Changes the points associated with the specified path element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/removeallpoints())*