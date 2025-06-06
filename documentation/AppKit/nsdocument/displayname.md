# displayName

**Framework**: AppKit  
**Kind**: property

The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var displayName: String! { get set }
```

#### Discussion

If the document has been saved, the display name is the last component of the directory location of the saved file (for example, “`MyDocument`” if the path is “`/tmp/MyDocument.rtf`”). If the document is new, `NSDocument` makes the display name “Untitled n,” where n is a number in a sequence of new and unsaved documents. The displayable name also takes into account whether the document’s filename extension should be hidden. Subclasses of `NSWindowController` can override [`windowTitle(forDocumentDisplayName:)`](nswindowcontroller/windowtitle(fordocumentdisplayname:).md) to modify the display name as it appears in window titles.

## See Also

- [func showWindows()](nsdocument/showwindows.md)
  Displays all of the document’s windows, bringing them to the front and making them main or key as necessary.
- [func setWindow(NSWindow?)](nsdocument/setwindow(_:).md)
  Sets the window outlet of this document to the specified value.
- [var windowForSheet: NSWindow?](nsdocument/windowforsheet.md)
  Returns the document window to use as the parent of a document-modal sheet.
- [func defaultDraftName() -> String](nsdocument/defaultdraftname.md)
  Returns the default draft name for the document subclass.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsdocument/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/displayname)*