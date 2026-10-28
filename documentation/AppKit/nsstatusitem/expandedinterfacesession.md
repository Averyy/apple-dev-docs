# expandedInterfaceSession

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A session object that tracks the lifecycle of the status item’s active expanded interface.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var expandedInterfaceSession: NSStatusItemExpandedInterfaceSession? { get }
```

```objc
@property (strong, readonly, nullable) NSStatusItemExpandedInterfaceSession * expandedInterfaceSession;
```

## Discussion

The status item sets this property to a valid session object before calling [`statusItem(_:didBegin:)`](../nsstatusitemexpandedinterfacedelegate/statusitem%28_,didbegin%29.md) on the [`expandedInterfaceDelegate`](./expandedinterfacedelegate.md), and sets the property to `nil` before calling [`statusItemDidEndExpandedInterfaceSession(_:animated:)`](../nsstatusitemexpandedinterfacedelegate/statusitemdidendexpandedinterfacesession%28_,animated%29.md).

## See Also

### Managing the expanded interface
- [var expandedInterfaceDelegate: (any NSStatusItemExpandedInterfaceDelegate)?](./expandedinterfacedelegate.md)
  The delegate that manages the lifecycle of the status item’s expanded interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/expandedinterfacesession)*