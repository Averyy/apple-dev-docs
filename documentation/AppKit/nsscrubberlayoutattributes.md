# NSScrubberLayoutAttributes

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The layout of a scrubber item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
class NSScrubberLayoutAttributes
```

```objc
@interface NSScrubberLayoutAttributes : NSObject
```

## Overview

A layout attributes object is the model for the layout of a single item in a scrubber control.

If you require model attributes in addition to those provided by this class, create a subclass and add appropriate attributes. Subclasses must implement [`isEqual(_:)`](../ObjectiveC/nsobjectprotocol/isequal%28_%29.md), [`hash`](../ObjectiveC/nsobjectprotocol/hash.md) and the [`NSCopying`](../Foundation/nscopying.md) protocol.

## Topics

### Creating layout attributes
- [convenience init(forItemAt: Int)](./nsscrubberlayoutattributes/init%28foritemat%29.md)
  Creates a new layout attributes object for the specified scrubber item index.
### Controlling the layout
- [var alpha: CGFloat](./nsscrubberlayoutattributes/alpha.md)
  The item’s alpha value.
- [var frame: NSRect](./nsscrubberlayoutattributes/frame.md)
  The frame of the scrubber item.
- [var itemIndex: Int](./nsscrubberlayoutattributes/itemindex.md)
  The index of the scrubber item that is represented by the item’s layout attributes.
### Initializers
- [convenience init(forItemAtIndex: Int)](./nsscrubberlayoutattributes/init%28foritematindex%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Scrubber layouts
- [class NSScrubberFlowLayout](./nsscrubberflowlayout.md)
  A concrete layout object that arranges items end-to-end in a linear strip.
- [protocol NSScrubberFlowLayoutDelegate](./nsscrubberflowlayoutdelegate.md)
  A protocol that a scrubber delegate can adopt to provide the size of an item.
- [class NSScrubberProportionalLayout](./nsscrubberproportionallayout.md)
  A concrete layout object that sizes each item to some fraction of the scrubber’s visible size.
- [class NSScrubberLayout](./nsscrubberlayout.md)
  An abstract class that describes the layout of items within a scrubber control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberlayoutattributes)*