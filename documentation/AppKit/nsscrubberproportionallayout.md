# NSScrubberProportionalLayout

**Framework**: AppKit  
**Kind**: class

A concrete layout object that sizes each item to some fraction of the scrubber’s visible size.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberProportionalLayout
```

## Topics

### Initializing a proprotional layout
- [init(numberOfVisibleItems: Int)](nsscrubberproportionallayout/init(numberofvisibleitems:).md)
  Initializes and returns a newly allocated proportional layout, configured to display the given number of items.
- [init(coder: NSCoder)](nsscrubberproportionallayout/init(coder:).md)
  Initializes and returns a newly allocated proprotional layout object from a storyboard or nib file.
### Configuring the layout
- [var numberOfVisibleItems: Int](nsscrubberproportionallayout/numberofvisibleitems.md)
  The number of items visible in the scrubber at once.

## Relationships

### Inherits From
- [NSScrubberLayout](nsscrubberlayout.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NSScrubberFlowLayout](nsscrubberflowlayout.md)
  A concrete layout object that arranges items end-to-end in a linear strip.
- [protocol NSScrubberFlowLayoutDelegate](nsscrubberflowlayoutdelegate.md)
  A protocol that a scrubber delegate can adopt to provide the size of an item.
- [class NSScrubberLayoutAttributes](nsscrubberlayoutattributes.md)
  The layout of a scrubber item.
- [class NSScrubberLayout](nsscrubberlayout.md)
  An abstract class that describes the layout of items within a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberproportionallayout)*