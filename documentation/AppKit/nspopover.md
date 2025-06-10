# NSPopover

**Framework**: AppKit  
**Kind**: class

A means to display additional content related to existing content on the screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class NSPopover
```

#### Overview

The popover is positioned relative to the existing content and an anchor is used to express the relation between these two units of content. A popover has an appearance that specifies its visual characteristics, as well as a behavior that determines which user interactions will cause the popover to close. A transient popover is closed in response to most user interactions, whereas a semi-transient popover is closed when the user interacts with the window containing the popover’s positioning view. Popovers with application-defined behavior are not usually closed on the developer’s behalf.

The system automatically positions each popover relative to its positioning view and moves the popover whenever its positioning view moves. A positioning rectangle within the positioning view can be specified for additional granularity.

Popovers can be detached to become a separate window when they are dragged by implementing the appropriate delegate method.

## Topics

### Accessing a Popover’s Content View Controller
- [var contentViewController: NSViewController?](nspopover/contentviewcontroller.md)
  The view controller that manages the content of the popover.
### Managing a Popover’s Position and Size
- [var behavior: NSPopover.Behavior](nspopover/behavior-swift.property.md)
  Specifies the behavior of the popover.
- [func show(relativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge)](nspopover/show(relativeto:of:preferrededge:).md)
  Shows the popover anchored to the specified view.
- [var positioningRect: NSRect](nspopover/positioningrect.md)
  The rectangle within the positioning view relative to which the popover should be positioned.
### Managing a Popover’s Appearance
- [var appearance: NSAppearance?](nspopover/appearance-swift.property.md)
  The appearance of the popover.
- [var effectiveAppearance: NSAppearance](nspopover/effectiveappearance.md)
  The appearance that will be used when the popover is displayed onscreen.
- [var animates: Bool](nspopover/animates.md)
  Specifies if the popover is to be animated.
- [var contentSize: NSSize](nspopover/contentsize.md)
  The content size of the popover.
- [var isShown: Bool](nspopover/isshown.md)
  The display state of the popover.
- [var isDetached: Bool](nspopover/isdetached.md)
  A Boolean value that indicates whether the window created by a popover’s detachment is automatically created.
### Closing a Popover
- [func performClose(Any?)](nspopover/performclose(_:).md)
  Attempts to close the popover.
- [func close()](nspopover/close.md)
  Forces the popover to close without consulting its delegate.
### Getting and Setting the Delegate
- [var delegate: (any NSPopoverDelegate)?](nspopover/delegate.md)
  The delegate of the popover.
### Constants
- [NSPopover.Behavior](nspopover/behavior-swift.enum.md)
  The appearance and disappearance behavior of a popover.
- [class let closeReasonUserInfoKey: String](nspopover/closereasonuserinfokey.md)
  The `userInfo` key containing the reason for the [`willCloseNotification`](nspopover/willclosenotification.md).
- [NSPopover.CloseReason](nspopover/closereason.md)
  Values that specify the reason for the [`willCloseNotification`](nspopover/willclosenotification.md) notification.
- [NSPopover.Appearance](nspopover/appearance-swift.enum.md)
  The set of predefined appearances for a popover.
### Notifications
- [class let willShowNotification: NSNotification.Name](nspopover/willshownotification.md)
  Sent before the popover is shown.
- [class let didShowNotification: NSNotification.Name](nspopover/didshownotification.md)
  Sent after the popover has finished animating onscreen.
- [class let willCloseNotification: NSNotification.Name](nspopover/willclosenotification.md)
  Sent before the popover is closed.
- [class let didCloseNotification: NSNotification.Name](nspopover/didclosenotification.md)
  Sent after the popover has finished animating offscreen.
### Initializers
- [init()](nspopover/init.md)
- [init?(coder: NSCoder)](nspopover/init(coder:).md)
### Instance Properties
- [var hasFullSizeContent: Bool](nspopover/hasfullsizecontent.md)
  A Boolean value that indicates whether the content view of the popover extends into the arrow region.
### Instance Methods
- [func show(relativeTo: NSToolbarItem)](nspopover/show(relativeto:).md)
  Shows the popover anchored to the specified toolbar item.

## Relationships

### Inherits From
- [NSResponder](nsresponder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSPopoverDelegate](nspopoverdelegate.md)
  A set of optional methods that a popover delegate can implement to provide additional or custom functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover)*