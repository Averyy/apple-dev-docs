# beginCriticalSheet(_:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts a document-modal session and presents the specified critical sheet.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func beginCriticalSheet(_ sheetWindow: NSWindow, completionHandler handler: ((NSApplication.ModalResponse) -> Void)? = nil)
```

```swift
func beginCriticalSheet(_ sheetWindow: NSWindow) async -> NSApplication.ModalResponse
```

```objc
- (void) beginCriticalSheet:(NSWindow *) sheetWindow completionHandler:(void (^)(NSModalResponse returnCode)) handler;
```

#### Discussion

This method displays the sheet—on top of the window’s current sheet, if one exists—makes it key and returns control to the caller. While the sheet remains visible, most events targeted at the receiver are prohibited. The runloop does not enter any special mode to accomplish this.

If the window already has a sheet when this method runs, the existing sheet is temporarily disabled while the critical sheet is presented. When the critical sheet is dismissed, the previously presented sheet continues its standard operation.

The sheet’s window never displays a title, regardless of its [`title`](./title.md) string, its [`titleVisibility`](./titlevisibility-swift.property.md) value, or whether its style mask includes the [`titled`](./stylemask-swift.struct/titled.md) flag.

## Parameters

- `sheetWindow`: The window object that represents the critical sheet to present. A critical sheet contains content that is time-critical or very important to the user.
- `handler`: The completion handler that gets called when the sheet’s modal session ends.

## See Also

### Managing Sheets
- [var attachedSheet: NSWindow?](./attachedsheet.md)
  The sheet attached to the window.
- [var isSheet: Bool](./issheet.md)
  A Boolean value that indicates whether the window has ever run as a modal sheet.
- [func beginSheet(NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](./beginsheet%28_,completionhandler%29.md)
  Starts a document-modal session and presents—or queues for presentation—a sheet.
- [func endSheet(NSWindow)](./endsheet%28_%29-4dmmq.md)
  Ends a document-modal session and dismisses the specified sheet.
- [func endSheet(NSWindow, returnCode: NSApplication.ModalResponse)](./endsheet%28_,returncode%29.md)
  Ends a document-modal session and dismisses the specified sheet.
- [var sheetParent: NSWindow?](./sheetparent.md)
  The window to which the sheet is attached.
- [var sheets: [NSWindow]](./sheets.md)
  An array of the sheets currently attached to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/begincriticalsheet(_:completionhandler:))*