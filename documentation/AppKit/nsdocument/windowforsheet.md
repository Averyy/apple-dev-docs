# windowForSheet

**Framework**: AppKit  
**Kind**: property

Returns the document window to use as the parent of a document-modal sheet.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windowForSheet: NSWindow? { get }
```

#### Discussion

This method searches the document’s window controllers for the most suitable window to use when displaying the sheet.

The value of this property may be `nil`, in which case the sender should present an app-modal panel. The `NSDocument` implementation of this property sets the value to the window of the first window controller, or `[NSApp mainWindow]` if there are no window controllers or if the first window controller has no window.

## See Also

- [func showWindows()](nsdocument/showwindows.md)
  Displays all of the document’s windows, bringing them to the front and making them main or key as necessary.
- [func setWindow(NSWindow?)](nsdocument/setwindow(_:).md)
  Sets the window outlet of this document to the specified value.
- [var displayName: String!](nsdocument/displayname.md)
  The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.
- [func defaultDraftName() -> String](nsdocument/defaultdraftname.md)
  Returns the default draft name for the document subclass.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsdocument/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/windowforsheet)*