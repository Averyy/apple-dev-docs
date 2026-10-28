# layoutAttributesClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A property containing a class that describes layout attributes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class var layoutAttributesClass: AnyClass { get }
```

```objc
@property (class, readonly) Class layoutAttributesClass;
```

## Return Value

The default return value is [`NSScrubberLayoutAttributes`](../nsscrubberlayoutattributes.md).

## Discussion

Create a custom subclass of [`NSScrubberLayout`](../nsscrubberlayout.md) and override this method if you wish to use a custom layout attributes subclass.

## See Also

### Related Documentation
- [class NSScrubberLayoutAttributes](../nsscrubberlayoutattributes.md)
  The layout of a scrubber item.
### Configuring a scrubber layout
- [var scrubber: NSScrubber?](./scrubber.md)
  The scrubber control that this layout is assigned to.
- [var visibleRect: NSRect](./visiblerect.md)
  The currently visible rectangle, in the coordinate space of the scrubber content.
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/layoutattributesclass)*