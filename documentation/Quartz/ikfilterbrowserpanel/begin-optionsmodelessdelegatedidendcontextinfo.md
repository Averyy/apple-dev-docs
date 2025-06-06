# begin(options:modelessDelegate:didEnd:contextInfo:)

**Framework**: Quartz  
**Kind**: method

Displays the filter browser in a new utility window, unless the filter browser is already open.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func begin(options inOptions: [AnyHashable : Any]! = [:], modelessDelegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!)
```

#### Discussion

When the filter browser session ends, `didEndSelector` is invoked on the modeless delegate, passing `contextInfo` as an argument. The selector `didEndSelector` must have the following signature:

`- (void)openPanelDidEnd:(NSOpenPanel *)panel returnCode:(int)returnCode  contextInfo:(void  *)contextInfo`

The `returnCode` value passed to the selector is set to [`NSOKButton`](https://developer.apple.com/documentation/AppKit/NSOKButton) if the user validates, or to [`NSCancelButton`](https://developer.apple.com/documentation/AppKit/NSCancelButton) if the user cancels.

## Parameters

- `inOptions`: A dictionary of options that describe the configuration to use for the filter browser user interface. For the possible keys you can supply see    and the constant  .
- `modelessDelegate`: The object that will invoke the selector    when the filter browser session terminates.
- `didEndSelector`: The selector to invoke when the filter browser session terminates.
- `contextInfo`: Any data that must be passed as an argument to the delegate through   after the filter browser session terminates.

## See Also

- [func filterBrowserView(options: [AnyHashable : Any]!) -> IKFilterBrowserView!](ikfilterbrowserpanel/filterbrowserview(options:).md)
  Returns a view that contains a filter browser.
- [func beginSheet(options: [AnyHashable : Any]!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/beginsheet(options:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays the filter browser in a sheet—that is, a dialog that is attached to its parent window and must be dismissed by the user.
- [func runModal(options: [AnyHashable : Any]!) -> Int32](ikfilterbrowserpanel/runmodal(options:).md)
  Displays the filter browser in a modal dialog that must be dismissed by the user but that is not  attached to a window.
- [func finish(Any!)](ikfilterbrowserpanel/finish(_:).md)
  Closes a filter browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel/begin(options:modelessdelegate:didend:contextinfo:))*