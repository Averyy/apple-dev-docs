# runModal(options:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Displays the filter browser in a modal dialog that must be dismissed by the user but that is not  attached to a window.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func runModal(options inOptions: [AnyHashable : Any]! = [:]) -> Int32
```

```objc
- (int) runModalWithOptions:(NSDictionary *) inOptions;
```

#### Return Value

Either [`NSOKButton`](../../AppKit/nsokbutton.md) if the user validates, or [`NSCancelButton`](../../AppKit/nscancelbutton.md) if the user cancels.

## Parameters

- `inOptions`: A dictionary of options that describe the configuration to use for the filter browser user interface. For the possible keys you can supply see  [Filter Browser Option Keys](../filter-browser-option-keys.md) and the constant [`IKUISizeFlavor`](../ikuisizeflavor.md).

## See Also

### Displaying and Running the Panel
- [func filterBrowserView(options: [AnyHashable : Any]!) -> IKFilterBrowserView!](./filterbrowserview%28options%29.md)
  Returns a view that contains a filter browser.
- [func begin(options: [AnyHashable : Any]!, modelessDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./begin%28options,modelessdelegate,didend,contextinfo%29.md)
  Displays the filter browser in a new utility window, unless the filter browser is already open.
- [func beginSheet(options: [AnyHashable : Any]!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28options,modalfor,modaldelegate,didend,contextinfo%29.md)
  Displays the filter browser in a sheet—that is, a dialog that is attached to its parent window and must be dismissed by the user.
- [func finish(Any!)](./finish%28_%29.md)
  Closes a filter browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel/runmodal(options:))*