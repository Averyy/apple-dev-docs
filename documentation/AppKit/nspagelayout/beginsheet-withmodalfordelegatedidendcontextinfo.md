# beginSheet(with:modalFor:delegate:didEnd:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func beginSheet(with printInfo: NSPrintInfo, modalFor docWindow: NSWindow, delegate: Any?, didEnd didEndSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

The `didEndSelector` argument must have the same signature as:

```objc
- (void)pageLayoutDidEnd:(NSPageLayout *)pageLayout returnCode:(int)returnCode  contextInfo: (void *)contextInfo;
```

The value passed as `returnCode` is either `NSCancelButton` or `NSOKButton`.

## Parameters

- `printInfo`: The   object to use.
- `docWindow`: The window to which the sheet is attached.
- `delegate`: The delegate to which   is sent. Can be  .
- `didEndSelector`: The selector sent to the delegate. Can be  .
- `contextInfo`: Context information object passed with  .

## See Also

- [func beginSheet(using: NSPrintInfo, on: NSWindow, completionHandler: ((NSPageLayout.Result) -> Void)?)](nspagelayout/beginsheet(using:on:completionhandler:).md)
- [func runModal() -> Int](nspagelayout/runmodal.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.
- [func runModal(with: NSPrintInfo) -> Int](nspagelayout/runmodal(with:).md)
  Displays the page layout panel and begins the modal loop using the specified print info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/beginsheet(with:modalfor:delegate:didend:contextinfo:))*