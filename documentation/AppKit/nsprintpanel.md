# NSPrintPanel

**Framework**: AppKit  
**Kind**: class

The Print panel that queries the user for information about a print job.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSPrintPanel
```

#### Overview

A Print panel may let the user select the range of pages to print and the number of copies before executing the Print command. Print panels can display a simplified interface when printing certain types of data. For example, the panel can display a list of print-setting presets, which lets the user enable print settings in groups as opposed to individually. Assigning an appropriate string to the [`jobStyleHint`](nsprintpanel/jobstylehint-swift.property.md) property activates the simplified interface and identifies which presets to display.

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/system-capabilities/printing/).

## Topics

### Customizing the Panel
- [var jobStyleHint: NSPrintPanel.JobStyleHint?](nsprintpanel/jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
- [NSPrintPanel.JobStyleHint](nsprintpanel/jobstylehint-swift.struct.md)
  Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.
- [var options: NSPrintPanel.Options](nsprintpanel/options-swift.property.md)
  The current configuration options for the Print panel.
- [NSPrintPanel.Options](nsprintpanel/options-swift.struct.md)
  Constants that specify options for configuring the contents of the main Print panel.
- [func defaultButtonTitle() -> String?](nsprintpanel/defaultbuttontitle.md)
  Returns the title of the Print panel’s default button.
- [func setDefaultButtonTitle(String?)](nsprintpanel/setdefaultbuttontitle(_:).md)
  Sets the title of the Print panel’s default button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsprintpanel/helpanchor.md)
  The HTML help anchor associated with the Print panel.
### Managing Accessory Views
- [func addAccessoryController(any NSViewController & NSPrintPanelAccessorizing)](nsprintpanel/addaccessorycontroller(_:).md)
  Adds a custom controller to the Print panel to manage an accessory view.
- [func removeAccessoryController(any NSViewController & NSPrintPanelAccessorizing)](nsprintpanel/removeaccessorycontroller(_:).md)
  Removes the specified controller and accessory view from the Print panel.
- [protocol NSPrintPanelAccessorizing](nsprintpanelaccessorizing.md)
  A set of methods that a Print panel object can use to get information from a printing accessory controller.
- [var accessoryControllers: [NSViewController]](nsprintpanel/accessorycontrollers.md)
  The array of controller objects that manage the Print panel’s accessory views.
### Running the Panel
- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPrintPanel.Result) -> Void)?)](nsprintpanel/beginsheet(using:on:completionhandler:).md)
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintpanel/beginsheet(with:modalfor:delegate:didend:contextinfo:).md)
  Displays a Print panel sheet and runs it modally for the specified window.
- [func runModal() -> Int](nsprintpanel/runmodal.md)
  Displays the Print panel and begins the modal loop.
- [func runModal(with: NSPrintInfo) -> Int](nsprintpanel/runmodal(with:).md)
  Displays the Print panel and runs the modal loop using the specified printing information.
### Accessing the Printing Information
- [var printInfo: NSPrintInfo](nsprintpanel/printinfo.md)
  The information associated with the running Print panel.
- [class NSPrintInfo](nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [NSPrintPanel.Result](nsprintpanel/result.md)

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

- [class NSPageLayout](nspagelayout.md)
  A panel that queries the user for information such as paper type and orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel)*