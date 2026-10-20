# beginSheet(with:modalFor:delegate:didEnd:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays a Print panel sheet and runs it modally for the specified window.

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

When the modal session ends, if `modalDelegate` and `didEndSelector` contain non-`nil` values, the method specified by `didEndSelector` is invoked on the object in `modalDelegate`. The data you specify in `contextInfo` is passed as a parameter to the `didEndSelector` method. The object in `modalDelegate` is not the same as a delegate assigned to the panel. Modal delegates for sheets are temporary and the relationship lasts only until the sheet is dismissed.

The `didEndSelector` argument must have the following signature:

```objc
- (void)printPanelDidEnd:(NSPrintPanel *)printPanel returnCode:(NSInteger)returnCode  contextInfo: (void *)contextInfo;
```

The value passed as `returnCode` is either `NSCancelButton` or `NSOKButton`. The value `NSOKButton` is returned even if the user clicked the Preview button.

## Parameters

- `printInfo`: The printing information for the current job.
- `docWindow`: The window on which to display the sheet.
- `delegate`: A modal delegate object assigned to handle the closing of the Print panel sheet.
- `didEndSelector`: The selector to call on the modal delegate object when the sheet is dismissed. The signature of this method is listed in the Discussion section.
- `contextInfo`: A pointer to context data the `didEndSelector` method needs to process the sheet. This data is user-defined and may be `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/beginsheet(with:modalfor:delegate:didend:contextinfo:))*