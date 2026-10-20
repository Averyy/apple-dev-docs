# NSPageLayout

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A panel that queries the user for information such as paper type and orientation.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
class NSPageLayout
```

```objc
@interface NSPageLayout : NSObject
```

#### Overview

A page layout panel is typically displayed in response to the user selecting the Page Setup menu item. You obtain an instance with the [`pageLayout`](./nspagelayout/pagelayout.md) class method. The pane can then be run as a sheet using [`beginSheet(with:modalFor:delegate:didEnd:contextInfo:)`](./nspagelayout/beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md) or modally using [`runModal()`](./nspagelayout/runmodal%28%29.md) or [`runModal(with:)`](./nspagelayout/runmodal%28with%29.md).

For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/macos/system-capabilities/printing#page-setup-dialogs).

## Topics

### Running the page setup dialog
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPageLayout.Result) -> Void)?)](./nspagelayout/beginsheet%28using,on,completionhandler%29.md)
- [func runModal() -> Int](./nspagelayout/runmodal%28%29.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.
- [func runModal(with: NSPrintInfo) -> Int](./nspagelayout/runmodal%28with%29.md)
  Displays the page layout panel and begins the modal loop using the specified print info object.
### Customizing the page setup dialog
- [func addAccessoryController(NSViewController)](./nspagelayout/addaccessorycontroller%28_%29.md)
  Adds the specified controller of an accessory view to be presented in the page setup panel.
- [func removeAccessoryController(NSViewController)](./nspagelayout/removeaccessorycontroller%28_%29.md)
  Removes the specified controller of an accessory view.
- [var accessoryControllers: [NSViewController]](./nspagelayout/accessorycontrollers.md)
  An array of accessory view controllers belonging to the page layout panel.
### Accessing the printing information
- [var printInfo: NSPrintInfo?](./nspagelayout/printinfo.md)
  The printing information object used when the page layout panel is run.
- [class NSPrintInfo](./nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [NSPageLayout.Result](./nspagelayout/result.md)
### Deprecated
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./nspagelayout/beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md)
  Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Print Panels
- [class NSPrintPanel](./nsprintpanel.md)
  The Print panel that queries the user for information about a print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout)*