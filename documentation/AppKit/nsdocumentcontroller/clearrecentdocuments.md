# clearRecentDocuments(_:)

**Framework**: AppKit  
**Kind**: method

Empties the recent documents list for the application.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func clearRecentDocuments(_ sender: Any?)
```

#### Discussion

This is the action for the Clear menu command, but it can be called directly if necessary.

## See Also

- [var maximumRecentDocumentCount: Int](nsdocumentcontroller/maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func noteNewRecentDocumentURL(URL)](nsdocumentcontroller/notenewrecentdocumenturl(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [func noteNewRecentDocument(NSDocument)](nsdocumentcontroller/notenewrecentdocument(_:).md)
  Adds or replaces an Open Recent menu item corresponding to the document.
- [var recentDocumentURLs: [URL]](nsdocumentcontroller/recentdocumenturls.md)
  The list of recent-document URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/clearrecentdocuments(_:))*