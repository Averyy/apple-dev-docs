# NSSharingServiceDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that you use to customize the position and animation of a share sheet, and to be notified whether the item is successfully shared.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSSharingServiceDelegate : NSObjectProtocol
```

#### Overview

See [`NSSharingService`](nssharingservice.md) for more information.

## Topics

### Sharing Items
- [func sharingService(NSSharingService, willShareItems: [Any])](nssharingservicedelegate/sharingservice(_:willshareitems:).md)
  Invoked when the sharing service will share the specified items.
- [func sharingService(NSSharingService, didShareItems: [Any])](nssharingservicedelegate/sharingservice(_:didshareitems:).md)
  Invoked when the sharing service has finished sharing the items.
- [func sharingService(NSSharingService, didFailToShareItems: [Any], error: any Error)](nssharingservicedelegate/sharingservice(_:didfailtoshareitems:error:).md)
  Invoked when the sharing service encountered an error when sharing items.
### Customizing Transition Animation
- [func sharingService(NSSharingService, sourceFrameOnScreenForShareItem: Any) -> NSRect](nssharingservicedelegate/sharingservice(_:sourceframeonscreenforshareitem:).md)
  Invoked when the sharing service is performed and the sharing window is displayed, to present a transition between the original items and the sharing window.
- [func sharingService(NSSharingService, transitionImageForShareItem: Any, contentRect: UnsafeMutablePointer<NSRect>) -> NSImage?](nssharingservicedelegate/sharingservice(_:transitionimageforshareitem:contentrect:).md)
  Invoked to allow returning a custom transition image when sharing an item.
- [func sharingService(NSSharingService, sourceWindowForShareItems: [Any], sharingContentScope: UnsafeMutablePointer<NSSharingService.SharingContentScope>) -> NSWindow?](nssharingservicedelegate/sharingservice(_:sourcewindowforshareitems:sharingcontentscope:).md)
  Returns the window that contained the share items.
- [NSSharingService.SharingContentScope](nssharingservice/sharingcontentscope.md)
  The sharing scope constants specify the nature of the things you are sharing.
### Getting an Anchor View
- [func anchoringView(for: NSSharingService, showRelativeTo: UnsafeMutablePointer<NSRect>, preferredEdge: UnsafeMutablePointer<NSRectEdge>) -> NSView?](nssharingservicedelegate/anchoringview(for:showrelativeto:preferrededge:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md)

## See Also

- [var delegate: (any NSSharingServiceDelegate)?](nssharingservice/delegate.md)
  Specifies the delegate of the sharing service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate)*