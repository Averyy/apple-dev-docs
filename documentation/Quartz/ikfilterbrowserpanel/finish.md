# finish(_:)

**Framework**: Quartz  
**Kind**: method

Closes a filter browser view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func finish(_ sender: Any!)
```

#### Discussion

Invoke this action when you want to dismiss the filter browser.

## Parameters

- `sender`: The object that invokes the action, such as an OK or Cancel button.

## See Also

- [func filterBrowserView(options: [AnyHashable : Any]!) -> IKFilterBrowserView!](ikfilterbrowserpanel/filterbrowserview(options:).md)
  Returns a view that contains a filter browser.
- [func begin(options: [AnyHashable : Any]!, modelessDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/begin(options:modelessdelegate:didend:contextinfo:).md)
  Displays the filter browser in a new utility window, unless the filter browser is already open.
- [func beginSheet(options: [AnyHashable : Any]!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/beginsheet(options:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays the filter browser in a sheet—that is, a dialog that is attached to its parent window and must be dismissed by the user.
- [func runModal(options: [AnyHashable : Any]!) -> Int32](ikfilterbrowserpanel/runmodal(options:).md)
  Displays the filter browser in a modal dialog that must be dismissed by the user but that is not  attached to a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel/finish(_:))*