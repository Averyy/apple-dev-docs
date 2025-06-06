# filterBrowserView(options:)

**Framework**: Quartz  
**Kind**: method

Returns a view that contains a filter browser.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func filterBrowserView(options inOptions: [AnyHashable : Any]! = [:]) -> IKFilterBrowserView!
```

#### Return Value

A filter browser view that is configured as specified.

#### Discussion

Use this method to add a view that contains the filter browser to your custom user interface. To dismiss the filter browser view, invoke the [`finish(_:)`](ikfilterbrowserpanel/finish(_:).md) method.

## Parameters

- `inOptions`: A dictionary of options that describe the configuration to use for the filter browser user interface. For the possible keys you can supply see    and the constant  .

## See Also

- [func begin(options: [AnyHashable : Any]!, modelessDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/begin(options:modelessdelegate:didend:contextinfo:).md)
  Displays the filter browser in a new utility window, unless the filter browser is already open.
- [func beginSheet(options: [AnyHashable : Any]!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/beginsheet(options:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays the filter browser in a sheet—that is, a dialog that is attached to its parent window and must be dismissed by the user.
- [func runModal(options: [AnyHashable : Any]!) -> Int32](ikfilterbrowserpanel/runmodal(options:).md)
  Displays the filter browser in a modal dialog that must be dismissed by the user but that is not  attached to a window.
- [func finish(Any!)](ikfilterbrowserpanel/finish(_:).md)
  Closes a filter browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel/filterbrowserview(options:))*