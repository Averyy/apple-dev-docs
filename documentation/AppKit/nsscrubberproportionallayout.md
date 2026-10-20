# NSScrubberProportionalLayout

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A concrete layout object that sizes each item to some fraction of the scrubber’s visible size.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberProportionalLayout
```

```objc
@interface NSScrubberProportionalLayout : NSScrubberLayout
```

## Topics

### Initializing a proprotional layout
- [init(numberOfVisibleItems: Int)](./nsscrubberproportionallayout/init%28numberofvisibleitems%29.md)
  Initializes and returns a newly allocated proportional layout, configured to display the given number of items.
- [init(coder: NSCoder)](./nsscrubberproportionallayout/init%28coder%29.md)
  Initializes and returns a newly allocated proprotional layout object from a storyboard or nib file.
### Configuring the layout
- [var numberOfVisibleItems: Int](./nsscrubberproportionallayout/numberofvisibleitems.md)
  The number of items visible in the scrubber at once.

## Relationships

### Inherits From
- [NSScrubberLayout](./nsscrubberlayout.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Scrubber layouts
- [class NSScrubberFlowLayout](./nsscrubberflowlayout.md)
  A concrete layout object that arranges items end-to-end in a linear strip.
- [protocol NSScrubberFlowLayoutDelegate](./nsscrubberflowlayoutdelegate.md)
  A protocol that a scrubber delegate can adopt to provide the size of an item.
- [class NSScrubberLayoutAttributes](./nsscrubberlayoutattributes.md)
  The layout of a scrubber item.
- [class NSScrubberLayout](./nsscrubberlayout.md)
  An abstract class that describes the layout of items within a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberproportionallayout)*