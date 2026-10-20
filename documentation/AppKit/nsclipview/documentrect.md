# documentRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle defining the document view’s frame, adjusted to the size of the clip view if the document view is smaller.

**Availability**:
- macOS

## Declaration

```swift
var documentRect: NSRect { get }
```

```objc
@property (readonly) NSRect documentRect;
```

#### Discussion

The document rectangle is used in conjunction with an [`NSClipView`](../nsclipview.md) object’s bounds rectangle to determine values for the indicators of relative position and size between the [`NSClipView`](../nsclipview.md) and its document view. For example, [`NSScrollView`](../nsscrollview.md) uses these rectangles to set the size and position of the knobs in its scrollers. When the document view is much larger than the [`NSClipView`](../nsclipview.md), the knob is small; when the document view is near the same size, the knob is large; and when the document view is the same size or smaller, there is no knob.

## See Also

### Related Documentation
- [func reflectScrolledClipView(NSClipView)](../nsscrollview/reflectscrolledclipview%28_%29.md)
  Adjusts the receiver’s scrollers to reflect the size and positioning of its content view.
### Accessing the Visible Portion
- [var documentVisibleRect: NSRect](./documentvisiblerect.md)
  The exposed rectangle of the clip view’s document view, in the document view’s own coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/documentrect)*