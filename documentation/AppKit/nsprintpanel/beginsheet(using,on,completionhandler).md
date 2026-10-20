# beginSheet(using:on:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow, completionHandler handler: ((NSPrintPanel.Result) -> Void)? = nil)
```

```swift
func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow) async -> NSPrintPanel.Result
```

```objc
- (void) beginSheetUsingPrintInfo:(NSPrintInfo *) printInfo onWindow:(NSWindow *) parentWindow completionHandler:(void (^)(NSPrintPanelResult result)) handler;
```

#### Discussion

## See Also

### Running the Panel
- [func runModal() -> Int](./runmodal%28%29.md)
  Displays the Print panel and begins the modal loop.
- [func runModal(with: NSPrintInfo) -> Int](./runmodal%28with%29.md)
  Displays the Print panel and runs the modal loop using the specified printing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/beginsheet(using:on:completionhandler:))*