# init(frame:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated `NSView` object with a specified frame rectangle.

**Availability**:
- macOS

## Declaration

```swift
init(frame frameRect: NSRect)
```

```objc
- (instancetype) initWithFrame:(NSRect) frameRect;
```

## Return Value

An initialized view or `nil` if AppKit couldn’t create the object.

## Discussion

Insert the view into your window’s view hieararchy before you can do anything with it. This method is the designated initializer for the [`NSView`](../nsview.md) class.

## Parameters

- `frameRect`: The frame rectangle for the created view object.

## See Also

### Related Documentation
- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](./addsubview%28_,positioned,relativeto%29.md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [var frame: NSRect](./frame.md)
  The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [func addSubview(NSView)](./addsubview%28_%29.md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [View Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002978)
### Creating a view object
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes a view using from data in the specified coder object.
- [func prepareForReuse()](./prepareforreuse%28%29.md)
  Restores the view to an initial state so that it can be reused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/init(frame:))*