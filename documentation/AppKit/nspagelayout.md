# NSPageLayout

**Framework**: AppKit  
**Kind**: class

A panel that queries the user for information such as paper type and orientation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSPageLayout
```

#### Overview

A page layout panel is typically displayed in response to the user selecting the Page Setup menu item. You obtain an instance with the [`pageLayout`](nspagelayout/pagelayout.md) class method. The pane can then be run as a sheet using [`beginSheet(with:modalFor:delegate:didEnd:contextInfo:)`](nspagelayout/beginsheet(with:modalfor:delegate:didend:contextinfo:).md) or modally using [`runModal()`](nspagelayout/runmodal().md) or [`runModal(with:)`](nspagelayout/runmodal(with:).md).

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/system-capabilities/printing#page-setup-dialogs).

## Topics

### Running the page setup dialog
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPageLayout.Result) -> Void)?)](nspagelayout/beginsheet(using:on:completionhandler:).md)
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nspagelayout/beginsheet(with:modalfor:delegate:didend:contextinfo:).md)
  Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.
- [func runModal() -> Int](nspagelayout/runmodal.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.
- [func runModal(with: NSPrintInfo) -> Int](nspagelayout/runmodal(with:).md)
  Displays the page layout panel and begins the modal loop using the specified print info object.
### Customizing the page setup dialog
- [func addAccessoryController(NSViewController)](nspagelayout/addaccessorycontroller(_:).md)
  Adds the specified controller of an accessory view to be presented in the page setup panel.
- [func removeAccessoryController(NSViewController)](nspagelayout/removeaccessorycontroller(_:).md)
  Removes the specified controller of an accessory view.
- [var accessoryControllers: [NSViewController]](nspagelayout/accessorycontrollers.md)
  An array of accessory view controllers belonging to the page layout panel.
### Accessing the printing information
- [var printInfo: NSPrintInfo?](nspagelayout/printinfo.md)
  The printing information object used when the page layout panel is run.
- [class NSPrintInfo](nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [NSPageLayout.Result](nspagelayout/result.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSPrintPanel](nsprintpanel.md)
  The Print panel that queries the user for information about a print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout)*