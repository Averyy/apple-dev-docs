# positioningRect

**Framework**: AppKit  
**Kind**: property

The rectangle within the positioning view relative to which the popover should be positioned.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var positioningRect: NSRect { get set }
```

#### Discussion

Popovers are positioned relative to a positioning view and are automatically moved when the location or size of the positioning view changes.

Sometimes it is desirable to position popovers relative to a rectangle within the positioning view. In this case, you must update the `positioningRect` property whenever this rectangle changes.

This property is exposed as a read-only binding.

## See Also

- [var behavior: NSPopover.Behavior](nspopover/behavior-swift.property.md)
  Specifies the behavior of the popover.
- [func show(relativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge)](nspopover/show(relativeto:of:preferrededge:).md)
  Shows the popover anchored to the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/positioningrect)*