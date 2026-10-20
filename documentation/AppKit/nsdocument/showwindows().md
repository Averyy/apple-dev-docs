# showWindows()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays all of the document’s windows, bringing them to the front and making them main or key as necessary.

**Availability**:
- macOS

## Declaration

```swift
func showWindows()
```

```objc
- (void) showWindows;
```

## See Also

### Managing Document Windows
- [func setWindow(NSWindow?)](./setwindow%28_%29.md)
  Sets the window outlet of this document to the specified value.
- [var windowForSheet: NSWindow?](./windowforsheet.md)
  Returns the document window to use as the parent of a document-modal sheet.
- [var displayName: String!](./displayname.md)
  The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.
- [func defaultDraftName() -> String](./defaultdraftname%28%29.md)
  Returns the default draft name for the document subclass.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](./encoderestorablestate%28with,backgroundqueue%29.md)
  Saves the interface-related state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/showwindows())*