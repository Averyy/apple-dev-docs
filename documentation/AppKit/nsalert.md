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

The methods of the [`NSAlert`](nsalert.md) class allow you to specify alert level, alert text, button titles, and a custom icon should you require it. The class also lets your alerts display a help button and provides ways for apps to offer help specific to an alert.

To display an alert as a sheet, call the [`beginSheetModal(for:completionHandler:)`](nsalert/beginsheetmodal(for:completionhandler:).md) method; to display one as an app-modal dialog, use the [`runModal()`](nsalert/runmodal().md) method.

By design, an [`NSAlert`](nsalert.md) object is intended for a single alert—that is, an alert with a unique combination of title, buttons, and so on—that is displayed upon a particular condition. You should create an [`NSAlert`](nsalert.md) object for each alert dialog, creating it only  when you need to display an alert, and release it when you are done. If you have a particular alert dialog that you need to show repeatedly, you can retain and reuse an instance of [`NSAlert`](nsalert.md) for this dialog.

After creating an alert using one of the alert creation methods, you can customize it further prior to displaying it by customizing its attributes. See [`Instance Attributes`](nsalert#Instance-Attributes.md).

Unless you must maintain compatibility with existing alert-processing code that uses the function-based API, you should allocate (`alloc`) and initialize (`init`) the alert object, and then set its attributes using the appropriate methods of the `NSAlert` class.

##### Instance Attributes

[`NSAlert`](nsalert.md) objects have the following attributes:

- Type An alert’s type helps convey the importance or gravity of its message to the user. Specified with the [`alertStyle`](nsalert/alertstyle.md) property.
- Message text The main message of the alert. Specified with [`messageText`](nsalert/messagetext.md).
- Informative text Additional information about the alert. Specified with [`informativeText`](nsalert/informativetext.md).
- Icon An optional, custom icon to display in the alert, which is used instead of the default app icon. Specified with [`icon`](nsalert/icon.md).
- Help Alerts can let the user get help about them. Use [`helpAnchor`](nsalert/helpanchor.md) and [`showsHelp`](nsalert/showshelp.md).
- Response buttons By default an alert has one response button: the OK button. You can add more response buttons using the [`addButton(withTitle:)`](nsalert/addbutton(withtitle:).md) method.
- Suppression checkbox A suppression checkbox allows the user to suppress the display of a particular alert in subsequent occurrences of the event that triggers it. Use [`showsSuppressionButton`](nsalert/showssuppressionbutton.md).
- Accessory view An accessory view lets you add additional information to an alert; for example, a text field with contact information. Use [`accessoryView`](nsalert/accessoryview.md), [`layout()`](nsalert/layout().md).

##### Subclassing Notes

The `NSAlert` class is not designed for subclassing.

## Topics

### Creating Alerts
- [init(error: any Error)](nsalert/init(error:).md)
  Returns an alert initialized from information in an error object.
### Configuring Alerts
- [func layout()](nsalert/layout.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](nsalert/alertstyle.md)
  Indicates the alert’s severity level.
- [var accessoryView: NSView?](nsalert/accessoryview.md)
  The alert’s accessory view.
- [var showsHelp: Bool](nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsalert/helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](nsalert/delegate.md)
  The alert’s delegate.
### Displaying Alerts
- [func runModal() -> NSApplication.ModalResponse](nsalert/runmodal.md)
  Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.
- [func beginSheetModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](nsalert/beginsheetmodal(for:completionhandler:).md)
  Runs the alert modally as a sheet attached to the specified window.
- [func beginSheetModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsalert/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the alert modally as an alert sheet attached to a specified window.
- [var suppressionButton: NSButton?](nsalert/suppressionbutton.md)
  The alert’s suppression checkbox.
- [var showsSuppressionButton: Bool](nsalert/showssuppressionbutton.md)
  Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.
### Accessing Alert Text
- [var informativeText: String](nsalert/informativetext.md)
  The alert’s informative text.
- [var messageText: String](nsalert/messagetext.md)
  The alert’s message text or title.
### Accessing a Custom Alert Icon
- [var icon: NSImage!](nsalert/icon.md)
  The custom icon displayed in the alert.
### Accessing Alert Response Buttons
- [var buttons: [NSButton]](nsalert/buttons.md)
  The array of response buttons for the alert.
- [func addButton(withTitle: String) -> NSButton](nsalert/addbutton(withtitle:).md)
  Adds a button with a given title to the alert.
### Getting Alert Windows
- [var window: NSWindow](nsalert/window.md)
  The app-modal panel or document-modal sheet that corresponds to the alert.
### Constants
- [NSAlert.Style](nsalert/style.md)
  The set of alert styles to style alerts in your app.
- [NSApplication.ModalResponse](nsapplication/modalresponse.md)
  A set of button return values for modal dialogs.

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

- [Sheet Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Sheets.html#//apple_ref/doc/uid/10000002i)
- [Dialogs and Special Panels](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Dialog/Dialog.html#//apple_ref/doc/uid/10000071i)
- [protocol NSAlertDelegate](nsalertdelegate.md)
  A set of optional methods implemented by the delegate of an [`NSAlert`](nsalert.md) object to respond to a user’s request for help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert)*