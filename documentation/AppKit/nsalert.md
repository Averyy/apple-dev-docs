# NSAlert

**Framework**: AppKit  
**Kind**: class

A modal dialog or sheet attached to a document window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSAlert
```

#### Overview

The methods of the [`NSAlert`](nsalert.md) class let you specify an alert’s urgency, message text, button titles, and a custom icon. The class also supports a help button and other ways to offer contextual help specific to an alert.

To display an alert as a sheet, call the [`beginSheetModal(for:completionHandler:)`](nsalert/beginsheetmodal(for:completionhandler:).md) method; to display one as an app-modal dialog, use the [`runModal()`](nsalert/runmodal().md) method.

By design, each [`NSAlert`](nsalert.md) object represents a single alert with a specific combination of title, buttons, and other attributes that appear in response to a particular condition. Allocate (`alloc`) and initialize (`init`) an [`NSAlert`](nsalert.md) object for each alert dialog, customize its attributes as described below, and release it once you’re done. If you need to show a particular alert repeatedly, retain and reuse a single instance instead of creating a new one each time.

[`NSAlert`](nsalert.md) objects have the following attributes:

- **Type**: The importance or urgency of the alert, as shown to the person viewing it. Specified with the [`alertStyle`](nsalert/alertstyle.md) property.
- **Message text**: The main message of the alert. Specified with [`messageText`](nsalert/messagetext.md).
- **Informative text**: Additional information about the alert. Specified with [`informativeText`](nsalert/informativetext.md).
- **Icon**: An optional, custom icon to display in the alert, used instead of the default app icon. Specified with [`icon`](nsalert/icon.md).
- **Help**: A help button that a person can click to get more information about the alert. Use [`helpAnchor`](nsalert/helpanchor.md) and [`showsHelp`](nsalert/showshelp.md).
- **Response buttons**: By default an alert has one response button: the OK button. You can add more response buttons using the [`addButton(withTitle:)`](nsalert/addbutton(withtitle:).md) method.
- **Suppression checkbox**: A checkbox that lets a person opt out of seeing this particular alert again. Use [`showsSuppressionButton`](nsalert/showssuppressionbutton.md).
- **Accessory view**: A custom view, such as a text field for entering contact information, that adds extra content to an alert. Use [`accessoryView`](nsalert/accessoryview.md) and [`layout()`](nsalert/layout().md).

> **Note**: The `NSAlert` class doesn’t support subclassing.

## Topics

### Creating alerts
- [init(error: any Error)](nsalert/init(error:).md)
  Returns an alert initialized from information in an error object.
### Configuring alerts
- [func layout()](nsalert/layout.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](nsalert/alertstyle.md)
  Indicates the alert’s severity level.
- [NSAlert.Style](nsalert/style.md)
  The set of alert styles to style alerts in your app.
- [var accessoryView: NSView?](nsalert/accessoryview.md)
  The alert’s accessory view.
- [var showsHelp: Bool](nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsalert/helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](nsalert/delegate.md)
  The alert’s delegate.
### Displaying alerts
- [func runModal() -> NSApplication.ModalResponse](nsalert/runmodal.md)
  Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.
- [func beginSheetModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nsalert/beginsheetmodal(for:completionhandler:).md)
  Runs the alert modally as a sheet attached to the specified window.
- [var suppressionButton: NSButton?](nsalert/suppressionbutton.md)
  The alert’s suppression checkbox.
- [var showsSuppressionButton: Bool](nsalert/showssuppressionbutton.md)
  Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.
### Accessing alert text
- [var informativeText: String](nsalert/informativetext.md)
  The alert’s informative text.
- [var messageText: String](nsalert/messagetext.md)
  The alert’s message text or title.
### Accessing a custom alert icon
- [var icon: NSImage!](nsalert/icon.md)
  The custom icon displayed in the alert.
### Accessing alert response buttons
- [var buttons: [NSButton]](nsalert/buttons.md)
  The array of response buttons for the alert.
- [func addButton(withTitle: String) -> NSButton](nsalert/addbutton(withtitle:).md)
  Adds a button with a given title to the alert.
- [NSApplication.ModalResponse](nsapplication/modalresponse.md)
  A set of button return values for modal dialogs.
### Getting alert windows
- [var window: NSWindow](nsalert/window.md)
  The app-modal panel or document-modal sheet that corresponds to the alert.
### Deprecated
- [func beginSheetModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsalert/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the alert modally as an alert sheet attached to a specified window.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [Dialogs and Special Panels](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Dialog/Dialog.html#//apple_ref/doc/uid/10000071i)
- [protocol NSAlertDelegate](nsalertdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSAlert`](nsalert.md) object to respond to a user’s request for help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert)*