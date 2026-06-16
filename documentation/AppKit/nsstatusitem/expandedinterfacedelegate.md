# expandedInterfaceDelegate

**Framework**: AppKit  
**Kind**: property

The delegate that manages the lifecycle of the status item’s expanded interface.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
weak var expandedInterfaceDelegate: (any NSStatusItemExpandedInterfaceDelegate)? { get set }
```

#### Discussion

Status items that assign an [`NSMenu`](nsmenu.md) to their button don’t receive expanded interface callbacks — the system handles the expanded menu interface automatically. The delegate shows the expanded interface, such as an [`NSWindow`](nswindow.md) positioned beneath the status item, in response to [`statusItem(_:didBegin:)`](nsstatusitemexpandedinterfacedelegate/statusitem(_:didbegin:).md), and dismisses the interface in response to [`statusItemDidEndExpandedInterfaceSession(_:animated:)`](nsstatusitemexpandedinterfacedelegate/statusitemdidendexpandedinterfacesession(_:animated:).md).

## See Also

- [var expandedInterfaceSession: NSStatusItemExpandedInterfaceSession?](nsstatusitem/expandedinterfacesession.md)
  A session object that tracks the lifecycle of the status item’s active expanded interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/expandedinterfacedelegate)*