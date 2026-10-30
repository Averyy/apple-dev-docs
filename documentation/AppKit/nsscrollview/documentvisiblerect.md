# documentVisibleRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The portion of the document view, in its own coordinate system, visible through the scroll view’s content view.

**Availability**:
- macOS

## Declaration

```swift
var documentVisibleRect: NSRect { get }
```

```objc
@property (readonly) NSRect documentVisibleRect;
```

## See Also

### Related Documentation
- [var documentVisibleRect: NSRect](../nsclipview/documentvisiblerect.md)
  The exposed rectangle of the clip view’s document view, in the document view’s own coordinate system.
- [var visibleRect: NSRect](../nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
### Determining component sizes
- [var contentSize: NSSize](./contentsize.md)
  The size of the scroll view’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/documentvisiblerect)*