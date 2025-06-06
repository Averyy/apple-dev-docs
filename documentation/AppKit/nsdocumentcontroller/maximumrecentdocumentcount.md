# maximumRecentDocumentCount

**Framework**: AppKit  
**Kind**: property

The maximum number of items that may be presented in the standard Open Recent menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var maximumRecentDocumentCount: Int { get }
```

#### Discussion

A value of 0 indicates that `NSDocumentController` will not attempt to add an Open Recent menu to your application’s File menu, although `NSDocumentController` will not attempt to remove any preexisting Open Recent menu item. The default implementation returns a value that is subject to change and may or may not be derived from a setting made by the user in System Preferences.

## See Also

- [func clearRecentDocuments(Any?)](nsdocumentcontroller/clearrecentdocuments(_:).md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocumentURL(URL)](nsdocumentcontroller/notenewrecentdocumenturl(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [func noteNewRecentDocument(NSDocument)](nsdocumentcontroller/notenewrecentdocument(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the document.
- [var recentDocumentURLs: [URL]](nsdocumentcontroller/recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/maximumrecentdocumentcount)*