# defaultDraftName()

**Framework**: AppKit  
**Kind**: method

Returns the default draft name for the document subclass.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func defaultDraftName() -> String
```

#### Discussion

The default implementation of this method returns the string “Untitled”, as adjusted according to the user’s specified locale. Your app should typically return a name that describes the kind of document. For example, a spreadsheet app could return “Spreadsheet”. A document created from a template could return the name of the template, for example, “Résumé”.

When a document has not yet been assigned a name, and has not yet been autosaved with the [`NSDocument.SaveOperationType.autosaveAsOperation`](nsdocument/saveoperationtype/autosaveasoperation.md) save operation type, the document bases the default name on the value in the [`displayName`](nsdocument/displayname.md) property.

If there is a already another document or file in the same place and with the same name as would be returned by this method, [`NSDocument`](nsdocument.md) appends a number to the [`defaultDraftName()`](nsdocument/defaultdraftname().md) string.

## See Also

- [func showWindows()](nsdocument/showwindows.md)
  Displays all of the document’s windows, bringing them to the front and making them main or key as necessary.
- [func setWindow(NSWindow?)](nsdocument/setwindow(_:).md)
  Sets the window outlet of this document to the specified value.
- [var windowForSheet: NSWindow?](nsdocument/windowforsheet.md)
  Returns the document window to use as the parent of a document-modal sheet.
- [var displayName: String!](nsdocument/displayname.md)
  The name of the document as displayed in the title bars of the document’s windows and in alert dialogs related to the document.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsdocument/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/defaultdraftname())*