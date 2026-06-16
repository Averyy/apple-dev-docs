# expandedInterfaceSession

**Framework**: AppKit  
**Kind**: property

A session object that tracks the lifecycle of the status item’s active expanded interface.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var expandedInterfaceSession: NSStatusItemExpandedInterfaceSession? { get }
```

#### Discussion

The status item sets this property to a valid session object before calling [`statusItem(_:didBegin:)`](nsstatusitemexpandedinterfacedelegate/statusitem(_:didbegin:).md) on the [`expandedInterfaceDelegate`](nsstatusitem/expandedinterfacedelegate.md), and sets the property to `nil` before calling [`statusItemDidEndExpandedInterfaceSession(_:animated:)`](nsstatusitemexpandedinterfacedelegate/statusitemdidendexpandedinterfacesession(_:animated:).md).

## See Also

- [var expandedInterfaceDelegate: (any NSStatusItemExpandedInterfaceDelegate)?](nsstatusitem/expandedinterfacedelegate.md)
  The delegate that manages the lifecycle of the status item’s expanded interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/expandedinterfacesession)*