# scrubber

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scrubber control that this layout is assigned to.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
weak var scrubber: NSScrubber? { get }
```

```objc
@property (weak, readonly, nullable) NSScrubber * scrubber;
```

## Discussion

If this layout is not currently assigned to a scrubber control, the value of this property is `nil`.

## See Also

### Configuring a scrubber layout
- [class var layoutAttributesClass: AnyClass](./layoutattributesclass.md)
  A property containing a class that describes layout attributes.
- [var visibleRect: NSRect](./visiblerect.md)
  The currently visible rectangle, in the coordinate space of the scrubber content.
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Signals that the layout has been invalidated, and that the scrubber control should perform a new layout pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayout/scrubber)*