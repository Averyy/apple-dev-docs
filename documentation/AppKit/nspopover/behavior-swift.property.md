# behavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Specifies the behavior of the popover.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var behavior: NSPopover.Behavior { get set }
```

```objc
@property NSPopoverBehavior behavior;
```

## Discussion

The default value is [`NSPopover.Behavior.applicationDefined`](./behavior-swift.enum/applicationdefined.md). See [`NSPopover.Behavior`](./behavior-swift.enum.md) for possible value.

## See Also

### Managing a Popover’s Position and Size
- [func show(relativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge)](./show%28relativeto,of,preferrededge%29.md)
  Shows the popover anchored to the specified view.
- [var positioningRect: NSRect](./positioningrect.md)
  The rectangle within the positioning view relative to which the popover should be positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/behavior-swift.property)*