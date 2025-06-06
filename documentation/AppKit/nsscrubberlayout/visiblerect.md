# visibleRect

**Framework**: AppKit  
**Kind**: property

The currently visible rectangle, in the coordinate space of the scrubber content.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var visibleRect: NSRect { get }
```

#### Discussion

The value of this property is [`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect) if the layout is not currently assigned to a scrubber control.

## See Also

- [class var layoutAttributesClass: AnyClass](nsscrubberlayout/layoutattributesclass.md)
  A property containing a class that describes layout attributes.
- [var scrubber: NSScrubber?](nsscrubberlayout/scrubber.md)
  The scrubber control that this layout is assigned to.
- [func invalidateLayout()](nsscrubberlayout/invalidatelayout.md)
  Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/visiblerect)*