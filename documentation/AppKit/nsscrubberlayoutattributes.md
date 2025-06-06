# NSScrubberLayoutAttributes

**Framework**: AppKit  
**Kind**: class

The layout of a scrubber item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberLayoutAttributes
```

#### Overview

A layout attributes object is the model for the layout of a single item in a scrubber control.

If you require model attributes in addition to those provided by this class, create a subclass and add appropriate attributes. Subclasses must implement [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)), [`hash`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/hash) and the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocol.

## Topics

### Creating layout attributes
- [convenience init(forItemAt: Int)](nsscrubberlayoutattributes/init(foritemat:).md)
  Creates a new layout attributes object for the specified scrubber item index.
### Controlling the layout
- [var alpha: CGFloat](nsscrubberlayoutattributes/alpha.md)
  The item’s alpha value.
- [var frame: NSRect](nsscrubberlayoutattributes/frame.md)
  The frame of the scrubber item.
- [var itemIndex: Int](nsscrubberlayoutattributes/itemindex.md)
  The index of the scrubber item that is represented by the item’s layout attributes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSScrubberFlowLayout](nsscrubberflowlayout.md)
  A concrete layout object that arranges items end-to-end in a linear strip.
- [protocol NSScrubberFlowLayoutDelegate](nsscrubberflowlayoutdelegate.md)
  A protocol that a scrubber delegate can adopt to provide the size of an item.
- [class NSScrubberProportionalLayout](nsscrubberproportionallayout.md)
  A concrete layout object that sizes each item to some fraction of the scrubber’s visible size.
- [class NSScrubberLayout](nsscrubberlayout.md)
  An abstract class that describes the layout of items within a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayoutattributes)*