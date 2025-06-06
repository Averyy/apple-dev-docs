# invalidateLayout()

**Framework**: AppKit  
**Kind**: method

Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func invalidateLayout()
```

## See Also

- [class var layoutAttributesClass: AnyClass](nsscrubberlayout/layoutattributesclass.md)
  A property containing a class that describes layout attributes.
- [var scrubber: NSScrubber?](nsscrubberlayout/scrubber.md)
  The scrubber control that this layout is assigned to.
- [var visibleRect: NSRect](nsscrubberlayout/visiblerect.md)
  The currently visible rectangle, in the coordinate space of the scrubber content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/invalidatelayout())*