# init(frame:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a newly allocated `NSView` object with a specified frame rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(frame frameRect: NSRect)
```

#### Return Value

An initialized view or `nil` if AppKit couldn’t create the object.

#### Discussion

Insert the view into your window’s view hieararchy before you can do anything with it. This method is the designated initializer for the [`NSView`](nsview.md) class.

## Parameters

- `frameRect`: The frame rectangle for the created view object.

## See Also

- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](nsview/addsubview(_:positioned:relativeto:).md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [var frame: NSRect](nsview/frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func addSubview(NSView)](nsview/addsubview(_:).md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [View Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002978)
- [init?(coder: NSCoder)](nsview/init(coder:).md)
  Initializes a view using from data in the specified coder object.
- [func prepareForReuse()](nsview/prepareforreuse.md)
  Restores the view to an initial state so that it can be reused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/init(frame:))*