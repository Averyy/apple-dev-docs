# beginSheet(with:modalFor:delegate:didEnd:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents a page setup sheet for the specified print info object, document-modal relative to the specified window.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```swift
func beginSheet(with printInfo: NSPrintInfo, modalFor docWindow: NSWindow, delegate: Any?, didEnd didEndSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) beginSheetWithPrintInfo:(NSPrintInfo *) printInfo modalForWindow:(NSWindow *) docWindow delegate:(id) delegate didEndSelector:(SEL) didEndSelector contextInfo:(void *) contextInfo;
```

#### Discussion

The `didEndSelector` argument must have the same signature as:

```objc
- (void)pageLayoutDidEnd:(NSPageLayout *)pageLayout returnCode:(int)returnCode  contextInfo: (void *)contextInfo;
```

The value passed as `returnCode` is either `NSCancelButton` or `NSOKButton`.

## Parameters

- `printInfo`: The `NSPrintInfo` object to use.
- `docWindow`: The window to which the sheet is attached.
- `delegate`: The delegate to which `didEndSelector` is sent. Can be `nil`.
- `didEndSelector`: The selector sent to the delegate. Can be `nil`.
- `contextInfo`: Context information object passed with `didEndSelector`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/beginsheet(with:modalfor:delegate:didend:contextinfo:))*