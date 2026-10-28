# showsSuppressionButton

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether the alert includes a suppression checkbox, which you can employ to allow a user to opt out of seeing the alert again.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var showsSuppressionButton: Bool { get set }
```

```objc
@property BOOL showsSuppressionButton;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md), which specifies the absence of a suppression checkbox in the alert. Set the value to [`true`](../../Swift/true.md) to show a suppression checkbox in the alert.

By default, a suppression checkbox has the title, “Do not show this message again.” In macOS 11.0 and later, if the alert displays multiple buttons that prompt the user to make a choice, the title is “Do not ask again.” To customize it, use the checkbox’s `title` property, as follows:

```swift
myAlert.suppressionButton.title = "Do not show this warning again"
```

To create an alert that responds to the selection state of the suppression checkbox, use code like that shown in Listing 1 to produce the alert shown below.

Listing 1. Creating an alert with a suppression checkbox

```swift
let alertSuppressionKey = "AlertSuppression"
let defaults = UserDefaults.standard

if defaults.bool(forKey: alertSuppressionKey) {
    print("Alert suppressed")
} else {
    let anAlert = NSAlert()
    anAlert.messageText = "Message text."
    anAlert.informativeText = "Informative Text."
    anAlert.showsSuppressionButton = true
    anAlert.runModal()

    if let suppressionButton = anAlert.suppressionButton,
       suppressionButton.state == .on {
        defaults.set(true, forKey: alertSuppressionKey)
    }
}
```

![Alert with a suppression checkbox and customized text](https://developer.apple.com/tutorials/images/com.apple.appkit/media-3686600@2x.png)

## See Also

### Displaying alerts
- [func runModal() -> NSApplication.ModalResponse](./runmodal%28%29.md)
  Runs the alert as an app-modal dialog and returns the constant that identifies the button clicked.
- [func beginSheetModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](./beginsheetmodal%28for,completionhandler%29.md)
  Runs the alert modally as a sheet attached to the specified window.
- [var suppressionButton: NSButton?](./suppressionbutton.md)
  The alert’s suppression checkbox.
- [func beginSheetModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the alert modally as an alert sheet attached to a specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/showssuppressionbutton)*