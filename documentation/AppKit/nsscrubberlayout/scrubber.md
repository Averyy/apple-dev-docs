# scrubber

**Framework**: AppKit  
**Kind**: property

The scrubber control that this layout is assigned to.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
weak var scrubber: NSScrubber? { get }
```

#### Discussion

If this layout is not currently assigned to a scrubber control, the value of this property is `nil`.

## See Also

- [class var layoutAttributesClass: AnyClass](nsscrubberlayout/layoutattributesclass.md)
  A property containing a class that describes layout attributes.
- [var visibleRect: NSRect](nsscrubberlayout/visiblerect.md)
  The currently visible rectangle, in the coordinate space of the scrubber content.
- [func invalidateLayout()](nsscrubberlayout/invalidatelayout.md)
  Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/scrubber)*