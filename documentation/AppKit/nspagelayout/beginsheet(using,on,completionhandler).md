# beginSheet(using:on:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow, completionHandler handler: ((NSPageLayout.Result) -> Void)? = nil)
```

```swift
func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow) async -> NSPageLayout.Result
```

```objc
- (void) beginSheetUsingPrintInfo:(NSPrintInfo *) printInfo onWindow:(NSWindow *) parentWindow completionHandler:(void (^)(NSPageLayoutResult result)) handler;
```

## See Also

### Running the page setup dialog
- [func runModal() -> Int](./runmodal%28%29.md)
  Displays the page layout panel and begins the modal loop using the shared print info object.
- [func runModal(with: NSPrintInfo) -> Int](./runmodal%28with%29.md)
  Displays the page layout panel and begins the modal loop using the specified print info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/beginsheet(using:on:completionhandler:))*