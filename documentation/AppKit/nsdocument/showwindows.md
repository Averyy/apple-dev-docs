# showWindows()

**Framework**: AppKit  
**Kind**: method

Displays all of the document’s windows, bringing them to the front and making them main or key as necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func showWindows()
```

## See Also

- [func setWindow(NSWindow?)](nsdocument/setwindow(_:).md)
  Sets the window outlet of this document to the specified value.
- [var windowForSheet: NSWindow?](nsdocument/windowforsheet.md)
  Returns the document window to use as the parent of a document-modal sheet.
- [var displayName: String!](nsdocument/displayname.md)
  The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.
- [func defaultDraftName() -> String](nsdocument/defaultdraftname.md)
  Returns the default draft name for the document subclass.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsdocument/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/showwindows())*