# invalidateLayout()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func invalidateLayout()
```

```objc
- (void) invalidateLayout;
```

## See Also

### Configuring a scrubber layout
- [class var layoutAttributesClass: AnyClass](./layoutattributesclass.md)
  A property containing a class that describes layout attributes.
- [var scrubber: NSScrubber?](./scrubber.md)
  The scrubber control that this layout is assigned to.
- [var visibleRect: NSRect](./visiblerect.md)
  The currently visible rectangle, in the coordinate space of the scrubber content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/invalidatelayout())*