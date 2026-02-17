# anchoringView(for:showRelativeTo:preferredEdge:)

**Framework**: AppKit  
**Kind**: method

The method invoked when the service is performed and wants to display its contents in a popover.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func anchoringView(for sharingService: NSSharingService, showRelativeTo positioningRect: UnsafeMutablePointer<NSRect>, preferredEdge: UnsafeMutablePointer<NSRectEdge>) -> NSView?
```

#### Discussion

The delegate should return the view that will act as the anchor of the popover, along with the target rectangle within the bounds of that view and preferred edge of that rectangle for the popover to appear. The delegate may also return `nil`, indicating that there is no anchoring view currently available, in which case the service may attempt to display the service via some other means.

The service named `NSSharingServiceNameCloudSharing` prefers to display itself using a popover anchored to an “Add People” or “Share” button. If no such button is available or visible, return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/anchoringview(for:showrelativeto:preferrededge:))*