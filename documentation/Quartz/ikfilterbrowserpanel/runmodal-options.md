# runModal(options:)

**Framework**: Quartz  
**Kind**: method

Displays the filter browser in a modal dialog that must be dismissed by the user but that is not  attached to a window.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func runModal(options inOptions: [AnyHashable : Any]! = [:]) -> Int32
```

#### Return Value

Either [`NSOKButton`](https://developer.apple.com/documentation/AppKit/NSOKButton) if the user validates, or [`NSCancelButton`](https://developer.apple.com/documentation/AppKit/NSCancelButton) if the user cancels.

## Parameters

- `inOptions`: A dictionary of options that describe the configuration to use for the filter browser user interface. For the possible keys you can supply see    and the constant  .

## See Also

- [func filterBrowserView(options: [AnyHashable : Any]!) -> IKFilterBrowserView!](ikfilterbrowserpanel/filterbrowserview(options:).md)
  Returns a view that contains a filter browser.
- [func begin(options: [AnyHashable : Any]!, modelessDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/begin(options:modelessdelegate:didend:contextinfo:).md)
  Displays the filter browser in a new utility window, unless the filter browser is already open.
- [func beginSheet(options: [AnyHashable : Any]!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/beginsheet(options:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays the filter browser in a sheet—that is, a dialog that is attached to its parent window and must be dismissed by the user.
- [func finish(Any!)](ikfilterbrowserpanel/finish(_:).md)
  Closes a filter browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel/runmodal(options:))*