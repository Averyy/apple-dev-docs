# begin(options:modelessDelegate:didEnd:contextInfo:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Displays the filter browser in a new utility window, unless the filter browser is already open.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func begin(options inOptions: [AnyHashable : Any]! = [:], modelessDelegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!)
```

```objc
- (void) beginWithOptions:(NSDictionary *) inOptions modelessDelegate:(id) modelessDelegate didEndSelector:(SEL) didEndSelector contextInfo:(void *) contextInfo;
```

## Discussion

When the filter browser session ends, `didEndSelector` is invoked on the modeless delegate, passing `contextInfo` as an argument. The selector `didEndSelector` must have the following signature:

`- (void)openPanelDidEnd:(NSOpenPanel *)panel returnCode:(int)returnCode  contextInfo:(void  *)contextInfo`

The `returnCode` value passed to the selector is set to [`NSOKButton`](../../AppKit/nsokbutton.md) if the user validates, or to [`NSCancelButton`](../../AppKit/nscancelbutton.md) if the user cancels.

## Parameters

- `inOptions`: A dictionary of options that describe the configuration to use for the filter browser user interface. For the possible keys you can supply see  [Filter Browser Option Keys](../filter-browser-option-keys.md) and the constant [`IKUISizeFlavor`](../ikuisizeflavor.md).
- `modelessDelegate`: The object that will invoke the selector  `didEndSelector` when the filter browser session terminates.
- `didEndSelector`: The selector to invoke when the filter browser session terminates.
- `contextInfo`: Any data that must be passed as an argument to the delegate through `didEndSelector` after the filter browser session terminates.

## See Also

### Displaying and Running the Panel
- [func filterBrowserView(options: [AnyHashable : Any]!) -> IKFilterBrowserView!](./filterbrowserview%28options%29.md)
  Returns a view that contains a filter browser.
- [func beginSheet(options: [AnyHashable : Any]!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28options,modalfor,modaldelegate,didend,contextinfo%29.md)
  Displays the filter browser in a sheet—that is, a dialog that is attached to its parent window and must be dismissed by the user.
- [func runModal(options: [AnyHashable : Any]!) -> Int32](./runmodal%28options%29.md)
  Displays the filter browser in a modal dialog that must be dismissed by the user but that is not  attached to a window.
- [func finish(Any!)](./finish%28_%29.md)
  Closes a filter browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel/begin(options:modelessdelegate:didend:contextinfo:))*