# behavior

**Framework**: AppKit  
**Kind**: property

Specifies the behavior of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var behavior: NSPopover.Behavior { get set }
```

#### Discussion

The default value is [`NSPopover.Behavior.applicationDefined`](nspopover/behavior-swift.enum/applicationdefined.md). See [`NSPopover.Behavior`](nspopover/behavior-swift.enum.md) for possible value.

## See Also

- [func show(relativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge)](nspopover/show(relativeto:of:preferrededge:).md)
  Shows the popover anchored to the specified view.
- [var positioningRect: NSRect](nspopover/positioningrect.md)
  The rectangle within the positioning view relative to which the popover should be positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/behavior-swift.property)*