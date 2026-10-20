# init(contentSize:preferredEdge:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new drawer with the given size on the specified edge of the parent window.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
init(contentSize: NSSize, preferredEdge edge: NSRectEdge)
```

```objc
- (instancetype) initWithContentSize:(NSSize) contentSize preferredEdge:(NSRectEdge) edge;
```

#### Discussion

You must specify the parent window and content view of the drawer using the methods in this class. When you create a drawer in Interface Builder, this constructor is invoked. The NSDrawer Inspector in Interface Builder allows you to set the edge, and you can specify the size by changing the content view in Interface Builder.

See [Positioning and Sizing a Drawer](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Drawers/Concepts/DrawerSizing.html#//apple_ref/doc/uid/20001524) for additional detail on content size and drawer positioning.

## Parameters

- `contentSize`: The size of the new drawer.
- `edge`: The edge to which to attach the new drawer.

## See Also

### Related Documentation
- [Drawer Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Drawers/Drawers.html#//apple_ref/doc/uid/10000001i)
### Creating Drawers
- [var delegate: (any NSDrawerDelegate)?](./delegate.md)
  The receiver’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/init(contentsize:preferrededge:))*