# detachableWindow(for:)

**Framework**: AppKit  
**Kind**: method

Detaches the popover creating a window containing the content.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func detachableWindow(for popover: NSPopover) -> NSWindow?
```

#### Return Value

Returns a window instance to which the popover should be detached.

#### Discussion

You should not remove the popover’s content view as part of your implementation of this method.

The popover and the detachable window may be shown at the same time and therefore cannot share a content view or content view controller.

If the popover and the detachable window should have the same content, you should define the content in a separate nib file and use a view controller to instantiate separate copies of the content for the popover and the detachable window.

The popover will animate to appear as though it morphs into the detachable window (unless the popover’s  [`animates`](nspopover/animates.md) property is set to [`false`](https://developer.apple.com/documentation/swift/false)). The exact animation used is not guaranteed.

If there is no delegate, the delegate does not implement this method, or the delegate returns nil, the popup will not be displayed detached.

## Parameters

- `popover`: The popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopoverdelegate/detachablewindow(for:))*