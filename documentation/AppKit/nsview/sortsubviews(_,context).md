# sortSubviews(_:context:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Orders the view’s immediate subviews using the specified comparator function.

**Availability**:
- macOS

## Declaration

```swift
func sortSubviews(_ compare: (NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)
```

```objc
- (void) sortSubviewsUsingFunction:(enum NSComparisonResult (*)(__kindof NSView *, __kindof NSView *, void *)) compare context:(void *) context;
```

## Parameters

- `compare`: A pointer to the comparator function. This function must take as arguments two subviews to be ordered and contextual data (supplied in `context` which may be arbitrary data used to help in the comparison. The comparator function should return `NSOrderedAscending` if the first subview should be ordered lower, `NSOrderedDescending` if the second subview should be ordered lower, and `NSOrderedSame` if their ordering isn’t important.
- `context`: Arbitrary data that might help the comparator function `compare` in its decisions.

## See Also

### Related Documentation
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](../../Foundation/nsarray/sortedarray%28_,context%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
### Adding and Removing Subviews
- [func addSubview(NSView)](./addsubview%28_%29.md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](./addsubview%28_,positioned,relativeto%29.md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [func removeFromSuperview()](./removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func removeFromSuperviewWithoutNeedingDisplay()](./removefromsuperviewwithoutneedingdisplay%28%29.md)
  Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.
- [func replaceSubview(NSView, with: NSView)](./replacesubview%28_,with%29.md)
  Replaces one of the view’s subviews with another view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/sortsubviews(_:context:))*