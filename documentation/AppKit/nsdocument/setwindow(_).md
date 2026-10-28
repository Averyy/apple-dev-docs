# setWindow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the window outlet of this document to the specified value.

**Availability**:
- macOS

## Declaration

```swift
func setWindow(_ window: NSWindow?)
```

```objc
- (void) setWindow:(NSWindow *) window;
```

## Discussion

This method is invoked automatically during the loading of any nib for which this document is the file’s owner, if the file’s owner `window` outlet is connected in the nib. You should not invoke this method directly, and typically you would not override it either.

## Parameters

- `window`: The window to which the receiver’s `window` outlet points.

## See Also

### Managing Document Windows
- [func showWindows()](./showwindows%28%29.md)
  Displays all of the document’s windows, bringing them to the front and making them main or key as necessary.
- [var windowForSheet: NSWindow?](./windowforsheet.md)
  Returns the document window to use as the parent of a document-modal sheet.
- [var displayName: String!](./displayname.md)
  The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.
- [func defaultDraftName() -> String](./defaultdraftname%28%29.md)
  Returns the default draft name for the document subclass.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](./encoderestorablestate%28with,backgroundqueue%29.md)
  Saves the interface-related state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/setwindow(_:))*