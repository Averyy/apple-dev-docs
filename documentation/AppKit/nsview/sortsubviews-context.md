# sortSubviews(_:context:)

**Framework**: AppKit  
**Kind**: method

Orders the view’s immediate subviews using the specified comparator function.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sortSubviews(_ compare: (NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)
```

## Parameters

- `compare`: A pointer to the comparator function. This function must take as arguments two subviews to be ordered and contextual data (supplied in   which may be arbitrary data used to help in the comparison. The comparator function should return   if the first subview should be ordered lower,   if the second subview should be ordered lower, and   if their ordering isn’t important.
- `context`: Arbitrary data that might help the comparator function   in its decisions.

## See Also

- [func sortedArray(_ comparator: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](../Foundation/NSArray/sortedArray(_:context:).md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func addSubview(NSView)](nsview/addsubview(_:).md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](nsview/addsubview(_:positioned:relativeto:).md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [func removeFromSuperview()](nsview/removefromsuperview.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func removeFromSuperviewWithoutNeedingDisplay()](nsview/removefromsuperviewwithoutneedingdisplay.md)
  Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.
- [func replaceSubview(NSView, with: NSView)](nsview/replacesubview(_:with:).md)
  Replaces one of the view’s subviews with another view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/sortsubviews(_:context:))*