# layoutAttributesClass

**Framework**: AppKit  
**Kind**: property

A property containing a class that describes layout attributes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class var layoutAttributesClass: AnyClass { get }
```

#### Return Value

The default return value is [`NSScrubberLayoutAttributes`](nsscrubberlayoutattributes.md).

#### Discussion

Create a custom subclass of [`NSScrubberLayout`](nsscrubberlayout.md) and override this method if you wish to use a custom layout attributes subclass.

## See Also

- [class NSScrubberLayoutAttributes](nsscrubberlayoutattributes.md)
  The layout of a scrubber item.
- [var scrubber: NSScrubber?](nsscrubberlayout/scrubber.md)
  The scrubber control that this layout is assigned to.
- [var visibleRect: NSRect](nsscrubberlayout/visiblerect.md)
  The currently visible rectangle, in the coordinate space of the scrubber content.
- [func invalidateLayout()](nsscrubberlayout/invalidatelayout.md)
  Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/layoutattributesclass)*