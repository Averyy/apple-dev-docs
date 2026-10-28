# visibleRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The currently visible rectangle, in the coordinate space of the scrubber content.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var visibleRect: NSRect { get }
```

```objc
@property (readonly) NSRect visibleRect;
```

## Discussion

The value of this property is [`NSZeroRect`](../../Foundation/nszerorect.md) if the layout is not currently assigned to a scrubber control.

## See Also

### Configuring a scrubber layout
- [class var layoutAttributesClass: AnyClass](./layoutattributesclass.md)
  A property containing a class that describes layout attributes.
- [var scrubber: NSScrubber?](./scrubber.md)
  The scrubber control that this layout is assigned to.
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/visiblerect)*